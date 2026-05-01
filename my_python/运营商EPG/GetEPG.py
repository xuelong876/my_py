#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote
import time
import os
import sys
import configparser
import threading

class EPGGenerator:
    def __init__(self):
        # 获取 py 文件所在目录
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # 配置文件固定放在 py 文件目录下
        self.config_file = os.path.join(self.script_dir, 'config.ini')
        self.config = self.load_config()
        self.lock = threading.Lock()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'EPG Generator/1.0'
        })
    
    def load_config(self):
        """加载配置文件"""
        config = configparser.ConfigParser()
        
        # 如果配置文件不存在，创建默认配置
        if not os.path.exists(self.config_file):
            self.create_default_config()
        
        config.read(self.config_file, encoding='utf-8')
        
        # 输出路径：如果配置了就用配置的，否则默认在 py 文件目录下的 epg.xml
        output_path = config.get('DEFAULT', 'outputPath', fallback='')
        if not output_path:
            output_path = os.path.join(self.script_dir, 'epg.xml')
        
        # 缓存目录：默认在 py 文件目录下的 cache
        cache_dir = config.get('DEFAULT', 'cacheDir', fallback='')
        if not cache_dir:
            cache_dir = os.path.join(self.script_dir, 'cache')
        
        return {
            'abilityString': config.get('DEFAULT', 'abilityString', fallback='0'),
            'channelUrlTemplate': config.get('DEFAULT', 'channelUrlTemplate', 
                fallback='http://test.com/cms-lvp-epg/lvps/channelList?abilityString={abilityString}&assortId=3&actionType=OpenNew&isShowNewProgram=true'),
            'progUrlTemplate': config.get('DEFAULT', 'progUrlTemplate',
                fallback='http://test.com/cms-lvp-epg/lvps/getAllProgramlist?abilityString={abilityString}&startDate={startDate}&endDate={endDate}&pos=fullplayer&uuid={uuid}'),
            'delayMs': config.getint('DEFAULT', 'delayMs', fallback=100),
            'debug': config.getint('DEFAULT', 'debug', fallback=0),
            'daysBackward': config.getint('DEFAULT', 'daysBackward', fallback=7),
            'daysForward': config.getint('DEFAULT', 'daysForward', fallback=2),
            'outputPath': output_path,
            'cacheDir': cache_dir,
            'channelIdMapping': self.parse_mapping(config.get('DEFAULT', 'channelIdMapping', fallback='')),
            'channelNameMapping': self.parse_mapping(config.get('DEFAULT', 'channelNameMapping', fallback=''))
        }
    
    def create_default_config(self):
        """创建默认配置文件"""
        default_output = os.path.join(self.script_dir, 'epg.xml')
        default_cache = os.path.join(self.script_dir, 'cache')
        
        default_config = f"""[DEFAULT]
# ========== 基础配置 ==========
# EPG配置参数
abilityString = 0

# API地址（请修改为实际地址）
channelUrlTemplate = http://your-real-api.com/channelList?abilityString={{abilityString}}&assortId=3&actionType=OpenNew&isShowNewProgram=true
progUrlTemplate = http://your-real-api.com/getAllProgramlist?abilityString={{abilityString}}&startDate={{startDate}}&endDate={{endDate}}&pos=fullplayer&uuid={{uuid}}

# 请求延迟（毫秒）
delayMs = 100

# 调试模式（0:关闭, 1:基本, 2:详细）
debug = 0

# 获取天数（往前N天，往后N天）
daysBackward = 7
daysForward = 2

# ========== 输出配置 ==========
# 输出文件路径（留空则默认：脚本目录/epg.xml）
# 示例1（绝对路径）：outputPath = /mnt/sda1/epg/epg.xml
# 示例2（相对路径）：outputPath = ./output/epg.xml
# 示例3（默认）：outputPath = 
outputPath = {default_output}

# 缓存目录（留空则默认：脚本目录/cache）
cacheDir = {default_cache}

# ========== 频道映射（可选）==========
# 频道ID映射（格式: 原ID:新ID;原ID2:新ID2）
channelIdMapping = 

# 频道名称映射（格式: 原名称:频道ID;原名称2:频道ID2）
channelNameMapping = 
"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            f.write(default_config)
        print(f"已创建配置文件: {self.config_file}")
        print("请修改配置文件中的API地址后再运行！")
        sys.exit(0)
    
    def parse_mapping(self, mapping_str):
        """解析映射配置"""
        mapping = {}
        if mapping_str:
            for item in mapping_str.split(';'):
                if ':' in item:
                    key, value = item.split(':', 1)
                    mapping[key.strip()] = value.strip()
        return mapping
    
    def url_encode_twice(self, text):
        """URL编码两次"""
        return quote(quote(text, safe=''), safe='')
    
    def http_get(self, url):
        """HTTP GET请求"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"HTTP请求失败: {url}, 错误: {e}")
            return ""
    
    def get_channels(self):
        """获取频道列表"""
        encoded_ability = self.url_encode_twice(self.config['abilityString'])
        url = self.config['channelUrlTemplate'].format(abilityString=encoded_ability)
        
        print(f"获取频道列表: {url}")
        response_text = self.http_get(url)
        if not response_text:
            return []
        
        try:
            data = json.loads(response_text)
            
            if data.get('resultCode') != '000':
                print(f"API返回错误: {data.get('resultCode')}")
                return []
            
            content = data.get('content', {})
            channels_data = content.get('channels', [])
            
            channels = []
            for ch in channels_data:
                uuid = ch.get('uuid', '')
                name = ch.get('name', '')
                num = ch.get('num', '')
                if uuid:
                    channels.append({'uuid': uuid, 'name': name, 'num': num})
            
            print(f"找到 {len(channels)} 个频道")
            return channels
            
        except json.JSONDecodeError as e:
            print(f"JSON解析失败: {e}")
            return []
    
    def generate_dates(self):
        """生成日期列表"""
        dates = []
        start_date = datetime.now() - timedelta(days=self.config['daysBackward'])
        total_days = self.config['daysBackward'] + self.config['daysForward']
        
        for i in range(total_days):
            date = start_date + timedelta(days=i)
            dates.append(date.strftime('%Y%m%d'))
        
        return dates
    
    def get_programmes_for_channel(self, channel, date):
        """获取单个频道单天的节目数据"""
        encoded_ability = self.url_encode_twice(self.config['abilityString'])
        url = self.config['progUrlTemplate'].format(
            abilityString=encoded_ability,
            startDate=date,
            endDate=date,
            uuid=channel['uuid']
        )
        
        # 缓存目录
        cache_dir = os.path.join(self.config['cacheDir'], date)
        os.makedirs(cache_dir, exist_ok=True)
        cache_file = os.path.join(cache_dir, f"{channel['num'] or channel['uuid']}_programmes.json")
        
        # 使用缓存
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    programmes = json.load(f)
                return programmes
            except:
                pass
        
        # 从API获取
        response_text = self.http_get(url)
        if response_text:
            time.sleep(self.config['delayMs'] / 1000.0)
        
        if not response_text:
            return []
        
        try:
            data = json.loads(response_text)
            if data.get('resultCode') != '000':
                return []
            
            content = data.get('content', {})
            programs_list = []
            if 'programs' in content:
                programs_list = content.get('programs', [])
            elif isinstance(content, list):
                for item in content:
                    programs_list.extend(item.get('programs', []))
            
            programmes = []
            for prog in programs_list:
                prog_name = prog.get('programName', '')
                start_time = prog.get('startTime', 0)
                end_time = prog.get('endTime', 0)
                category = prog.get('tvsouItemType', '')
                
                if not prog_name or start_time == 0 or end_time == 0:
                    continue
                
                channel_id = self.config['channelIdMapping'].get(channel['uuid'], 
                               channel['num'] or channel['uuid'])
                
                programmes.append({
                    'channel_id': channel_id,
                    'start_time': start_time,
                    'end_time': end_time,
                    'title': prog_name,
                    'category': category
                })
            
            if programmes:
                with open(cache_file, 'w', encoding='utf-8') as f:
                    json.dump(programmes, f, ensure_ascii=False, indent=2)
            
            return programmes
        except json.JSONDecodeError as e:
            print(f"JSON解析失败: {channel['name']} {date}, 错误: {e}")
            return []
    
    def get_all_programmes(self, channels, dates):
        """并发获取所有节目数据"""
        all_programmes = []
        total_tasks = len(channels) * len(dates)
        completed = 0
        
        print(f"\n开始获取节目数据 (共 {total_tasks} 个任务)...")
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for channel in channels:
                for date in dates:
                    future = executor.submit(self.get_programmes_for_channel, channel, date)
                    futures.append(future)
            
            for future in as_completed(futures):
                programmes = future.result()
                with self.lock:
                    all_programmes.extend(programmes)
                    completed += 1
                    if completed % 100 == 0 or completed == total_tasks:
                        percentage = (completed * 100) // total_tasks
                        print(f"  进度: {completed}/{total_tasks} ({percentage}%)")
        
        print(f"总共获取 {len(all_programmes)} 个节目")
        return all_programmes
    
    def timestamp_to_xml_time(self, timestamp):
        """时间戳转XML时间格式 (秒级)"""
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime('%Y%m%d%H%M%S')
    
    def escape_xml(self, text):
        """转义XML特殊字符"""
        replacements = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&apos;'
        }
        for char, escape in replacements.items():
            text = text.replace(char, escape)
        return text
    
    def generate_xml(self, channels, programmes):
        """生成EPG XML文件"""
        programmes.sort(key=lambda x: (x['channel_id'], x['start_time']))
        
        tv = ET.Element('tv')
        tv.set('generator-info-name', 'Python EPG Generator')
        
        added_channels = set()
        for ch in channels:
            channel_id = self.config['channelIdMapping'].get(ch['uuid'], 
                           ch['num'] or ch['uuid'])
            
            if channel_id in added_channels:
                continue
            added_channels.add(channel_id)
            
            channel_elem = ET.SubElement(tv, 'channel')
            channel_elem.set('id', channel_id)
            
            display_name = ET.SubElement(channel_elem, 'display-name')
            display_name.set('lang', 'zh')
            display_name.text = self.escape_xml(ch['name'])
        
        for prog in programmes:
            programme_elem = ET.SubElement(tv, 'programme')
            programme_elem.set('start', f"{self.timestamp_to_xml_time(prog['start_time'])} +0800")
            programme_elem.set('stop', f"{self.timestamp_to_xml_time(prog['end_time'])} +0800")
            programme_elem.set('channel', prog['channel_id'])
            
            title_elem = ET.SubElement(programme_elem, 'title')
            title_elem.set('lang', 'zh')
            title_elem.text = self.escape_xml(prog['title'])
            
            if prog['category']:
                category_elem = ET.SubElement(programme_elem, 'category')
                category_elem.set('lang', 'zh')
                category_elem.text = self.escape_xml(prog['category'])
        
        xml_str = ET.tostring(tv, encoding='unicode')
        dom = minidom.parseString(xml_str)
        pretty_xml = dom.toprettyxml(indent='  ')
        
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + pretty_xml.split('?>', 1)[1].lstrip()
    
    def clean_old_cache(self, dates_to_keep):
        """清理旧缓存"""
        cache_dir = self.config['cacheDir']
        if not os.path.exists(cache_dir):
            return
        
        keep_dates = set(dates_to_keep)
        deleted_count = 0
        
        for date_dir in os.listdir(cache_dir):
            if len(date_dir) == 8 and date_dir.isdigit():
                if date_dir not in keep_dates:
                    import shutil
                    shutil.rmtree(os.path.join(cache_dir, date_dir))
                    deleted_count += 1
                    print(f"  清理过期缓存: {date_dir}")
        
        if deleted_count > 0:
            print(f"  共清理 {deleted_count} 个过期缓存目录")
    
    def run(self):
        """主运行函数"""
        print("=" * 50)
        print("EPG 节目单生成器 (Python版本)")
        print("=" * 50)
        
        print(f"\n配置信息:")
        print(f"  脚本目录: {self.script_dir}")
        print(f"  配置文件: {self.config_file}")
        print(f"  往前天数: {self.config['daysBackward']}")
        print(f"  往后天数: {self.config['daysForward']}")
        print(f"  输出路径: {self.config['outputPath']}")
        print(f"  缓存目录: {self.config['cacheDir']}")
        
        # 1. 获取频道列表
        print("\n[1] 获取频道列表...")
        channels = self.get_channels()
        if not channels:
            print("错误：无法获取频道列表")
            return
        
        # 2. 生成日期列表
        dates = self.generate_dates()
        print(f"\n[2] 生成日期列表: {', '.join(dates)}")
        
        # 3. 清理旧缓存
        print("\n[3] 清理旧缓存...")
        self.clean_old_cache(dates)
        
        # 4. 获取所有节目数据
        print("\n[4] 获取节目数据...")
        programmes = self.get_all_programmes(channels, dates)
        
        if not programmes:
            print("警告：没有获取到任何节目数据")
        
        # 5. 生成XML文件
        print("\n[5] 生成EPG XML文件...")
        xml_content = self.generate_xml(channels, programmes)
        
        # 确保输出目录存在
        output_dir = os.path.dirname(self.config['outputPath'])
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        with open(self.config['outputPath'], 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"\n完成！生成 {self.config['outputPath']}")
        print(f"总节目数: {len(programmes)}")
        print("=" * 50)

if __name__ == '__main__':
    generator = EPGGenerator()
    generator.run()