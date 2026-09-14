import requests
import json
"""
"""
#接口地址
xiaosa_json_url="https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json"
#壁纸 logo spidir 地址
wallpaper="http://饭太硬.top/深色壁纸/api.php"
logo= "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/pg.gif"
spider="https://gitee.com/xuelong88/xiaosa_box/raw/master/spider.jar"
#排除站点名称
exclude_names=["短剧","123","戏曲","本地","抖音","推送","预告","动漫","看球","DJ","体育","听书","FM",
             "儿童","童趣","课堂","教育","急救","养生","知识","急救"]
#直播列表
lives=[
    {
      "name": "移动8m",
      "type": 0,
      "url": "https://gh-proxy.com/https://raw.githubusercontent.com/xuelong876/mybox_PG/refs/heads/main/live/YD8M.m3u",
      "playerType": 2,
      "ua": "okhttp/3.12.13",
      "logo": "https://cdn.jsdelivr.net/gh/xuelong876/channal_logo2@master/{name}.png",
      "epg": "http://cdn.1678520.xyz/epg/?ch={name}&date={date}"
    },
        {
      "name": "刺桐自营",
      "type": 0,
      "url": "https://www.cttv.vip/ys/json/ctzb.txt",
      "playerType": 2,
      "ua": "okhttp/3.12.13",
      "logo": "https://cdn.jsdelivr.net/gh/xuelong876/channal_logo2@master/{name}.png",
      "epg": "http://cdn.1678520.xyz/epg/?ch={name}&date={date}"
    }
]

# --- 名称美化（添加Emoji）---
def add_emoji_to_name(name: str) -> str:
    """添加Emoji到名称
    匹配规则：按列表顺序依次判断，命中第一条即返回
    """
    # 规则配置：(匹配类型, 匹配值, 结果模板/固定返回文本)
    # type: "startswith"前缀 / "endswith"后缀
    rules = [
        ("startswith", "豆瓣", "🏠豆瓣 • 潇洒👨"),
        ("startswith", "配置", "⚙️配置 • 中心🍅"),
        ("startswith", "哔哩", "🅱️{name}🍅"),
        ("endswith", "APP", "🐞{name}🍅"),
        ("endswith", "视频", "🎬{name}🍅"),
        ("endswith", "影视", "🎥{name}🍅"),
        ("endswith", ("4K", "网盘", "云盘"), "☁{name}🍅"),
        ("endswith", "磁力", "🧲{name}🍅"),
        ("endswith", "搜索", "🔍 {name}🍅"),
    ]

    # 入参校验
    if not isinstance(name, str):
        return ""

    for match_type, match_val, template in rules:
        if match_type == "startswith":
            if name.startswith(match_val):
                # 如果模板不含占位符，直接返回字符串；否则格式化
                if "{name}" in template:
                    return template.format(name=name)
                else:
                    return template
        elif match_type == "endswith":
            if name.endswith(match_val):
                return template.format(name=name)

    # 默认规则
    return f"🍅{name}🍅"
    #主程序 修改json文件
def main():
      """
      1；读取指定接口地址JSON 文件，转换为py字典
      2；修改壁纸和logo，jar地址
      3；修改lives键的值为指定路径
      4；遍历字典中键“"sites"的值，排除包含exclude_names中的站点名称的值，
      5，对各站点中的name添加emoji名称美化
      5；修改后的json文件，保存为指定路径

      """
      #获取在线json内容
      response = requests.get(xiaosa_json_url,timeout=10)
      data = response.json()
      #修改壁纸和logo，jar地址
      data["wallpaper"] = wallpaper
      data["logo"] = logo
      data["spider"] = spider
      #修改lives键的值为指定路径
      data["lives"] = lives
      
  
     #遍历字典中键“"sites"的值，排除包含exclude_names中的站点名称的值，
     # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
     #元素除了是 0、空、FALSE 外都算 TRUE。
      data["sites"] = [
        site for site in data["sites"] 
        if not any(
            exclude_name in site.get("name", "") 
            for exclude_name in exclude_names
        )
    ]
       

      #对各站点中的name添加emoji名称美化
      for site in data["sites"]:
        site["name"] = add_emoji_to_name(site["name"])
        #关闭自动换源
        site["changeable"]= 0
       # 保存修改后的json文件
      with open(r"C:\C盘下载\Tvbox_json\xiao.json", "w", encoding="utf-8") as f:
          json.dump(data, f, ensure_ascii=False, indent=2)
      print("处理完成，文件已保存")

main()

    


