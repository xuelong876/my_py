	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ++++    Pyton 库（模块）       安装：pip install py库 -i https://pypi.tuna.tsinghua.edu.cn/simple                     +++++
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __________________________________________________________________________________________________________________________
    ● 网络请求 requests 
    ● 三个处理时间库：time、datetime、calenda
    ● 数学计算 math (内置库)
    ● 数据存储 shelve（自带标准库）
    ● 字符串模块  string(标准库)
    ● 高阶函数functools模块
    ● sys python解释器交互
    ● Pillow （pil)  图像处理
    ● qdm 进度条模块
    ● Beautiful Soup 4 (bs4)     用于从 HTML/XML 文档中提取数据
    ● opencc 简繁体转换
    ● typing  typing_extensions 类型注释
    ● m3u8 模块
    ● aiohttp 模块
    ● multidict 模块
    ● fake_useragent
    ● lxml（更快解析器）
    ● aiohttp
    ● utils
    ● pystray
    ● pycryptodome
    ----------------------------------------------------------------------------------------------------------
    +++                                     网络请求 requests                                             ++++
    -----------------------------------------------------------------------------------------------------------
    一、基础安装
        pip install requests
        导入：import requests

    二、核心请求方法（最常用）
        1. GET：获取数据
        requests.get(url, params=None, **kwargs)

        2. POST：提交/创建数据
        requests.post(url, data=None, json=None, **kwargs)

        3. PUT：更新数据
        requests.put(url, data=None, **kwargs)

        4. DELETE：删除数据
        requests.delete(url, **kwargs)

        5. HEAD：仅获取响应头
        requests.head(url, **kwargs)

        6. OPTIONS：查看支持的请求方法
        requests.options(url, **kwargs)

    三、请求核心参数（必背）
        1. url：请求地址（字符串）
        2. params：GET 请求参数（字典）
        例：params={'key': 'value', 'page': 1}
        3. data：表单格式提交数据（字典）
        4. json：JSON 格式提交数据（字典/字符串）
        5. headers：请求头（字典，模拟浏览器、认证等）
        6. cookies：携带 Cookie（字典）
        7. files：上传文件
        例：files={'file': open('test.txt', 'rb')}
        8. timeout：超时时间（秒）
        例：timeout=5
        9. auth：基础认证
        例：auth=('username', 'password')
        10. verify：是否验证 SSL 证书（True/False）
        11. allow_redirects：是否允许重定向（True/False）
        12. proxies：设置代理
            例：proxies={'http': 'http://127.0.0.1:8080'}

     四、响应对象属性与方法
        res = requests.get(url)

        1. 响应状态
        res.status_code       # 状态码（200=成功，404=未找到，500=服务器错误）
        res.reason            # 状态码描述（OK / Not Found）
        res.ok                # 200-399 返回 True

        2. 响应内容
        res.text              # 文本格式内容（自动编码）
        res.content           # 字节格式（图片/文件）
        res.json()            # 解析 JSON 数据（返回字典）
        res.encoding          # 获取/设置编码（如 res.encoding='utf-8'）

        3. 响应头与Cookie
        res.headers           # 响应头（字典）
        res.cookies           # 服务器返回的 Cookie
        res.url               # 最终请求的 URL
        服务器返回的 headers 常见：
            Content-Type: 内容类型
            Content-Length: 大小
            Content-Encoding: 压缩
            Set-Cookie: 设置cookie
            Server: 服务器类型
            Date: 时间
            Cache-Control: 缓存
            Location: 重定向地址

        4. 其他
        res.elapsed           # 请求耗时
        res.history           # 重定向历史
        
        5  res.raise_for_status()  必须配合 try-except 使用
        作用：
            检查 HTTP 状态码
            4xx/5xx → 抛出 HTTPError
            2xx/3xx → 正常不报错

        好处：
            强制暴露请求错误
            避免程序静默失败

    五、常用状态码速查
        200 OK            请求成功
        201 Created       创建成功
        301/302           重定向
        400 Bad Request   参数错误
        401 Unauthorized  未授权
        403 Forbidden     禁止访问
        404 Not Found     地址不存在
        500 Server Error  服务器错误

    六、异常处理（必用）
        try:
            res = requests.get(url, timeout=5)
            res.raise_for_status()  # 状态码非200时抛出异常
        except requests.exceptions.Timeout:
            print("请求超时")
        except requests.exceptions.ConnectionError:
            print("网络连接失败")
        except requests.exceptions.HTTPError:
            print("HTTP 错误")
        except requests.exceptions.RequestException as e:
            print("请求异常：", e)

    七、实战示例
        1. 基础 GET 请求
        res = requests.get('https://httpbin.org/get')
        print(res.json())

        2. 带参数 GET
        params = {'wd': 'python', 'page': 1}
        res = requests.get('https://httpbin.org/get', params=params)

        3. 带请求头（模拟浏览器）
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers)

        4. POST 提交 JSON
        data = {'name': 'test', 'age': 18}
        res = requests.post('https://httpbin.org/post', json=data)

        5. 下载图片/文件
        res = requests.get('https://xxx.com/img.jpg')
        with open('test.jpg', 'wb') as f:
            f.write(res.content)

        6. 携带 Cookie
        cookies = {'token': '123456'}
        res = requests.get(url, cookies=cookies)

        7. 会话保持（登录后访问）
        s = requests.Session()
        s.post(login_url, data={'user': 'xxx'})
        res = s.get(user_info_url)

    八、高级用法
        1. 关闭 SSL 验证（内网/自签名证书）
        requests.get(url, verify=False)

        2. 自定义编码
        res.encoding = 'utf-8'

        3. 流式下载大文件
        res = requests.get(url, stream=True)
        with open('file.zip', 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                f.write(chunk)
        4  iter_content(chunk_size=1024)
         作用： 流式分块读取响应（大文件下载） 下载大文件、节省内存k,必须配合：stream=True
            参数：
            1. chunk_size：每次读取大小（字节）
                默认 1，常用 1024/8192
            2. decode_unicode：是否解码字符串
                下载文件用 False（默认）        
    -----------------------------------------------------------------------------------------------------------
    ++++      								 处理时间的库：time   											+++++
    -----------------------------------------------------------------------------------------------------------    
    ● #TODO:  year:年；  moon:月；  day: 天；  hour:小时； min:分钟； sec:秒；
            ● tm_year   年          (例如，1993年)
            ● tm mon    月          范围[1,12]
            ● tm_mday 每月第几天    范围[1,31]
            ● tm_hour   小时        范围[0,23]
            ● tm_min    分钟        范围[0，59]
            ● tm sec    秒          范围[0，61];见（2）中strftime（)描述
            ● tm_wday: 星期         范围[0，6]，星期一为0 ;
            ● tm_yday  每年第几天   范围[1,366]
            %y 两位数的年份表示（00-99）
                %Y 四位数的年份表示（000-9999）
                %m 月份（01-12）
                %d 月内中的一天（0-31）
                %H 24小时制小时数（0-23）
                %I 12小时制小时数（01-12）
                %M 分钟数（00=59）
                %S 秒（00-59）
                %a 本地简化星期名称
                %A 本地完整星期名称
                %b 本地简化的月份名称
                %B 本地完整的月份名称
                %c 本地相应的日期表示和时间表示
                %j 年内的一天（001-366）
                %p 本地A.M.或P.M.的等价符
                %U 一年中的星期数（00-53）星期天为星期的开始
                %w 星期（0-6），星期天为星期的开始
                %W 一年中的星期数（00-53）星期一为星期的开始
                %x 本地相应的日期表示
                %X 本地相应的时间表示
                %Z 当前时区的名称
                %% %号本身
 	● time模块的作用   时间获取、表达和转换。
    ● time模块表示时间的四种方式
        ● 时间戳（timestamp）的表现形式： 1581838663.752684
          t0 = time.time()   # 返回当前时间的时间戳1696218424.976779
       ● 时间对象（struct_time）表现形式 ：
                    time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, 
                                        tm_wday=3, tm_yday=335, tm_isdst=-1)
          t2 =time.strftime("%H:%M:%S")  # 12:31:18
       ● 自定义时间字符串（format_time）表示形式： '2020-02-16 17:37:28'
          t3 = time.strftime('%b %d %Y %H:%M:%S', time.gmtime(time.time()))#Oct 02 2023 03:52:40
       ● 默认时间字符串（defaut_time）表示形式：'Feb 16 2020 07:42:38'
         生成默认时间字符串的例子：time.asctime()默认以 %a %b %d %H:%M:%S %Y 形式展示
         t=(1993,6,20,23,21,1,2,0,0)
                         # t = (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec,tm_wday, tm_yday, tm_isdst)
         print(time.asctime(t))  #Wed Jun 20 23:21:01 1993
   ● sleep(secs) 推迟调用线程的运行，secs指秒数
   ● ctime(secs) 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
   ● localtime(secs)不传入参数的话，返回当前时间的时间对象（struct_time）;传入时间戳参数的话，返回指定时间时间对象。
   ● strftime(format, t)接收以时间对象（struct_time），并返回以自定义字符串所表示的当地时间，格式由 format 决定。
                         t默认本地时间可不写    format 一般习惯格式化成："%Y-%m-%d %H:%M:%S" 显示为2023-10-02 13:36:17
         示例：time.strftinme("%Y-%m-%d %H:%M:%S",time.localtime())    #显示为2023-10-02 13:36:17
   ● mktime(string, format)接受时间对象并返回时间戳（1970纪元后经过的浮点秒数）
   ● gmtime([secs])接收时间戳并返回时间对象
      print(time.gmtime(time.time()))  #time.struct_time(tm_year=2023, tm_mon=10, tm_mday=2, tm_hour=5,
                                          tm_min=43,tm_sec=59, tm_wday=0, tm_yday=275, tm_isdst=0)
   ● process_time()   返回当前进程执行 CPU 的时间总和，不包含睡眠时间
   ● perf_counter()  返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间    
   ● 上面两个函数 常常用来计算程序的执行耗时  
    -----------------------------------------------------------------------------------------------------------
    ++++                            处理时间的库：datetime                                                ++++++       
    -----------------------------------------------------------------------------------------------------------  
   ● datetime模块中包含如下类
        ● date	日期对象,常用的属性有year, month, day
        ● time	时间对象
        ● datetime	日期时间对象,常用的属性有hour, minute, second, microsecond
        ● datetime_CAPI	日期时间对象C语言接口
        ● timedelta	时间间隔，即两个时间点之间的长度
        ● tzinfo	时区信息对象
   ● datetime模块中包含的常量
           常量	      功能说明	              用法	         返回值
        MAXYEAR	  返回能表示的最大年份	datetime.MAXYEAR	   9999
        MINYEAR	  返回能表示的最小年份	datetime.MINYEAR	    1
   ● date类 ● date对象由year年份、month月份及day日期三部分构成：date（year，month，day)
            ● 通过year, month, day三个数据描述符可以进行访问：datetime.date(2017, 3, 22)
   ● date对象中包含的方法与属性
             方法名	    方法说明	         用法
            __eq__(…)	等于(x==y)    	 x.__eq__(y)
            __ge__(…)	大于等于(x>=y)	   x.__ge__(y)
            __gt__(…)	大于(x>y)     	 x.__gt__(y)
            __le__(…)	小于等于(x<=y)	   x.__le__(y)
            __lt__(…)	小于(x)            x.__lt__(y)
            __ne__(…)	不等于(x!=y)	    x.__ne__(y)
           ● 以上方法的返回值为True\False
      ● 获得二个日期相差多少天
            方法名	         方法说明    	用法
            __sub__(…)  	x - y	    x.__sub__(y)
            __rsub__(…)	    y - x	    x.__rsub__(y)
      ● 计算结果的返回值类型为datetime.timedelta, 如果获得整数类型的结果方法： x.__sub__(y).days
   ● ISO标准化日期
            1).* isocalendar(...)*:返回一个包含三个值的元组，三个值依次为：
                                       year年份，week number周数，weekday星期数（周一为1…周日为7)
            2). isoformat(...): 返回符合ISO 8601标准 (YYYY-MM-DD) 的日期字符串；
            3). isoweekday(...): 返回符合ISO标准的指定日期所在的星期数（周一为1…周日为7)
            4).与isoweekday(...)相似的还有一个weekday(...)方法，只不过是weekday(...)方法返回的周一为 0, 周日为 6
  ● 其他方法与属性
            1). timetuple(...):该方法为了兼容time.localtime(...)返回一个类型为time.struct_time的数组，
                                                                        但有关时间的部分元素值为0：
            2).toordinal(...)： 返回公元公历开始到现在的天数。公元1年1月1日为1
            3). replace(...)：返回一个替换指定日期字段的新date对象。参数3个可选参数，分别为year,month,day。
                                                            注意替换是产生新对象，不影响原date对象。    
            4).resolution：date对象表示日期的最小单位。这里是天。
            5).fromordinal(...)：将Gregorian日历时间转换为date对象；Gregorian Calendar ：一种日历表示方法，
                                                                    类似于我国的农历，西方国家使用比较多。 
            6).fromtimestamp(...)：根据给定的时间戮，返回一个date对象
            7).today(...)：返回当前日期
            8).max： date类能表示的最大的年、月、日的数值
            9).min： date类能表示的最小的年、月、日的数值
  ● 日期的字符串输出
      ● 如果你想将日期对象转化为字符串对象的话，可以用到__format__(...)方法以指定格式进行日期与此方法等价的方法为strftime(...)                                                                            
      ● 对象的属性和方法如下
             mport datetime
            now = datetime.datetime(2020,8,31,12,10,10)
            print("年为：",now.year)
            print("月为：",now.month)
            print("日为：",now.day)
            print("小时为：",now.hour)
            print("分钟为：",now.minute)
            print("秒数为：",now.second)
            print('当前日期为:', now.date() )
            print('当前时间:', now.time() )
            print("返回struct_time为",now.timetuple())   #  和date一样
            print("返回UTC的struct_time为",now.utctimetuple())
            print("返回的公历序列数为：",now.toordinal())   #  和date一样
            print("返回标准日期格式为：",now.isoformat())   #  和date一样
            print("返回的周几(1表示周一)：",now.isoweekday())    #  和date一样
            print("返回的周几(0表示周一)：",now.weekday())    #  和date一样  
            print("now.isocalendar():", now.isocalendar())  #  和date一样
            print("now.ctime():",now.ctime())   #  和date一样
            print("格式化时间为：",now.strftime('%Y/%m/%d %H:%M:%S'))   #  把日期按照format指定的格式进行格式化
    ● 总结：其中比较常见的应用有：
        ● 时间的转换：时间戳转日期（datetime.datetime.fromtimestamp(1234567896)）、
        ● 字符串转日期(datetime.datetime.strptime("2020/12/29 8:8:00",'%Y/%m/%d %H:%M:%S'))；
        ● 当前时间的计算：datetime.date.today()、datetime.datetime.now()；计算当前时间的年、月、日、时、分、秒、星期：直接
                  通过时间对象的属性提取即可；时间差的运用：如：五天前的日期datetime.timedelta(days=-5)；
    -----------------------------------------------------------------------------------------------------------
    ++++                                   处理时间的库：calenda                                           ++++
    -----------------------------------------------------------------------------------------------------------  
    ● calendar是和日历模块，calendar模块文件里定义了很多类型，主要有Calendar，TextCalendar以及HTMLCalendar类型
             其中，Calendar是TextCalendar与HTMLCalendar的基类。 calendar是内置库，直接使用import导入         
    ● calendar 模块相关方法
        ● firstweekday()	设置每星期的第一天数值
        ● isleap(year)	判断是闰年，则返回Ture
        ● leapdays(y1,y2)	计算要y1与y2的闰年数
        ● weekday(year,month,day)	返回某日是星期几
        ● weekheader(n)	星期几的缩写名的头
        ● mothrange(year,month)	计算出指定年份的某月第一天是星期几和天数
        ● prmonth(theyear,themonth,w=0,1=0)	格式化打印指定年的某月的日历
        ● month(theyear,themonth,w=0,1=0)	使用Text类formation()以多行字符串形式返回月份日历
        ● prcal(year,w=1,1=0,c=6,m=3)	格式化打印出整年的日历
        ● calendar(year,w=1,1=0,c=6,m=3)	以整年3列的日历多行字符串的形式的日历
          ● theyear指定年；themonth指定月  w:日期之间的宽度   l:指定每行日期之间的行数  c:月之间的宽度； m:将12个月分为m列
    ● calendar 模块属性
        ● day_name	当前语言环境下星期几的数组
        ● day_abbr	当前语言环境下星期几的缩写
        ● month_name	当前语言下一年的月份数组
        ● month_abbr	当前语言下一年的月份缩写
    ● calendar 模块提供5个类
        ● Calendar(firstweekday=0)	创建Calendar对象，默认周一为第一天
        ● TextCalendar(firstweekday=0)	生成纯文本日历对象
        ● HTMLCalendar(firstweekday=0)	生成HTML日志对象
        ● LocaleTextCalenda(firstweekday=0,locale=None)	语言环境名称
        ● LocaleHTMLCalendar(firstweekday=0,locale=None)	语言环境名称
     ● setfirstweekday(firstweekday) ：通过常量 MONDAY、TUESDAY、WEDNESDAY、THURSDAY、FRIDAY、SATURDAY、SUNDAY 设置星期；
                                            其中 0 表示星期一，以此类推6表示星期日；
    ● Calendar类实例相关方法
        ● cal.itermonthdates(year,month)	返回一个year年month月的日期的迭代器
        ● cal.iterweekdats()	返回为一星期的数字的迭代器
        ● cal.itermonthdays(year,month)	返回的日期为当月每一天的日期对应的天数，对于不在当月的日期，会显示0
        ● cal.itermonthdays2(year,month)	返回一个由日期和代表星期几的数字组成的元组
        ● cal.itermonthdays3(year,month)	返回一个由年月日组成的元组
        ● cal.itermonthdays4(year,month)	返回一个由年月日和星期几的数字组成的元组
        ● cal.monthdatescalendar(year,month)	返回一个由datetime.date对象组成的年月的周列表
        ● cal.monthdays2calendar(year,month)	返回一个由日期数字和周几的数字的二元元组
        ● cal.monthdayscalendar(year,month)	返回一个由七个日期数字的组成周列表
        ● cal.yeardatescalendar(year,width=3)	返回可以用来格式化的指定年月的数据列表
        ● cal.yeardays2calendar(year,width=3)	返回用来模式化的指定年月的数据。在这个月的日期为0，周列表由日期和星期数组成的元组
        ● cal.yeardayscalendar(year,width=3)	返回一个周列表是日期数字组成可以用来模式化的指定年月的数据
   ● TextCalendar类实例相关方法
        ● theyear指定年；themonth指定月  w:日期之间的宽度   l:指定每行日期之间的行数  c:月之间的宽度； m:将12个月分为m列
        ● tc.formatmonth(theyear,themonth,w=0,1=0)	以多行字符串来表示指定年月的日历   
        ● tc.prmonth(theyear,themonth,w=0,1=0)	格式化打印一个月的日历
        ● tc.formatyear(theyear,w=0,1=1,c=6,m=3)	返回一个m列的日历               
        ● tc.pryear(theyear,w=0,1=1,c=6,m=3)	格式化打印一整年的日历
   ●  HTMLCalendar类实例相关方法
        ● htl.formatmonth(theyear,themonth,withyear=True)	返回一个HTML表格的指定的年月日历
        ● htl.formatyear(theyear，width=3)	返回HTML指定年份的日历
        ● htl.formatyearpage(theyear,width=3,css='calendar.css',encoding=None)	
                             返回一个完整的HTML页面作为指定的年份日历calendar.HTMLCalendar类实例相关属性
   ● HTMLCalendar类实例相关属性
        ● htl.cssclasses	星期一到星期天的CSS class 列表
        ● htl.cssclass_noday	工作日的CSS类在上个月或下个月发生
        ● htl.cssclasses_weekday_head	用于标题行中工作日名称的css列表
        ● htl.cssclass_month_head	月份的CSS列表标题
        ● htl.cssclass_month	某个月的月历CSS类
        ● htl.cssclass_year	某个年的年历CSS类
        ● htl.cssclasses_year_head	年历的CSS列表标题
     ● firstweekday(): 返回当前每周起始日期值。默认情况下，首次载入calendar模块时返回0，即星期
     ● setfirstweekday(firstweekday) ：通过常量 MONDAY、TUESDAY、WEDNESDAY、THURSDAY、FRIDAY、SATURDAY 
                                                     和 SUNDAY 设置星期；其中 0 表示星期一，以此类推6表示星期日；
     ● isleap()  isleap(year)：判断是否是闰年，闰年为True，平年为False
     ● leapdays(y1, y2): 返回[y1,y2)年份之间的闰年数量;
     ● weekday(year, month, day)：获取指定日期为星期几
     ● monthrange(year, month)： 返回元组， 第一个值代表给定月份第一天的星期；第二个值代表给定月份有多少天；
     ● weekheader(n)：返回包含星期的英文缩写，n表示返回缩写的长度；
     ● monthcalendar(year, month): 返回表示一个月的日历的矩阵，每一行代表一周; 可以通过setfirstweekday() 改变默认值；
     ● prmonth(theyear, themonth, w=0, l=0): 打印一个月的日历 theyear : 指定年份 themonth：指定月份    
                                            w：日之间的间隔w个字符，默认0； l : 星期之间的行数，默认0； 
     ● prcal(year, w=0, l=0, c=6, m=3) : 打印一年的日历 year： 指定年份                w：日之间的间隔w个字符，默认0；
                                        l : 星期之间的行数，默认0；  c : 月之间的宽度；        m: 将12个月分为m列 
     ● day_name 返回星期列表
     ● month_name 返回月份列表
     4、总结
           ● 我们对calendar模块日历相关的方法的学习，calendar模块主要提供3个主要类Calendar、TextCalendar、HTMLCalendar。
           ●  我们可以更好地以字符串或者HTML形式打印出指定的日历
    -----------------------------------------------------------------------------------------------------------
    ++++                      数学计算 math (内置库)                                                       +++++
    -----------------------------------------------------------------------------------------------------------  
   ●  Python math 模块提供了许多对浮点数的数学运算函数。
        ● math 模块下的函数，返回值均为浮点数，除非另有明确说明。
        ● 如果你需要计算复数，请使用 cmath 模块中的同名函数。
        ● 要使用 math 函数必须先导入：import math
   ● math 模块常量
         常量      	    描述
        ● math.e	     返回欧拉数 (2.7182...)
        ● math.inf	     返回正无穷大浮点数
        ● math.nan	     返回一个浮点值 NaN (not a number)
        ● math.pi	     π 一般指圆周率。 圆周率 PI (3.1415...)
        ● math.tau	    数学常数 τ = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。
   ● math 模块方法
         方法	                描述
        ● math.acos(x)	    返回 x 的反余弦，结果范围在 0 到 pi 之间。
        ● math.acosh(x)	    返回 x 的反双曲余弦值。
        ● math.asin(x)	    返回 x 的反正弦值，结果范围在 -pi/2 到 pi/2 之间。
        ● math.asinh(x)	    返回 x 的反双曲正弦值。
        ● math.atan(x)	    返回 x 的反正切值，结果范围在 -pi/2 到 pi/2 之间。
        ● math.atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值，结果是在 -pi 和 pi 之间。
        ● math.atanh(x)	    返回 x 的反双曲正切值。
        ● math.ceil(x)	    将 x 向上舍入到最接近的整数
        ● math.comb(n, k)	    返回不重复且无顺序地从 n 项中选择 k 项的方式总数。
        ● math.copysign(x, y)	返回一个基于 x 的绝对值和 y 的符号的浮点数。
        ● math.cos()	        返回 x 弧度的余弦值。
        ● math.cosh(x)	    返回 x 的双曲余弦值。
        ● math.degrees(x) 	将角度 x 从弧度转换为度数。
        ● math.dist(p, q)	    返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。
        ● math.erf(x)	        返回一个数的误差函数
        ● math.erfc(x)	    返回 x 处的互补误差函数
        ● math.exp(x)	        返回 e 的 x 次幂，Ex， 其中 e = 2.718281... 是自然对数的基数。
        ● math.expm1()	    返回 Ex - 1， e 的 x 次幂，Ex，其中 e = 2.718281... 是自然对数的基数。这通常比 math.e ** x 或 pow(math.e, x) 更精确。
        ● math.fabs(x)	    返回 x 的绝对值。
        ● math.factorial(x)	返回 x 的阶乘。 如果 x 不是整数或为负数时则将引发 ValueError。
        ● math.floor()	    将数字向下舍入到最接近的整数
        ● math.fmod(x, y)	    返回 x/y 的余数
        ● math.frexp(x)	    以 (m, e) 对的形式返回 x 的尾数和指数 m 是一个浮点数 e是一个整数 好是 x == m * 2**e 如果x为零则返回 (0.0, 0)
                                                                                                          否则返回 0.5 <= abs(m) < 1 。
        ● math.fsum(iterable)	返回可迭代对象 (元组, 数组, 列表, 等)中的元素总和，是浮点值。
        ● math.gamma(x)	    返回 x 处的伽马函数值。
        ● math.gcd()	        返回给定的整数参数的最大公约数。
        ● math.hypot()	    返回欧几里得范数，sqrt(sum(x**2 for x in coordinates))。 这是从原点到坐标给定点的向量长度。
        ● math.isclose(a,b)	检查两个值是否彼此接近，若 a 和 b 的值比较接近则返回 True，否则返回 False。。
        ● math.isfinite(x)	判断 x 是否有限，如果 x 既不是无穷大也不是 NaN，则返回 True ，否则返回 False 。
        ● math.isinf(x)	    判断 x 是否是无穷大，如果 x 是正或负无穷大，则返回 True ，否则返回 False 。
        ● math.isnan()	    判断数字是否为 NaN，如果 x 是 NaN（不是数字），则返回 True ，否则返回 False 。
        ● math.isqrt()	    将平方根数向下舍入到最接近的整数
        ● math.ldexp(x, i)	返回 x * (2**i) 。 这基本上是函数 math.frexp() 的反函数。
        ● math.lgamma()	    返回伽玛函数在 x 绝对值的自然对数。
        ● math.log(x[, base])	使用一个参数，返回 x 的自然对数（底为 e ）。
        ● math.log10(x)	    返回 x 底为 10 的对数。
        ● math.log1p(x)	    返回 1+x 的自然对数（以 e 为底）。
        ● math.log2(x)	    返回 x 以 2 为底的对数
        ● math.perm(n, k=None)	返回不重复且有顺序地从 n 项中选择 k 项的方式总数。
        ● math.pow(x, y)	    将返回 x 的 y 次幂。
        ● math.prod(iterable)	计算可迭代对象中所有元素的积。
        ● math.radians(x)	    将角度 x 从度数转换为弧度。
        ● math.remainder(x, y)	返回 IEEE 754 风格的 x 除于 y 的余数。
        ● math.sin(x)	        返回 x 弧度的正弦值。
        ● math.sinh(x)	    返回 x 的双曲正弦值。
        ● math.sqrt(x)	    返回 x 的平方根。
        ● math.tan(x)	        返回 x 弧度的正切值。
        ● math.tanh(x)	    返回 x 的双曲正切值。
        ● math.trunc(x)	    返回 x 截断整数的部分，即返回整数部分，删除小数部分
    -----------------------------------------------------------------------------------------------------------
    ++++                             数据存储 shelve（自带标准库）                                  ************
    -----------------------------------------------------------------------------------------------------------  
    ● 在已有json和pickle的情况下，为什么用shelve？
        ● 使用json或者 pickle 持久化数据，能 dump 多次，但 load 的话只能取到最新的 dump，因为先前的数据已经被后面 dump 的数据覆盖掉了。
        ● 如果想要实现 dump 多次不被覆盖，可以使用 shelve 模块。
    ● shelve模块的特点
        ● shelve 是一个简单的数据存储方案，类似 key-value 数据库，可以很方便的保存 python 对象，其内部是通过 pickle 协议来实现数据序列化。
        ● shelve 只有一个 open() 函数，这个函数用于打开指定的文件（一个持久的字典），然后返回一个 shelf 对象。shelf 是一种持久的、类似字典的对象。
        ● shelve 模块可以看做是 pickle 模块的升级版，可以持久化所有 pickle 所支持的数据类型，而且 shelve 比 pickle 提供的
            操作方式更加简单、方便；
        ● 在 shelve 模块中，key 必须为字符串，而值可以是 python 所支持的数据类型。
        ● shelve 只提供给我们一个 open 方法，是用 key 来访问的，使用起来和字典类似。可以像字典一样使用get来获取数据等。
        ● shelve 模块其实用 anydbm 去创建DB并且管理持久化对象的。
        ● Shelve的主要特点包括：
            1)使用键值对存储数据，类似于字典。
            2)可以存储各种Python对象，包括列表、字典、自定义对象等。
            3)可以方便地将数据保存到磁盘，以及从磁盘中读取数据。
        ● Shelve通常用于需要将数据保存到文件以供以后使用的应用中，比如配置文件、小型数据库、缓存等。
        ● 要使用Shelve保存数据，首先需要创建一个Shelve文件。Shelve文件实际上是一个包含键值对的数据库文件，通常以.db、.shelf或.dat为扩展名。
    ● 导入模块：import shelve
     ● 方法:
       ● shelve.open(filename, flag=’c’, protocol=None, writeback=False):创建或打开一个shelve对象。shelve默认打开方式支持同时读写操作。
             1. filename是关联的文件路径。可选参数flag，默认为‘c’，如果数据文件不存在，就创建，允许读写；可以是: ‘r’: 只读；’w’: 可读写; 
                        ‘n’: 每次调用open()都重新创建一个空的文件，可读写。
             2. protocol：是序列化模式，默认值为None。具体还没有尝试过，从pickle的资料中查到以下信息【protocol的值可以是1或2，表示以二进制的形式序列化】
             3. writeback：默认为False。当设置为True以后，shelf将会将所有从DB中读取的对象存放到一个内存缓存。当我们close()打开的shelf的时候，
                           缓存中所有的对象会被重新写入DB。
                writeback方式有优点也有缺点。优点是减少了我们出错的概率，并且让对象的持久化对用户更加的透明了；但这种方式并不是所有的情况下都需要，
                         首先，使用writeback以后，shelf在open()的时候会增加额外的内存消耗，并且当DB在close()的时候会将缓存中的每一个对象都写入到DB，
                         这也会带来额外的等待时间。因为shelve没有办法知道缓存中哪些对象修改了，哪些对象没有修改，因此所有的对象都会被写入。
                  注意：为了保存增、删、改的内容，建议显示的标明writeback=True。
       ● shelve.close()同步并关闭shelve对象。注意：每次使用完毕，都必须确保shelve对象被安全关闭。同样可以使用with语句
                          db   = shelve.open('test_shelf.db')  #.创建一个对象，直接使用open函数即可
            示例代码：       with shelve.open('spam'，writeback=True) as db:    #.创建一个对象，直接使用open函数即可 使用with语句保证打开后 安全关闭
                           db['eggs'] = 'eggs'                #新建数据，已有数据的更新数据
                           del db['aggs']                     #删除数据 为了使Shelve支持数据的更新，在shelve.open()函数中传递了参数writeback=True。
    -----------------------------------------------------------------------------------------------------------
    ++++                          字符串模块  string(标准库)  improt string                             ++++++++
    -----------------------------------------------------------------------------------------------------------  
     Python字符串常用方法的列表及其简短描述。以下是每个方法及对应的描述：
        1. str.capitalize()                                 - 描述：把字符串的首字母大写。
        2. str.center(width)                                - 描述：将原字符串用空格填充成一个长度为width的字符串，原字符串居中。
        3. str.count(s)                                     - 描述：返回字符串s在str中出现的次数。
        4. str.decode(encoding='UTF-8', errors='strict')    - 描述：以指定编码格式解码字符串。
        5. str.encode(encoding='UTF-8', errors='strict')    - 描述：以指定编码格式编码字符串。
        6. str.endswith(s)           - 描述：判断字符串str是否以字符串s结尾。
        7. str.find(s)              - 描述：返回字符串s在字符串str中的位置索引，没有则返回-1。
        8. str.index(s)             - 描述：与find()方法一样，但是如果不存于str中则会抛出异常。
        9. str.isalnum()            - 描述：如果str至少有一个字符并且都是字母或数字则返回True, 否则返回False。
        10. str.isalpha()           - 描述：如果str至少有一个字符并且都是字母则返回True, 否则返回False。
        11. str.isdigit()           - 描述：如果str只包含数字则返回True, 否则返回False。
        12. str.islower()           - 描述：如果str存在区分大小写的字符，并且都是小写则返回True, 否则返回False。
        13. str.isspace()           - 描述：如果str中只包含空白，则返回True, 否则返回False。
        14. str.istitle()           - 描述：如果str是标题化的(单词首字母大写)则返回True, 否则返回False。
        15. str.isupper()           - 描述：如果str存在区分大小写的字符，并且都是大写则返回True, 否则返回False。
        16. str.ljust(width)        - 描述：返回一个原字符串左对齐的使用空格填充至长度width的新字符串。
        17.str.lower()              - 描述：转换str中所有大写字符为小写。
        18. str.lstrip()            - 描述：去掉str左边的不可见字符。
        19. str.partition(s)        - 描述：用s将str切分成三个值。
        20. str.replace(a, b)       - 描述：将字符串str中的a替换成b。
        21. str.rfind(s)            - 描述：类似于find()函数，不过是从右边开始查找。
        22. str.rindex(s)           - 描述：类似于index(), 不过是从右边开始。
        23. str.rjust(width)        - 描述：返回一个原字符串右对齐的使用空格填充至长度width的新字符串。
        24. str.rpartition(s)       - 描述：类似于partition()函数，不过是从右边开始查找。
        25. str.rstrip()            - 描述：去掉str右边的不可见字符。
        26. str.split(s)            - 描述：以s为分隔符切片str。
        27. str.splitlines()        - 描述：按照行分割，返回一个包含各行作为元素的列表。
        28.str.startswith(s)        - 描述：检查字符串str是否是以s开头，是则返回True, 否则返回False。
        29. str.strip()             - 描述：等于同时执行lstrip()和rstrip()。
        30. str.title()                         - 描述：返回“标题化”的str, 所有单词都是以大写开始，其余字母均为小写。
        31. str.upper()                         - 描述：返回str所有字符为大写的字符串。
        32. str.zfill(width)                    - 描述：返回长度为width的字符串，原字符串str右对齐，前面填充0。
    ● Python中的字符串常量及其含义的表格。具体如下：
        1. string.ascii_lowercase：  小写字母'a'到'z'
        2. string.ascii_uppercase：  大写字母'A'到'Z'
        3. string.ascii_letters：    所有ASCII的小写和大写字母
        4. string.digits：           数字0到9
        5. string.hexdigits：        十六进制数字（包括a-f和A-F）
        6. string.letters：          所有大小写英文字母
        7. string.lowercase：        小写字母'a'到'z'
        8. string.octdigits：        八进制数字0到7
        9. string.punctuation：      所有的标点符号
        10. string.printable：       可打印字符集，包括数字、字母、标点和空白符
        11. string.uppercase：       大写字母'A'到'Z'
        12.string.whitespace**：     空白字符，如'\t', '\n', ' ', '\r'
    -----------------------------------------------------------------------------------------------------------
    ++++                   高阶函数functools模块  import functools                                        +++++
    -----------------------------------------------------------------------------------------------------------  
   ● functools模块是Python的标准库的一部分，它是为高阶函数而实现的，用于增强函数功能
     ● 函数被定义为一段代码，它接受参数，充当输入，执行涉及这些输入的一些处理，并根据处理返回一个值（输出）。
     ● 当一个函数将另一个函数作为输入或返回另一个函数作为输出时，这些函数称为高阶函数。
     ● 如：map() 、reduce() 和 filter() 都是高阶函数。
     ●下是 functools 模块中包含的主要方法的详细说明：
        ● cached_property: 一个装饰器，用于将方法转换为只读属性，第一次访问时计算值并缓存。
        ● cmp_to_key: 用于在比较函数中将老式比较函数转换为关键字函数的工具。
        ● cache: 一个装饰器，提供了一个带有缓存的函数装饰器，用于缓存函数的结果以提高性能。
        ● lru_cache: 一个装饰器，提供了一个带有最近最少使用（LRU）缓存的函数装饰器，用于缓存函数的结果以提高性能。
        ● partial: 一个函数，用于部分应用一个函数的参数，并返回一个新的函数，使得可以在原函数的基础上预先设置一部分参数。
        ● partialmethod: 与 partial 类似，但专门用于部分应用类方法的参数。
        ● reduce: 一个函数，对序列中的元素进行累积运算，通常与二元函数结合使用。
        ● singledispatch: 一个装饰器，用于创建基于单个分派泛型函数的多分派泛型函数，根据不同的参数类型调用不同的函数实现。
        ● singledispatchmethod: 与 singledispatch 类似，但专门用于类方法。
        ● total_ordering: 一个类装饰器，可以根据一个类的一组方法（__eq__, __lt__, __le__, __gt__, __ge__, __ne__）自动生成所有比较运算。
        ● update_wrapper: 一个函数，用于更新一个函数对象的特性，例如 __doc__、__name__ 和 __module__，以便被包装函数更好地模拟原函数。
        ● wraps: 一个装饰器，用于将一个装饰器应用到一个函数上，并保留原函数的元数据。
    -----------------------------------------------------------------------------------------------------------
    ++++                             sys python解释器交互                                                ++++++
    -----------------------------------------------------------------------------------------------------------
     ********************************* sys模块  *********************************************************
    ● sys模块是与python解释器交互的一个接口。sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分
    ● 处理命令行参数
    ● 在解释器启动后, argv 列表包含了传递给脚本的所有参数, 列表的第一个元素为脚本自身的名称。
        ● sys.argv[0] 表示程序自身
        ● sys.argv[1] 表示程序的第一个参数
        ● sys.argv[2] 表示程序的第二个参数
        ● sys.exit(n) 退出程序，正常退出时exit(0)
        ● sys.version 获取Python解释程序的版本信息
        ● sys.platform 返回操作系统平台名称
        ● sys.stdin.readline()与input区别  1）sys.stdin.readline() 相当于input，区别在于input不会读入'\n'
                                           2）还有一个区别在于，input()里面可以直接传入文本，然后打印出来
        ● sys.stdout与print #标准输出  
              sys.stdout.write('hello' + '\n') 等价print('hello') 
                  #默认无法实现print方式的sep参数功能，所以需要手动在后面添加一个换行符
              sys.stdout.write(obj+'\n')中的obj只能是字符串
        ● Python中sys模块：该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数
        ● sys.argv #命令行参数List，第一个元素是程序本身路径
        ● sys.modules.keys() #返回所有已经导入的模块列表
        ● sys.exc_info() #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
        ● sys.exit(n) #程序，正常退出时exit(0)
        ● sys.hexversion #获取Python解释程序的版本值，16进制格式如：0x020403F0
        ● sys.version #获取Python解释程序的版本信息
        ● sys.maxint #最大的Int值
        ● sys.maxunicode #最大的Unicode值
        ● sys.modules #返回系统导入的模块字段，key是模块名，value是模块
        ● sys.path #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
        ● sys.platform #返回操作系统平台名称
        ● sys.stdout #标准输出
        ● sys.stdin #标准输入
        ● sys.stderr #错误输出
        ● sys.exc_clear() #用来清除当前线程所出现的当前的或最近的错误信息
        ● sys.exec_prefix #返回平台独立的python文件安装的位置
        ● sys.byteorder #本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
        ● sys.copyright #记录python版权相关的东西
        ● sys.api_version #解释器的C的API版本
        ● sys.version_info #获取Python解释器的版本信息
        ● sys.getwindowsversion #获取Windows的版本
        ● sys.getdefaultencoding #返回当前你所用的默认的字符编码格式
        ● sys.getfilesystemencoding #返回将Unicode文件名转换成系统文件名的编码的名字
        ● sys.setdefaultencoding(name) #用来设置当前默认的字符编码
        ● sys.builtin_module_names #Python解释器导入的模块列表
        ● sys.executable #Python解释程序路径
        ● sys.stdin.readline #从标准输入读一行，sys.stdout.write("a") 屏幕输出a
    -----------------------------------------------------------------------------------------------------------
    ++++                                Pillow （pil)  图像处理                                          ++++++
    -----------------------------------------------------------------------------------------------------------  
        ● Python Pillow 官方文档：https://pillow.readthedocs.io/en/latest/
        ● Pillow是PIL的一个分支，且与PIL完全兼容，并且在大多数情况下，Pillow可以直接代替PIL使用。Pillow提供了一系列强大
        ● 的图像处理功能，、 包括打开、操作、保存各种格式的图像文件，这使得它成为Python社区中最流行的图像处理库之一。
        ● Pillow 库提供了非常丰富的功能，主要有以下几点：
           ● Pillow 库能够很轻松的读取和保存各种格式的图片；
           ● Pillow 库提供了简洁易用的 API 接口，可以让您轻松地完成许多图像处理任务；
           ● Pillow 库能够配合 GUI（图形用户界面） 软件包 Tkinter 一起使用；
           ● Pillow 库中的 Image 对象能够与 NumPy ndarray 数组实现相互转换。
        ● 安装：pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
        ● 打开和保存图像
            ●使用 Image.open() 打开图像，使用 save() 保存图像。例如：
              im = Image.open("my_image.jpg")  # 打开图像
              im.save("my_image.png")  # 保存为 PNG 格式
        ● 调整图像大小
            ●使用 resize() 方法调整图像大小。例如：
                new_size = (200, 200)  # 新尺寸
                resized_im = im.resize(new_size)
                resized_im.save("my_image_resized.jpg")
        ● 旋转和翻转图像
            ●使用 rotate() 和 transpose() 方法旋转和翻转图像。例如：
                im_rotated = im.rotate(45)  # 旋转 45 度
                im_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)  # 水平翻转
                im_rotated.save("my_image_rotated.jpg")
                im_flipped.save("my_image_flipped.jpg")
        ● 裁剪图像
            ●使用 crop() 方法裁剪图像。例如：
                box = (100, 100, 400, 400)  # 裁剪区域
                region = im.crop(box)
                region.save("my_image_cropped.jpg")
        ● 颜色转换
            ●使用 convert() 方法转换图像颜色模式。例如：
                im_gray = im.convert("L")  # 转换为灰度图像
                im_gray.save("my_image_grayscale.jpg")
        ● 图像格式转换
            ●Pillow 支持多种图像格式之间的转换。例如，将 JPG 转换为 PNG：
                img = Image.open("input.jpg")
                img.save("output.png", "PNG")
        ● 缩略图生成
            ●使用 thumbnail() 方法生成缩略图。例如：
                size = (100, 100)  # 缩略图尺寸
                im.thumbnail(size)
                im.save("my_image_thumbnail.jpg")
    -----------------------------------------------------------------------------------------------------------
    ++++                                qdm 进度条模块                                                   ++++++
    -----------------------------------------------------------------------------------------------------------
     ***************************   tqdm 进度条模块   **************************
     ●tqdm 是一个用于显示进度条的 Python 库，适用于循环、文件处理、数据加载等需要长时间运行的任务。以下是其基本用法和常见场景：
        ●1. 安装‌
            pip install tqdm
        ●2. 基本用法‌
           ● 在循环中显示进度条
                from tqdm import tqdm
                import time
                # 在循环外包裹 tqdm()
                for i in tqdm(range(100)):
                    time.sleep(0.1)  # 模拟耗时操作
           ● 手动控制进度条更新
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(0.1)
                        pbar.update(10)  # 每次更新进度条 10%
        ● 高级用法‌
            ● 自定义进度条格式
                for i in tqdm(
                    range(100),
                    desc="Processing",      # 进度条前的描述
                    bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",  # 自定义格式
                    colour="green"          # 颜色（需要终端支持）
                ):
                    time.sleep(0.1)
            ● 嵌套进度条（多任务）
                from tqdm import tqdm
                outer = tqdm(range(3), desc="Outer")
                for i in outer:
                    inner = tqdm(range(5), desc="Inner", leave=False)  # leave=False 表示完成后隐藏
                    for j in inner:
                        time.sleep(0.1)
                    inner.close()
            ● 文件读取进度
                from tqdm import tqdm
                with open("large_file.txt", "r") as f:
                    for line in tqdm(f, desc="Reading file"):
                        pass  # 处理每一行
            ●与 pandas 结合‌
                import pandas as pd
                from tqdm import tqdm
                # 启用 pandas 的进度条支持
                tqdm.pandas()
                # 在 apply 方法中使用
                df = pd.DataFrame({"data": range(1000)})
    -----------------------------------------------------------------------------------------------------------
    ++++       Beautiful Soup 4 (bs4)     用于从 HTML/XML 文档中提取数据                                  ++++++     
    -----------------------------------------------------------------------------------------------------------  
    ● Beautiful Soup 4 是一个 Python 库，用于从 HTML/XML 文档中提取数据。它通过构建文档树结构，提供简单直观的接口遍历和搜索标签
        常用于网页爬虫和数据抓取。
    ● 核心用途： 解析网页内容与 requests 或 urllib 等库配合，将网页 HTML 转换为可操作的对象树。
    ● 定位与提取数据：通过标签名、属性、层级关系等快速定位目标数据（如文本、链接、图片等）。
    ● 核心功能：
              功能	                  说明
            ●自动修复文档	             容错性强，即使 HTML 标签不完整也能解析（如缺失闭合标签）。
            ●多种解析器支持	            支持 lxml, html.parser, html5lib 等解析器（推荐 lxml）。
            ●灵活的搜索方法  	        find(), find_all(), select() 支持标签、属性、CSS 选择器等筛选。
            ●文档树遍历    	          通过 .parent, .children, .next_sibling 等遍历节点关系。
        ● 典型应用场景
            ●抓取网页中的 标题、正文、表格数据。
            ●提取 链接（<a> 标签） 或 图片资源（<img> 标签）。
            ●处理动态生成的 HTML（如 JavaScript 渲染后的页面，需配合 selenium
    ● 安装与导入
            pip install beautifulsoup4  # 安装
            pip install lxml            # 推荐安装（更快解析器
            from bs4 import BeautifulSoup
   ● 创建解析对象
            # 从字符串
            soup = BeautifulSoup(html_content, 'html.parser')
            # 从文件
            with open("example.html", "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, 'html.parser')
            # 从网页
            import requests
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')  # 推荐 lxml
    ● 查找标签
        ● find() / find_all()
            # 查找第一个 <div>
            div = soup.find('div')
            # 查找所有 class 为 'item' 的 <li>
            items = soup.find_all('li', class_='item')
            # 按属性过滤（如 href 包含 "example" 的 <a>）
            links = soup.find_all('a', href=lambda x: x and 'example' in x)
        ● CSS 选择器 select()‌
            # 查找所有 <div> 下的 <p>
            paragraphs = soup.select('div p')
            # 查找 id 为 'header' 的标签
            header = soup.select_one('#header')
            # 属性选择器（href 以 "https" 开头的 <a>）
            secure_links = soup.select('a[href^="https"]')
    ● 数据提取
        ● 获取标签内容
            text = tag.get_text()  # 提取标签内所有文本
            text = tag.string      # 提取标签内纯文本（无子标签时）
        ● 获取属性值
            href = tag['href']           # 直接访问属性
            href = tag.get('href', '')   # 安全获取（避免 KeyError）
    ● 文档树遍历
        1. 层级关系
            parent = tag.parent          # 父节点
            children = tag.contents      # 直接子节点列表
            children = tag.children      # 子节点生成器（迭代用）
        2. 兄弟节点
            next_sibling = tag.next_sibling         # 下一个兄弟节点
            previous_sibling = tag.previous_sibling # 上一个兄弟节点
    ● 实用场景
        ● 提取所有链接
            links = [a['href'] for a in soup.find_all('a') if a.has_attr('href')]
        ● 提取图片资源
            images = [img['src'] for img in soup.find_all('img') if img.has_attr('src')]
        ● 处理动态属性
            # 提取包含 data-id 属性的标签
            data_items = soup.find_all(attrs={"data-id": True})
    ● 注意事项
        ● 解析器选择：优先用 lxml（速度快），复杂页面用 html5lib（容错强）
        ● 异常处理‌：访问属性前用 .get() 避免 KeyError
        ● 性能优化‌：避免在循环中重复调用 soup.find()
    -----------------------------------------------------------------------------------------------------------
    ++++                                opencc 简繁体转换
    -----------------------------------------------------------------------------------------------------------  
    ● OpenCC（Open Chinese Convert）是一个开源的中文简繁转换工具，支持：
        简体中文 ↔ 繁体中文
        台湾繁体 ↔ 香港繁体
        自定义词汇转换
    ● 安装
        ● pip install opencc  # Python 包
    ● 核心功能
        ●配置文件
            配置文件	说明
            s2t.json	简体 → 繁体
            t2s.json	繁体 → 简体
            s2tw.json	简体 → 台湾繁体
            tw2s.json	台湾繁体 → 简体
            s2hk.json	简体 → 香港繁体
            hk2s.json	香港繁体 → 简体
            t2tw.json	繁体 → 台湾繁体
            tw2t.json	台湾繁体 → 繁体
            t2hk.json	繁体 → 香港繁体
            hk2t.json	香港繁体 → 繁体
       ●Python 使用‌
            import opencc
            # 创建转换器
            converter = opencc.OpenCC('s2t.json')  # 简体 → 繁体
            # 转换文本
            text = "简体中文"
            result = converter.convert(text)
            print(result)  # 输出：簡體中文
    -----------------------------------------------------------------------------------------------------------
    ++++                            typing  typing_extensions 类型注释                                    +++++
    -----------------------------------------------------------------------------------------------------------  
   ● typing 模块是 Python 3.5 引入的标准库，用于支持 类型提示 (Type Hints)，旨在提升代码的可读性、可维护性和类型安全性。
        ● pythom 3.8  用typing_extensions (扩展库)
       ● 核心功能
        ● 类型注解 为变量、函数参数和返回值添加类型信息，例如：
            def greet(name: str) -> str:
                return f"Hello, {name}"
        ●支持基本类型（如 int、str）和复杂类型（如 List、Dict）。
       ● 类型别名‌
        ● 创建自定义类型别名，简化复杂类型声明：
            from typing import List, Tuple  # python3.8  from typing_extensions ipport List,Tuple
            Coordinates = List[Tuple[float, float]]
            ●这提高了代码的可读性和可维护性1。
       ● 联合类型 (Union)
        ● 允许变量或参数接受多种类型：
            from typing import Union
            def parse(value: Union[int, str]) -> int:
                return int(value)
           ● 适用于处理多种可能的输入类型1。
       ● 可选类型 (Optional)
        ●表示变量或参数可以是特定类型或 None：
            from typing import Optional
            def find_user(id: int) -> Optional[str]:
                return "Alice" if id == 1 else None
          ●常用于处理可能缺失的值。
      ●高级特性
     -----------------------------------------------------------------------------------------------------------
    ++++                                 m3u8 模块
    -----------------------------------------------------------------------------------------------------------
     -----------------------------------------------------------------------------------------------------------
    ++++                				aiohttp 模块
    -----------------------------------------------------------------------------------------------------------
     -----------------------------------------------------------------------------------------------------------
    ++++          						multidict 模块 
    -----------------------------------------------------------------------------------------------------------
     -----------------------------------------------------------------------------------------------------------
    ++++       							fake_useragent 
    -----------------------------------------------------------------------------------------------------------
       -----------------------------------------------------------------------------------------------------------
    ++++       							 lxml（更快解析器 
    -----------------------------------------------------------------------------------------------------------
       -----------------------------------------------------------------------------------------------------------
    ++++       							utils
    -----------------------------------------------------------------------------------------------------------
       -----------------------------------------------------------------------------------------------------------
    ++++       							pystray
    -----------------------------------------------------------------------------------------------------------
       -----------------------------------------------------------------------------------------------------------
    ++++       							pycryptodome
    -----------------------------------------------------------------------------------------------------------
     -----------------------------------------------------------------------------------------------------------
    ++++           jupyter     maturin  MinGW   Rust   没安装成功
    -----------------------------------------------------------------------------------------------------------  
          +++++++++++++++++++++++++++代码片段测试 maturin 缺少依赖无法安装++++++++++++++++++++++++++
        ● jupyter ： pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple
             ● 和：pip install maturin -i https://pypi.tuna.tsinghua.edu.cn/simple
             ● 装 Visual C++ Redistributable VC_redist.x64.exe
             ● 需安装win7编译器  rust-1.75.0-x86_64-pc-windows-msvc.msi  添加环境变量path路径
             ● 下载兼容 Windows 7 的 rustup-init​​：
             # 从社区维护的镜像下载
             ● https://static.rust-lang.org/rustup/archive/1.24.3/x86_64-pc-windows-msvc/rustup-init.exe
          ​​ ● 安装 Rust 1.70.0（最后一个完全兼容 Win7 的版本）
             ● rustup-init.exe -y --default-toolchain 1.70.0
             ● 测试安装是否成功：运行：rustc --version  cargo --version
             ● MinGW-W64 GCC 8.5.0 (UCRT runtime)  https://github.com/brechtsanders/winlibs_mingw/releases?page=20
               vscode 安装jupyter 扩展 
             ● 使用：  测试的代码片段前后 输入：#%%
================================================================================================================================
