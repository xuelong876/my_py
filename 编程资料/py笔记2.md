
"""
---使用对象组织数据
  --在程序中可以做的设计，生产，填写 表格的组织形式的
  1，在程序中设计表格 ，我们称之为: 设计类（clss）
     clss student:
          name = None  # 记录学生姓名
  2，在程序中打印生产表格，我们称之为：创建对象
      stu_1 = student()
      sty_2 = student()  #基于类创建对象
  3，在程序中填写表格，我们称之为：对象属性赋值
      stu_1.name = "周杰伦"  #为学生1对象赋予名称属性值
      stu_2.name = "林俊杰"  #为学生2对象赋予名称属性值
  4,类里面 方法（函数）的使用（调用）：
       stu.方法（参数）   
---  类只是程序内的“设计图纸”，需要基于图纸生产实体（对象），才能正常工作，这种套路，称之为“面向对象编程”
       面向对象编程就是，使用对象进行编程，设计一个类，并且基于类创建对象，并使用对象来完成具体的工作。
      类的使用语法： class 类名称：   #class 是关键字，表示要定义类了
                     类的属性    #类的属性，即定义类中的变量（成员变量）
                     类的行为    #类的行为，即定义在类中的函数（成员方法）  类内部的函数称之为 方法
          --成员方法和定义函数基本一致，但有细微区别
            def 方法名（self,形参1，形参2，形参n) #self必写，它表示类对象自身的意思，当类对象调用方法时，self会自动被py传入
                方法体                          #在方法内部，想要访问类的成员变量，必须使用self     
 -创建对象语法：  对象 = 类名称（）
   --- import winsound    # windows 声音模块
       winsound.Beep(2000，3000)   # 2000赫兹 声音响 3000毫秒 3秒
   ---魔术方法    
     构造方法: __init__() 的方法可以实现，1在创建类对象（构造类）的时候会自动执行。2 将传入参数自动传递给_init_方法使用
     字符串方法__str__()  直接转换类对象为字符串时，输出内存地址，可以通过_str_方法，控制类转换为字符串的行为
                         如果调用类对象（如print(类对象) 返回  __str__() 方法下的内容  如：return f"{name}"
       __repr__()  直接打印list 是由list调用的对象输出信息的方法,它会默认调用__repr__()【面向程序员】的方法，
                  而不是__str__()【面向用户】的方法，当一个对象放在列表里面时，要重写__repr__()而不是__str__()
       > <符合比较 __lt__() 直接对两个类对象进行比较会报错，这是因为没有对类赋予比较功能，
                               def __it __(self,other):  #方法名 传入参数：other,另一个对象 
                                    return  self.age < other.ae #返回True 或False   内容自定义
                                    print (stu1<stu2)   #结果 True  传入参数 stu1.age=11 stu2.age =13
                                    print (stu1>stu2))  #结果False
       >= <=符合比较 __le__() 
       == 符合笔记 __eq__()
    -- 封装： 将现实世界事物在类中描述为属性和方法，即为封装； 私有成员 是不公开对使用者开放的
    -定义私有成员：在私有成员变量和方法 前面加两个下划线即可 __  私有方法无法直接被类对象使用 私有变量无法赋值，也无法获取值
      --私有成员可以被其他成员使用   也就是在类中提供仅供内部使用的属性和方法，而不对外开放（类对象无法使用）
    --继承：在原有的类上新增内容
     -语法：1 单继承： class 类名（父类名）      #父类名 被继承的类
           2 多继承： class 类名（父类1，父类2，父类n)   父类中有同名的属性或方法， 左侧父类优先（先继承的优先级高于后继承的）
     pass:关键字表示无内容，空的意思，占位语法，用来保证函数（方法）或定义类的完整性
    --复写：子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以复写。即：在子类中重新定义同名的属性或方法即可
          -在子类中对已经复写的（同名）父类成员调用：1-成员属性：父类名.成员名 - 成员方法： 父类名.成员方法（self）
                             第二种调用方法：    2-成员属性：super().成员名          - 成员方法super().成员方法
    ---类型注解： 
     -基本语法：变量：类型    如 var_1: int =10                    对象类型注解 class Student:
                              var_2：flost= 3.14                                  pass
            var_4:str = "it"  var_3:bool =True                              stu:student = Student()                         
     -基础容器类注解： my_list:list =[]   tuple(元组)  set(集合) dict(字典) str (字符串)
     -容器类型详细注解：my_list: list[int] =[1,2]  my_tuple:tuple[int,str,bool] = (11,"it",True) 元组需要元素类型都标注
        -python 3.8 及以下版本 不支持 下标类型定义
     --注释中类型注解：代码 # type: 类型;  如 val_1 = random  #tuye:int  或 my_list =[1,2] #type:list[int]
     --函数（方法）的类型注解：
      -形参及返回值注解：  def 函数方法名（形参名：类型，形参名：类型...) -> 返回值类型：  
     --Union类型：使用Union[类型，类型，...类型] 可以定义联合类型（多种类型）注解  多选一
              例如：my_list:list[Union[str,int]] = [1,2,"it","heima"]  #列表元素是有可能是str 也有可能是int 二选一
    ---多态: 即完成某个行为时，使用不同的对象会得到不同的状态  同样的行为（函数），传入不同的对象，得到不同的结果
        class Animal:
            def speak(self):                         def make_noise(animal:Animal):
               pass                                         animal.speak()
        class Dog(Animal):                           dog = Dog()
            def speak(self):                         cat = Cat()
               print("汪汪汪") 
        class Cat(Animal):                           make_moise(dog)    #输出：汪汪汪
            def speak(self):                         make_noise(cat)    #输出：喵喵喵
               print("喵喵喵")                  
     - 函数（方法）形参声明接收父类对象，实际传入父类的子类对象进行工作，即以父类做定义说明，以子类做实际工作用以获得同一行为不用状态
     -抽象类（接口） 上述父类Animal的speak 的方法是空实现 ，这种设计的含义是：1，父类用来确定有哪些方法                   
                    2：具体的方法实现，有子类自行决定 ；这种写法就叫抽象类（也可以称之为接口）
                    抽象类:含有抽象方法的类称为抽象类 ；抽象方法：方法体是空实现的（pass)称之为抽象方法
         多态中：抽象的父类设计（设计标准）  具体的子类实现（实现标准）         
"""
""" SQC语言:  cmd 下访问数据库：mysql -uroot -p
    -MySQL 数据库使用：在CMD 输入mysql -uroot -p 回车 输入密码 123456 进入数据库管理
      -- show databases;   查看有哪些数据库
      -- use 数据库名 ;       使用某个数据库
      -- show tables ;       查看数据库内有哪些表
      -- exit               退出My SQL 的命令行环境
    ---图形化数据库管理DBeaver :
    --SQL全称 Structured Query Language 结构化查询语言，用于访问和处理数据库的标准计算机语言；
     --数据定义：DDL(Data Definition Language)   库的创建删除，表的创建删除
     --数据操作：DML(Data Manipulation Language)  新增数据，删除数据，修改数据
     --数据控制：DCL(Data Control Language)   新增用户，删除用户，密码修改，权限管理等
     --数据查寻：DQL(Data Query Language)   基于需求查询和计算数据
     -特点：大小写不敏感，语句以分号结束； 不分行（可以多行写）
     -单行注释：-- 注释内容（--后面一点有一个空格） # 注释内容（可以不加空格） 
     -多行注释：/* z注释内容 */
     --库操作：
     - show databases: 查看数据库
     -USE 数据库名；   使用数据库
     - create database 数据库名 [charse utf8]; 创建数据库 中括号是可选项，可以不写 注意：写代码时不写中括号
     - DROP DATABASE 数据库名; 删除数据库
     - SELECT DATABASE();   查看当前使用的数据库
     --表操作：
      - show tables;            # 查看有哪些表，注意：需要先选择数据库     [  可选项，不写括号]
      --drop table 表名称；           # 删除表
      --drop table if extsts 表名称； # 删除表
      -- create tavle 表名称（列名称 列类型，列名称 列类型，...);   # 创建表 
      --列类型有 1 int  2 float 3 timestamp #(时间戳类型) 4 varchar(长度）#文本，长度为数字，做最大长度限制 5 date  #(时间类型)
     --DML 数据操作
       -插入:  insert into 表[（列1，列2,...,列n)] values(值1，值2，...,值n)[,(值1，值2，...,值n),...] #[] 里面是可选项
                     写代码是不要写[] ,输入字符串是 要用 '单引号' 不支持双引号
       -删除：delete from 表名称 [where 条件判断]；  #条件判断：列 操作符 值  操作符： = < > <= >= != 等等
       -更新：update 表名称 set 列=值 [where 条件判断] #条件判断如上
     --DQL 查询
       -select 字段列表|* from 表 [where 条件判断]    #从表中显示某些列展示 where 条件判断 如上
        - select id,name from student;   #查询表student 的id和name 两个列
        - select * from student:  #查询全部
       --分组集合查询 GROUP BY (group by)
        -基础语法：select 字段|聚合函数 from 表 [where 条件] group by 列： #以列分组 聚合函数(字段) 计算结果
           -聚合函数:1 sum(列) #求和    2 avg(列) #求平均值     3 min(列) #求最小值   4 MAX(列) #求最大值 
                    5 connt(列|*)  #求数量
         例如：select gunder, avg(age) from student group by gender;
           以 表（student) 中的列gender(性别) 分组 后 显示列gender 列age(年龄求平均数（avg）计算后的列） 
            group by中出现那个列，那个列才能出现在select 的非聚合中 ，聚合函数可以写多个
        ---分页
         -结果排序; 关键字 order by  写在查询后面
           select 列|聚合函数|* from 表 order by 列 [asc|desc];    #asc 小到大 （默认） desc从大到小
         --结果分页限制 关键字 limit  查询后面加 limit n[,m];    #不写m 只显示n 行； n,m 前n行跳过, 显示 n后面的 m行
      --总结 ：where, group , order by .limit 均可按需求省略， select ,from 是必须写的
              执行顺序 from -> where -> group by和聚合函数 -> select -> order by -> limit
"""
"""   pytho & MySQL
      from pymysql import connect #导入数据库包
        #创建数据库连接
        conn = connect(
            host='localhost',  #连接主机默认127.O.O.1
            port = 3306,        #端口
            user = 'root',
            passwd='123456'
            autocommit = True )  #设置自动提交修改 ，如不设置需手动输入代码： 链接对象.commit（)   来提交修改
      cursor = conn.cursor() #获取游标对象
      conn.select_db("test")   #先选择数据库 test 
      #使用游标对象，执行sql 语句
      cursor.execute("select" * from student")
        例如  cursor.execute("CRRATE TABLE test_pymysql(id INT,info VARCHAR(255))")  
      #获取查询结果
       results: tuple = cursor.fetchall()  #获取返回值对象 类型注解为元组tuple
       for r in results:
            print(r)
      conn,close() #关闭数据库连接
      总结：
       --获取链接对象: 1 from pymysql import Connect(有的是Connecion）  导包
                     2  Connect (主机，端口，账号，密码)  即可得到链接对象
                     3  链接对象.close()  关闭和MySQL链接数据库的
       -- 执行SQL查询：1 通过链接对象调用 cursor()方法，得到游标对象
                     2  游标对象.select_db("数据库") #选择数据库
                     3  游标对象.execute() 执行SQL 语句
                     4  游标对象.fetchall() 得到全部查询结果封装入元组内
       --commit 提交
         pyMySQL 在执行数据插入后其他数据更改的SQL语句是，默认是需要提交更改的，即需要通过代码，确认这种更改行为
        - 通过链接对象.commit() 即可确认此行为。 
          也可以在构建链接对象时 设置自动 commit 的属性 和密码，用户 在一起  格式 ：autocoomit = True
"""
"""  --PySpark  大数据 分布式计算    安装pyspark 需安装JAVA 环境  写入文件需配置 Hadoop 依赖
                在python中使用os 模块配置：os.environ['HADOOP_HOME'] ="D:\pycharm\hadoop-3.0.0"
                 winut.exe 放入bin目录内  hadoop.dll放到C:/windows/system32 文件夹内
     --rdd分区设置:方式1，Sparkconf 对象设置属性全局并行度为1   (全局设置）
                          conf.set("spark.default.parallelism","1")  #修改 RDD分区为一个  
                  方法2 ，创建RDD的时候设置（parallelize方法传入numSlices 参数为1） （局部设置）
                          rdd1 = sc.parallelize([2,3]),numSlices =1)     
       PySpark 的执行环境入口对象是：类SparkContext的类对象
     --创建pyspark 链接环境代码：
            from pyspark import SparkConf,SparkContext  #导包
            import  os  #配置
            os.environ['PYSPARK_PYTHON'] ="D:/python/python.exe" #配置python解释器路径 环境变量
               #创建SparkConf类对象
            conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") #链式调用 返回值是同一个对象可以用链式写法
                #上面代码等同于以下三行代码
                # conf = SparkConf()
                # conf = conf.setMaster("local[*]")
                # conf = conf.setAppName("test_spark_app")
              #基于SparkConf类对象创建SparkContext类对象
            sc = SparkContext(conf=conf)
              #打印pyspark版本
            print(sc.versino)
              #停止SparkContext对象的运行（停止pyspark程序）
            sc.stop()
      输出--将RDD的结果输出为Python对象的各类方法
               collect：将RDD内容转换为list
               reduce：对RDD内容进行自定义聚合
               take：取出RDD的前N个元素组成list返回
               count：统计RDD元素个数返回
     -RDD对象 ：RDD 全程称为弹性分布式数据集（Resilient Distriluted Dtatsets),PySpark 针对数据的处理，都是以RDD对象作为载体，
              即; 1 数据存储在RDD内 2各类数据的计算方法，返回值依旧是RDD对象
     --数据输入： pyspark 支持通过SparkContext 对象的parallelize 成员方法，将 list, tuple, set, dict, str ,转换为RDD对象
               注意： 1字符串会拆分为一个个字符存入RDD对象， 2 字典仅有KEY 会被存入RDD对象   
      --打印数据  print(rdd1.collect()) #打印RDD1  
      --读取数据  rdd = sc.parallelize(数据容器对象)
      --读取文件 rdd =sc.textFILE(文件路径)  
     --数据计算：
  计算 - map 方法（算子）：将RDD 的数据一条条处理（处理的逻辑基于map 算子中接收的处理 函数），返回新的RDD
       -语法： rdd.map(func)  #func: f:(T) -> u   #f: 表示这是一个函数 #（T)-> U 表示的是方法的定义：
              # -> u 表示返回值    #() 表示传入参数 （T)表示传入1个参数，（）表示没有传入参数 #T和U 是泛型的代称，在这里表示任意类型
              #(T) -> u 总结起来的意思是:这是一个方法，这个方法接受一个参数传入，传入参数不限，返回一个返回值，返回值类型不限
              #（A）-> A  意思同上： 不同的是返回值和传入值参数类型一致  
            -例1： def func(data):      #定义一个函数  里面的DATA 就是代表是sc 获取的一个个数据的合集 它会一个个处理
                    return  data*10  #返回值  每个数乘以10 后返回
                  rdd1 = rdd.map(func)  #使用map 算子对方程 func 计算 结果赋值给rddq
            -例2    rdd1 = rdd.map(lambda x: x*10).map(lambda x:x+5)   #链式写法 返回值*10+5
        -总结：1 接受一个处理函数，可以用lambda 表达式快速编写 对RDD内的元素逐个处理，并返回新的RDD
              2 链式调用， 对于返回值是新RDD的算子，可以通过链式调用的方式多次调用算子  
  解嵌套   --flatMapa   算子功能: 同map 算子用法一样，只是计算后数据解嵌套
               语法：rdd.flatMapa(func) 
  分组   --reduceByKey 算子功能 ：  接收一个处理函数 对valve 进行两两处理（如相加）   分组功能
 Vilue聚合    用法 rdd.reduceByKey(func)
                 #func: (v,v) -> v  接收两个传入参数（类型一致），返回一个返回值，类型和传入参数要求一致
              功能：针对KV型RDD. 自动安装key 分组，然后按照你提供的聚合逻辑，完成组内数据（value） 的聚合操作
                    KV 型： 即二元元组组， 元组里面有两个元素 第一个为KEY  第二个为value
           例如：rdd = sc.parallelizerdd = sc.parallelize([('男',88),('男',99),('女',55),('女',99),('女',77)])  #KV型数据
                result = rdd.reduceByKey(lambda a,b: a+b)                   #以成key分组   value累加为value 
                print(result.collect())   #结果[('男', 187), ('女', 231)]
                #在reduceByKiy 中接收的函数，只负责聚合，不理会分组 ,分组是自动by key 分组的   
    过滤---Filter 算子功能：过滤想要的数据进行保留   
          语法：rsd.filter(func)     #func 为方程
          #func:(T)  -> bool 传入一个任意参数进来，返回值必需是 Ture or  False  返回的Ture 的数据保留，False 的数据丢弃
   去重 --distinct 算子功能：对RD数据进行去重 ，返回新想RDD  
           语法：rdd.distinct()  无需传参
   排序  --sortBy  算子功能：对rdd 数据进行排序，基于你指定的依据排序
           语法：rdd.sortBy(func,ascending=False, numPartitinons=1)
            #func:(T) -> U:告知按照rdd中的那个数据进行排序，不然lambda x: x[1] 表示按照rdd中第二个元素排序
            # ascending Ture为升序 False 降序
            #numPartitions: 用多少分区排序
  写入文本  ---saveAsTextFile 算子功能： 将RDD中的内容写到文本文件中，支持本地写出，hdfs 等文件系统
            语法：rdd.saveAsTestFile("文件路径“)
      
"""
"""python 高阶    返回/回调函数
   ---闭包：在函数嵌套的前提下，内部函数使用了外部的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称之为闭包
    例如:    def outer(logo):                   #定义外部函数
                def inner(msg):  #定义函数 inner 变量 = logo
 --声明修改外部变量   nonlocal logo                   # 用关键字nonlaca 修饰外部函数的变量才能在函数内部修改它
                    print(f"<{logo}>{msg}<{logo}>")
            return inner                         #返回内部函数运行结果
            fn1 = outer("黑马程序员")      #fn1 是一个函数
            fn1("大家好")       #result: <黑马程序员>大家好<黑马程序员>
            fn1("我在这里")     #result:  <黑马程序员>我在这里<黑马程序员>
   --总结：优点，使用闭包可以让我们得到：  1 无需定义全局变量即可实现通过函数，持续的访问、修改某个值
                                      2 闭包使用的变量的作用域在函数内 难以被错误的调用修改
          缺点：由于内部函数持续引用外部函数的值，所以会导致一部分内存空间不被释放，一直占用内存
   ---装饰器：1 也是一种闭包，在不破坏目标函数原有代码和功能的前期下，为目标函数增加新功能
             2 使用创建一个闭包函数，在闭包函数内部调用目标函数
            def outer(func):     #定义闭包外部函数，函数的形参为 函数（引用）
                def inner():
                print("开始睡眠了")
                func()               #引用外部函数
                print("睡眠结束")
            return inner             #返回内部函数执行结果
   增加功能- @outer      #把sleep() 传入outer(sleep) 函数运行   可以理解为 调用sleep 函数实际运行 outer(sleep)函数
            def sleep():            #睡眠函数
                import  random      #随机数函数
                import time         #时间函数
                print("睡眠中.........")
                time.sleep(random.randint(1,5))   #程序等待 1~5秒
            sleep() #运行睡眠函数 相当于：# sep1 = outer(sleep) # sep1()  结果 
                    #运行结果三行1 开始睡眠了 2 睡梦..... 3 睡眠结束
   --设计模式：是一种编程套路，可以极大的方便程序的开发， 最经典，常见的设计模式，就是面向对象了，还有很多设计模式
    -单例，工厂模式，建造者，责任链，状态，备忘录，解释器，访问者，中介，模版，代理模板，等的  设计模式
    -单例模式（Singleton Patterm)是一种常见的软件设计模式，该模式的注意目的是确保某一个类只能有一个实例存在
      在整个系统中某个例只能出现一个实例，单例对象就能派上用车
      --定义：保证一个类只能有一个实例，并提供一个访问它的全局访问点
      --适用场景，当一个类只能有一个实例，而客户可以从一个众所周知的访问点访问它时；
      单例的实现模式：
       示例：  新建py文件  ：  str_tools_py.py  （模块）
              写入代码  class StrTools:             #传进类对象
                              pass
                       str_tool = StrTools()      #创建单例对象
         再新建一个py文件写入以下代码：
                    from str_tools_py import str_tool  #导入单例对象
                    s1 = str_tool                      #单例对象S1
                    s2 = str_tool                      #单例对象S2
                    print(id(s1))         #打印S1 内存地址
                    print(id(s2))         #打印s2 内存地址    单例对象S1 和S2 内存地址相同
     总结：单例模式就是一个类，只获取其唯一实例对象，持续使用它， 节省内存，节省创建对象的开销
  ---工厂模式：大量创建一个类的实例的时候，可以使用工厂模式
      使用工厂类的get_person() 方法创建具体的类对象的优点：1 大批量创建对象的时候有统一的入口，易于代码维护
      2 当发生修改，仅修改工厂类的创建方法即可，3符合现实世界的模式，即由工厂来制作产品（对象）
       示例：class Person:            #父类 （入口）
                pass
            class  Worker(Person):   #子类1
                pass
            class  Studen(Person):  #子类2
                pass
            class Teacher(Person):  #子类3
                pass
            class Factory:                  #工厂类
                def get_person(self,p_type):  #工厂类的get_person()方法
                    if p_type == "w":         
                        return Worker()     
                    elif p_type=="s":
                        return Studen
                    else:
                        return Teacher
            factory = Factory()
            worker = factory.get_person("w")    #worker = Worker()
            stu = factory.get_person("s")
            teacher = factory.get_person("t")
  ----多线程 进程：  
      --进程：就是一个程序，运行在系统之上，那么便称之为一个运行进程，并分配进程ID方便系统管理        
      --线程：线程是归属于进程的，一个进程可以开多个线程，执行不同的工作，是进程的实际工作最小单位     
      -- 进程间的内存是隔离的，即不同的进程拥有各自的内存空间， 线程之间是内存共享，
      --并行执行的意思指的是同一时间做不同的事
  ---多线程并行执行  threadong 模块
  --语法： import threading  #导入线程模块
          thread_obj = threading.Thread([glorp[,target[,name[args[,kargs ]]]]])
            -group: 暂时无用，
            -target: 执行的目标任务名      函数名 不含括号
            -args: 以元组的方式给执行任务传参
            -kwargs: 以字典的方式给执行任务传参
            -name: 线程名，一般不用设置
            thread_obj.start()  #启动线程，让线程开始工作 构建多少个类对象就是有多少个线程
       示例：import threading
            def sing(msg):
                while True:
                    print(msg)
            def dance(msg):
                while True:
                    print(msg)
            #创建两个线程对象 唱歌和跳舞 以元组和字典的方式 传入参数
            sing_obj = threading.Thread(target=sing,args=("我要唱歌哈哈哈",))           #以元组形式传参，一个参数也有写逗号
            dance_obj = threading.Thread(target=dance,kwargs={"msg":"我在跳舞啦啦啦"}) #以字典形式传参 变量为KEY 
            #启动线程
            sing_obj.start()
            dance_obj.start()
  ----网络编程
           Socket (简称 套接字) 是进程之间通信的一个工具， 进程直接想要网络通信就需要socket 
           socke 服务端(server)：等待其它进程的连接，可接受发来的消息，可以回复消息
           socke 客户端(client)：主动连接服务端，可以发消息，可以接收信息
     --socket 服务端(server)编程  
          1.创建socket对象    import socket
                            socket_server = socket.socket()
          2. 绑定socket_sever到指定ip 和地址  ：   socker_server.bind((host,port))  #参数为二元元组
          3.服务端开始监听端口  socket_server.listen(backlog) #baklog 为int 表示允许的连接数量，超出会等待，不填会设置一个合理值
          4.接收客户端连接，获取连接对象 conn,address =socket.server.accept()
                                    print(f"接收到客户端连接，连接来自：{address}")
                                    #accept() 方法是阻塞方法，如果没有连接，会卡在当前这一行不想下执行代码
                                    #accept 返回的是二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素
          5.客户端连接后通过recv方法，接受客户端发送的消息
            while True:
            data = conn.recv(1024).decode("utf-8) #recv返回值是字节数组（Bytes) 可以通过decode使用utf-8 解码为字符串
                                                  #recv(buffsize)  buffsize 为缓冲区大小一般1024
            if data == "exit"      #判定客户端发来的特殊标记如 exit 来退出无限循环
                break
            print("接收到发来的数据：",data)  #通过while True 无限循环来持续和客户端进行数据交互
          6.通过conn(客户端当次链接对象)，调用send 方法可以回复消息
            conn.send("你好啊".encode("utf-8"))  #在此上面5的代码省略未写  通encode 把字符串转为字节数组（Bytes）
          7.conn（客户端当次连接对象） 和socker.server 对象调用close 方法关闭连接
    ---socket 客户端（client)编程：
          1.创建socket 对象   import socket
                             socket_client = socket.socket()
          2.连接到服务器       socket_client.connect(("localhost",8888))   #配置IP 和端口号prot
          3.发送消息          while True:  #无限循环
                                 msg = input("请输入您要发送的消息")
                                 if msg == 'exit':   # 此处单引号，判断信息是exit 退出循环
                                    break
                                 socket_client.send(mag.encode("utf-8"))
          4.接收返回消息 recv_data = socket_client.recv(1024)  #1024 是缓存大小  recv方法是阻塞式的
                        print("服务端回复消息为：",recv_data.decode("utf-8")) #接收消息通过utf-8 解码为字符串
          5.关闭连接 ： socket_client.colse()
     总结：服务端 需创建连接对象，绑定bind ip 客户端不需要 始终使用socket 对象  连接connect ip       
"""
""" ---正则表达式（Regular Expression)   re模块（match ; search; findall)
     匹配开头  --- re.match(匹配规则，被匹配字符串)  #从被匹配字符串的开头匹配，匹配成功返回匹配对象（包含匹配信息），匹配不成功发回空
     多个匹配                                    #如果开头没有匹配对象 直接返回空，后面的也不配
        示例：   import re
                s ="python itheima python itheima python itheima"     #字符串1
                result = re.match("python",s)
                print(result)               # <re.Match object; span=(0, 6), match='python'>
                print(result.span())        #(0, 6)  
                print(result.group())       #python
                s2 ="mypython itheima python itheima python itheima"  #字符串2
                result2 = re.match("python",s2)
                print(result2)                      #返回None   
       匹配第一个-- re.search(匹配规则，被匹配字符串)  #搜索整个字符串，从前往后找到第一个后，就停止，不会继续向后  对于正则收敛模式
       示例：    import re
                s = "itpython itheima python"
                resulrt1 = re.search("python",s)
                print(resulrt1)                  #<re.Match object; span=(2, 8), match='python'>
                print(resulrt1.span())            # (2, 8)
                print(resulrt1.group())         #python  
       匹配全部 ---re.findall(匹配规则，被匹配字符串)  # 匹配整个字符串，找出全部匹配项 返回的是一个列表list  对应正则贪婪模式
        示例：   import  re
                s = "mypython itheima python itheima ipython itheima"
                result = re.findall("python",s)
                print(result)                 #['python', 'python', 'python']    
    ---  在pytho 中    在前面加  r  如 r'\d' 声明 '\d' 是普通字符 （字符类型）
                                | 或的意思 匹配左右任意一个表达式
                                （）将括号中的字符作为一个分组
       示例：import re
            s = "itheima1 @@python2 !!666 ##itccasst3"
            result = re.findall(r'\d', s)  #匹配全部数字  r' 表示字符串中转义字符无效，就是普通字符
            print(result)  #['1', '2', '6', '6', '6', '3']
        示例2：匹配邮箱 只能qq 163.gmail
            import re
            r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'  #邮箱地址匹配 含\w \. @ -  qq|163|gmail
            s = 'a.b.c.e.f.g@qq.com.a.z.c.d.e'
            print(re.findall(r,s))  #[('a.b.c.e.f.g@qq.com.a.z.c.d.e', '.g', 'qq', '.e')]
   --递归：即方法（函数）自己调用自己的一种特殊写法
          语法：det foun()
                 if ...:
                    fuon()   #调用自己
                 return ...
          示例: import os   #系统模块
                def test_os():
                    print(os.listdir("D:/temp"))    #查看指定 目录下文件列
                    print(os.path.isdir("D:/temp/a"))  #判断指定路径是否为文件夹  返回Ture
                    print(os.path.exists("D:/temp"))   #判断指定路径是否存在   返回Ture
                def get_files_recursion_from_dir(path):
                    """
                    从指定文件夹中使用递归的方法，获取全部的文件列表
                    :param path: 被判断的文件夹
                    :return: 包含全部的文件，如果目录不存在或者无文件就返回一个空的list
                    """
                    file_liat = []                  #新建文件列表
                    if os.path.exists(path):         #判断指定路径是否存在
                        for f in os.listdir(path):         #取出文件列表
                            new_pach = path+'/'+ f"{f}"        #增加新文件路径
                            if os.path.isdir(new_pach):              #判断是否为文件夹
                                file_liat += get_files_recursion_from_dir(new_pach)  #文件列表接收下一次返回的列表 并和它合并
                                 #函数返回值需要 用一个变量接收，这里用文件列表变量接收并和下一个返回列表合并列表
                            else:
                                file_liat.append(new_pach)    #文件列表写入新增 文件路径
                    else:
                        print(f"指定的目录{path}不存在")
                        return []                        #返回空列表
                    return file_liat              #函数返回值 文件列表
          总结：递归需要注意：1.有退出的条件，否则容易编程无限递归   2.返回值的传递，确保从最内层，层层传递到最外层
          #TODO: 总结：1.递归函数需要 结束循环条件：本例结束条件： 目录下没有文件夹 就结束循环
          #TODO: 总结：2.递归函数返回值的传送；本例传送条件： 文件列表 = 文件列表 + 下一个路径下文件列表 结果是全部文件列表
"""