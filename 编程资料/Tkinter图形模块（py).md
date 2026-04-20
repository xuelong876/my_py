    --------------------------------------------------------------------------------------------------------------------
    +++                                   TKinter  gui图形界面                                                      ++++
    --------------------------------------------------------------------------------------------------------------------

    ● Tkinter（TK接口） 编程  gui 图形界面  在命令行中运行 python -m tkinter 可显示一个tk 窗口 查看tk版本
        ●Tkinter是使用 python 进行窗口视窗设计的模块。Tkinter模块("Tk 接口")是Python的标准Tk GUI工具包的接口。
        ●作为 python 特定的GUI界面，是一个图像的窗口，tkinter是python 自带的，可以编辑的GUI界面，我们可以用GUI 实现很多直观的功能
        ●而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。
        ●注意：Python3.x 版本使用的库名为 tkinter,即首写字母 T 为小写。
    ● Tk()：创建应用程序主窗口    Frame()：创建控件容器，可依附在窗口中        TopLevel()：创建弹出式窗口
    ● tkinter的函数列表：
        Tk()：创建一个主窗口对象。
        mainloop()：启动Tk事件循环。
        quit()：退出Tk事件循环。
        title()：设置窗口标题。
        geometry()：设置窗口大小和位置。
        resizable()：设置窗口是否可以调整大小。
        iconbitmap()：设置窗口图标。
        protocol()：指定窗口关闭时的处理方式。
        configure()：配置窗口的属性。
        destroy()：销毁窗口对象。
        Frame()：创建一个框架对象。
        Label()：创建一个标签对象。
        Button()：创建一个按钮对象。
        Entry()：创建一个文本框对象。
        Text()：创建一个文本框对象，支持多行文本。
        Radiobutton()：创建一个单选按钮对象。
        Checkbutton()：创建一个复选框对象。
        Listbox()：创建一个列表框对象。
        Scrollbar()：创建一个滚动条对象。
        Menu()：创建一个菜单对象。
        MenuBar()：创建一个菜单栏对象。
        Canvas()：创建一个画布对象。
        Messagebox()：显示一个消息框。
        askquestion()：显示一个询问框，返回True或False。
        askyesno()：显示一个询问框，返回True或False。
        askokcancel()：显示一个询问框，返回True或False。
        askretrycancel()：显示一个询问框，返回True或False。
        filedialog()：显示文件对话框。
        colorchooser()：显示颜色选择对话框。
        fontchooser()：显示字体选择对话框。
        messagebox.showerror()：显示一个错误消息框。
        messagebox.showwarning()：显示一个警告消息框。
        messagebox.showinfo()：显示一个信息消息框。
        messagebox.askquestion()：显示一个询问消息框，返回True或False。
        messagebox.askyesno()：显示一个询问消息框，返回True或False。
        messagebox.askokcancel()：显示一个询问消息框，返回True或False。
        messagebox.askretrycancel()：显示一个询问消息框，返回True或False。
  ● 提供Tk支持的其他模块包括：
        tkinter.scrolledtext       内置纵向滚动条的文本组件。
        tkinter.colorchooser        让用户选择颜色的对话框。
        tkinter.commondialog        在此处列出的其他模块中定义的对话框的基类。
        tkinter.filedialog           允许用户指定文件的通用对话框，用于打开或保存文件。
        tkinter.font               帮助操作字体的工具。
        tkinter.messagebox        访问标准的 Tk 对话框。
        tkinter.simpledialog      基础对话框和便捷功能。
        tkinter.dnd为            tkinter 提供拖放支持。这是实验性功能，当被 Tk DND 取代时应被废弃。
        turtle                  Tk 窗口中的海龟绘图库。
  ● 流程：  
    1、导入 Tkinter 模块  import tkinter  #创建一个GUI程序
    2、创建控件
    3、指定这个控件的 master， 即这个控件属于哪一个
    4、告诉 GM(geometry manager) 有一个控件产生了。
            import tkinter
            top = tkinter.Tk()   #  创建TK(根窗口)对象 TK是图形界面接口 窗口都是基于这个函数（方法）
            top.mainloop()   # 进入消息循环
            #  示例2 
            from tkinter import * 
            root = Tk()  # 创建窗口对象 创建一个TK()实例
                   #root.withdraw()  # 将Tkinter.Tk()实例隐藏
            root.g
            li     = ['C','python','php','html','SQL','java']
            movie  = ['CSS','jQuery','Bootstrap']
            listb  = Listbox(root)          #  创建两个列表组件
            listb2 = Listbox(root)
            for item in li:                 # 第一个小部件插入数据
                listb.insert(0,item)
            for item in movie:              # 第二个小部件插入数据
                listb2.insert(0,item)
            listb.pack()                    # 将小部件放置到主窗口中
            listb2.pack()
            root.mainloop()                 # 进入消息循环
            root.destroy()                   #退出窗口
            root.update()        #更新窗口
  ● Toplevel（顶层窗口）组件类似于 Frame 组件，但 Toplevel 组件是一个独立的顶层窗口，这种窗口通常拥有标题栏、边框等部件。
       ● 语法：top = tk.Toplevel(root)
    __________________________________________________________________________________________________________________
    ++++                                         15种Tkinter的部件                                                ++++
    ------------------------------------------------------------------------------------------------------------------
  ● Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。
  ● 目前有15种Tkinter的部件。我们提出这些部件以及一个简短的介绍，在下面的表:
        ● Button按钮控件；在程序中显示按钮。
              ●  Button(父窗口，text="按钮名称“，command = "函数”,winch=宽度，height= 高度)  注意 命令函数不写括号
                      # 部件宽，高 在显示文本时 单位是一个字符 ，图片时 单位是像素
              ●如： Button(root, width=40, height=10,textvariable=字符串,command = 命令)
                    Button.pak() #添加按钮 用pak(）方式加入按钮
        ● Canvas画布控件；显示图形元素如线条或文本 绘制图形和图表，创建图形编辑器，并实现各种自定义的小部件
              ● Canvas       组件支持对象
                arc         （弧形、弦或扇形）
                bitmap      （内建的位图文件或 XBM 格式的文件）
                image       （BitmapImage 或 PhotoImage 的实例对象）
                line        （线）
                oval（       圆或椭圆形）
                polygon     （多边形）
                rectangle   （矩形）
                text        （文本）
                window      （组件）
              ● 方法：● create_xxx() 的方法（xxx 表示对象类型，例如线段 line，矩形 rectangle，文本 text 等）：
                     ● create_text(position, **options) 指定的位置（x, y）创建一个文本对象-- 创建成功后返回该文本对象的 ID
        ● Checkbutton多选框控件；用于在程序中提供多项选择框  组件被用于作为二选一的按钮（通常为选择“开”或“关”的状态）
              ● 但是处理“多选一”的问题，还是交给 Radiobutton 和 Listbox 组件来实现吧
              ● indicatoron 该选项会影响到按钮的样式，设置为 False，则点击后该按钮变成 "sunken"（凹陷）raised"（凸起
              ● offvalue 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0
              ● onvalue 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0
              ● variable将 Checkbutton 跟一个 Tkinter 变量关联  切换的过程是完全自动的
                                            当按钮按下时，该变量在 onvalue 和 offvalue 之间切换
                      text:文字  textvariable #变量   command:指定于该按钮相关联的函数或方法
              ●方法：● deselect()-- 取消 Checkbutton 组件的选中状态，也就是设置 variable 为 offvalue。
                     ● invoke()调用 Checkbutton 中 command 选项指定的函数或方法，并返回函数的返回值 state(状态)"disabled"是（不可用）
                     ● select()-- 将 Checkbutton 组件设置为选中状态，也就是设置 variable 为 onvalue。
                     ● toggle()-- 切换 Checkbutton 组件的状态（选中 -> 未选中 / 未选中 -> 选中）。
        ●Entry输入控件；用于显示简单的文本内容
             ● extvariable:  指定一个与输入框的内容相关联的 Tkinter 变量（通常是 StringVar） 
             ● show:指定文本框内容显示为字符，值随意，满足字符即可。如密码可以将值设为 show="*"
             ● state:分为只读和可写，值为：normal/disabled,默认为 state=NORMAL, 文框状态，
             ● xscrollcommand 设置水平方向滚动条，一般在用户输入的文本框内容宽度大于文本框显示的宽度时使用
             ● 方法：● delete ( first, last=None ) 删除文本框里直接位置值 只有一个参数时 删除该位置内容
                     ● delete(0, "end")  #删除全部输入控件文本  从0到最后
                     ● insert ( index, s )   #向文本框中插入值，index：插入位置，s：插入值
                     ● select_clear()   ：清空文本框
                   	 ● select_from ( index ) 设置光标的位置，通过索引值 index 来设置
                   	 ● select_to ( index )选中指定索引与光标之间的值
                     ● xview ( index )该方法在文本框链接到水平滚动条上很有用   设置第几行滚动
                     ● xview_scroll ( number, what )用于水平滚动文本框。 what 参数可以是 UNITS（units单位）, 按字符宽度滚动，
                              或者可以是 PAGES（pages页）, 按文本框组件块滚动。 number 参数，正数为由左到右滚动，负数为由右到左滚动。
                     ● e1 = Entry(master, textvariable=v, textvariable="focusout", validatecommand=test)
        ●Frame框架控件；在屏幕上显示一个矩形区域，多用来作为组件容器 所谓容器组件，就是可以收纳其它组件，可以做其它组件的父组件的组件
            ● width:框架宽度 ，height :框架高度，bg:背景色；fg ：前景色：bd:边框（默认2）
                     ● Frame(父组件, 参数….)
        ● Label标签控件；可以显示文本和位图
                     ● Label（标签）组件用于在屏幕上显示文本或图像。Label 组件仅能显示单一字体的文本，但文本可以跨越多行。
                               另外，还可以为其中的个别字符加上下划线（例如用于表示键盘快捷键）。
        ●Listbox列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
             ● yscrollcommand：为 Listbox 组件添加一条水平滚动条 将此选项与 Scrollbar 组件相关联即可
             ● yscrollcommand：为 Listbox 组件添加一条垂直滚动条   yscrollcommand =Scrollbar.set
             ●方法：● get(first, last=None)-- 返回一个元组，包含参数 first 到 last 范围内（包含 first 和 last）的所有选项的文本
                    ● insert(index, *elements) -- 添加一个或多个项目到 Listbox 中，insert("end") 添加新选项到末尾
                    ● delete(first, last=None)删除参数 first 到 last 范围内（包含 first 和 last）的所有选项
                    ● bbox(index)#返回给定索引号对应的选项的边框
                                 #返回值是一个以像素为单位的 4 元祖表示边框：(xoffset, yoffset, width, height)
                                 #xoffset 和 yoffset 表示距离左上角的偏移位置
                                 #返回的 width 是文本的实际宽度（像素为单位）
                                 # 如果指向的选项是不可见的，那么返回值是 None
                    ● size()-- 返回 Listbox 组件中选项的数量
                    ● xview(*args) 该方法用于在水平方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项
                       如Scollbar 组件config( command = Listbox.xview),
                           ● 如果第一个参数是 "moveto"，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端
                           ● 如果第一个参数是 "scroll"，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 "units" 或 
                               "pages"），例如：xview("scroll", 3, "pages")表示向右滚动三行
                    ● yview(*args) 该方法用于在垂直方向上滚动 Listbox 组件的内容
                         listbox =Listbox(root,listvariable = var,width =10,height = 3,fg="red")
                                    #listvariable = var  绑定列表变量
        ● Menubutton菜单按钮控件，用于显示菜单项。
            ● Menubutton 组件是一个与 Menu 组件相关联的按钮，它可以放在窗口中的任意位置，并且在被按下时弹出下拉菜单。
                    menubutton = Menubutton(root,text="菜单按钮",)  #菜单按钮对象
                    filemenu = Menu(menubutton, tearoff=False) #显示菜单 父容器为菜单按钮对象  绑定
        ● Menu菜单控件；显示菜单栏,下拉菜单和弹出菜单
                    add_cascade(**options) #添加一个父菜单
                    add_command(**options) #添加一个普通的命令菜单
                    add_radiobutton(**options) #添加一个单选按钮的菜单项
                    add_separator(**options) #添加一条分割线
              ● 示例： 需要先创建一个菜单实例，然后使用 add() 方法将命令和其它子菜单添加进去：
                        menubar = tk.Menu(root)    #创建菜单对象
                        menubar.add_command(label = "Quit", command = root.quit) #添加菜单
                        root.config(menu = menubar)   #显示菜单
                      ● 如果添加子菜单：
                        fili_menu = tk.Menu(menubar,tearoff =False) #子菜单对象（实例）
                        file_menu = (label = ""保存"，command=callback)  #添加 文件下拉菜单 保存
                        menubar.add_cascade(label= "文件",menu = flie_nemu) #父菜单为“文件” 下拉菜单方法fili_nemu
        ● Message消息控件；
             ● Label 组件的变体，用于显示多行文本消息。Message 组件能够自动换行，并调整文本的尺寸使其适应给定的尺寸。
        ● Radiobutton单选按钮控件；显示一个单选的按钮状态
             ● anchor控制文本（或图像）在 Radiobutton 中显示的位置ewsn 代表东西南北
                   "n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位
             ● bitmap指定显示到 Radiobutton 上的位图 如果指定了 image 选项，则该选项被忽略
             ● image指定 Radiobutton 显示的图片
             ● indicatoron该选项会影响到按钮的样式，如果设置为 False，则点击后该按钮变成 "sunken"（凹陷），再次点（凸起）
             ● justify定义如何对齐多行文本"left"，"right" 或 "center"文本的位置取决于 anchor 选项
             ● tsxt : 文本         textvariable:变量  如果变量被修改，Radiobutton 的文本会自动更新
             ● value： 标志该单选按钮的值 在同一组中的所有按钮应该拥有各不相同的值
                     通过将该值与 variable 选项的值对比，即可判断用户选中了哪个按钮
             ● variable：与 Radiobutton 组件关联的变量  同一组中的所有按钮的 variable 选项应该都指向同一个变量
                    通过将该变量与 value 选项的值对比，即可判断用户选中了哪个按钮
             ● command指定于该按钮相关联的函数或方法 当按钮被按下时由 Tkinter 自动调用对应的函数或方法
             ● compound1. 控制 Radiobutton 中文本和图像的混合模式2. 默认情况下，如果有指定位图或图片，则不显示文本
                ● 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）
                ● 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边
                                   （如 "bottom"，则图像在文本的下方）      5. 默认值是 NONE
             ●方法：● deselect()  -- 取消该按钮的选中状态。
                    ● flash() -- 刷新 Radiobutton 组件，该方法将重绘 Radiobutton 组件若干次（在"active" 和 "normal" 状态间切换）。
                            -- 该方法在调试的时候很有用，也可以使用此方法提醒用户激活了该按钮。
                    ● invoke() -- 调用 Radiobutton 中 command 选项指定的函数或方法，并返回函数的返回值。
                             -- 如果 Radiobutton 的 state(状态)"disabled"是 （不可用）或没有指定 command 选项，则该方法无效。
                    ● select()-- 将 Radiobutton 组件设置为选中状态。
        ● Scale（刻度）组件看起来像是一个带数据的 Scrollbar（滚动条）组件，但事实上它们是不同的两个东东。
            ● Scale 组件允许用于通过滑动滑块来选择一个范围内的数字。你可以控制该组件的最大值、最小值，以及分辨率。
            ● 当你希望用户输入某个范围内的一个数值，使用 Scale 组件可以很好的代替 Entry 组件
            ● 但由于 from 本身是 Python 的关键字，所以为了区分需要在后边紧跟一个下划线：from_
            ● from:  设置滑块最顶（左）端的位置 (默认值0)    to:  设置滑块最底（右）端的位置（默认值100）
            ● length：设置滑块长度（默认30像素） resolution：步长 分辨率 精度（默认0.1）
            ● tickinterval：设置显示的刻度，如果设置一个值，那么就会按照该值的倍数显示刻度（默认不显示）
            ● orient：设置该 Scale 组件是水平放置（"horizontal"）还是垂直放置（"vertical"默认）
            ● label:  文本标签（默认不显示） width 宽度(默认15)
            ● command：1.指定一个函数，每当滑块发生改变的时候都会自动调用该函数
                       2.该函数有一个唯一的参数，就是最新的滑块位置
                       3.如果滑块快速地移动，函数可能无法获得每一个位置，但一定会获得滑块停下时的最终位置
            ● 方法：coords(value=None)：获得当前滑块的位置对应 Scale 组件左上角的相对坐标如果设置 value 参数，则返回当滑块所在该位置时的相对坐标
                ● get()：获得当前滑块的位置  会尽可能地返回一个整型值，否则返回一个浮点型值
                ● identify(x, y)：-- 返回一个字符串表示指定位置下（如果有的话）的 Scale 部件
                ● set(value)：-- 设置 Scale 组件的值（滑块的位置）
                ● 返回值可以是："slider"（滑块），"trough1"（左侧或上侧的凹槽），"trough2"（右侧或下侧的凹槽）或 ""（啥都没有）
                ● scale.config(label= "测试",length=350,orient =HORIZONTAL,from_=5,to=95,resolution=0.01,tickinterval= 15)
        ● Scrollbar滚动条控件，当内容超过可视化区域时使用，如列表框。.
            ● command:● 当滚动条更新时回调的函数,   ● 通常的是指定对应组件的 xview() 或 yview() 方法
                      ● jump :默认值是 False，滚动条的任何一丝变动都会即刻调用 command 选项指定的回调函数 设置为 True 则当用户松开鼠标才调用
                      ● orient：指定绘制 "horizontal"（水平滚动条）还是 "vertical"（垂直滚动条：默认值）
            ● 方法：● delta(deltax, deltay)--#给定一个鼠标移动的范围 deltax 和 deltay（像素为单位，deltax 表示水平移动量，deltay 表示垂直移动量），
                                    #然后该方法返回一个浮点类型的值（范围 -1.0 ~ 1.0）通常在鼠标绑定上使用，用于确定当用户拖拽鼠标时滑块的如何移动
                    ● fraction(x, y)-- 给定一个像素坐标 (x, y)，该方法返回最接近给定坐标的滚动条位置（范围 0.0 ~ 1.0）
                    ● get()-- 返回当前滑块的位置 (a, b)
                    ● set(*args) 设置滚动条位置
            Text	文本控件；用于显示多行文本
                    Text.insert("行.列","字符""）  #在几行几列的地方插入字符
                    Text.delete("行.列","行.列")    #删除第一个行列到第二人行列的字符 一个参数时只删除这个位置字符
        ● Toplevel顶级容器控件；用来提供一个单独的对话框，和Frame比较类似  Toplevel 组件和 Tk（根窗口）是一个级别的
            ● Toplevel 组件通常用在显示额外的窗口、对话框和其他弹出窗口上。
        ● Spinbox输入控件；与Entry类似，但是可以指定输入范围值常用于在限定数字中选取的情况下代替普通的 Entry 组件 
            ● values:例如 values= ("小新", "风间", "正男", "妮妮", "阿呆") 则允许用户在这 5个字符串中选择
                通过 from_ 和 to 选项设置范围
            ● validate :是否启用验证 
            ● vcmd(validatecommand)：1. 该选项指定一个验证函数，用于验证输入框内容是否合法 返回Ture 后False
            ● textvariable:指定一个与输入框的内容相关联的 Tkinter 变量（通常是 StringVar） 
            ● command:1. 指定一个函数，当用户点击调节箭头的时候将自动调用该函数 用户输入时不触发
            ● format：设置选择数值的样式（from_ 和 to 指定范围，用户自行输入的不算）
                ● 例如 format='%10.4f' 表示显示的数值占 10 位，小数点后保留 4 位
            ● increment 选项设置每次点击调节箭头递增（递减）的精度
            ● 方法：● insert(index, text)  ：将text内容 插入到index 位置
                   ● delete(first, last=None),删除 包含first 和last 的内容
                   ● get()  :   返回spinbox 当前的值
                   ● index(index):-- 返回与 index 参数相应的选项的序号（例如 e.index("end")）
                   ● scan_mark(x):-- 使用这种方式来实现输入框内容的滚动
                               ●  -- 需要将鼠标按下事件绑定到 scan_mark(x) 方法（x 是鼠标当前的水平位置），
                               ●  然后再将 <motion> 事件绑定到 scan_dragto(x) 方法（x 是鼠标当前的水平位置），
                               ●  就可以实现输入框在当前位置和 sacn_mack(x) 指定位置之间的水平滚动
                   ● bbox(index)-- 返回一个 4 元组（x1, y1, x2, y2）用于描述输入框中 index 参数指定的字符所在的矩形范围
        ● PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
            ● 组件会为每一个子组件生成一个独立地窗格，用户可以自由调整窗格的大小
        ● LabelFrame是一个简单的容器控件。常用于复杂的窗口布局。
            ● LabelFrame 会在其子组件的周围绘制一个边框以及一个标题。
        ● MessageBox用于显示你应用程序的d对话框。from tkinter.messagebox import *
            ● askquestion("title","消息内容"，)   #显示一个对话框 自定义标题 和消息内容
   ● 标准属性：标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。
      ● 属性           描述
        Dimension	  控件大小；
        Color	      控件颜色；
        Font	      控件字体；
        Anchor	      锚点；
        Relief	      控件样式；
        Bitmap	      位图；
        Cursor	      光标；
    __________________________________________________________________________________________________________________
    ++++                                        tkinter 主窗口                                                    ++++
    ------------------------------------------------------------------------------------------------------------------
  ● tkinter 主窗口
     ● 位置和大小
        ● root.geometry("宽 x 高 +X +Y")  +X:距屏幕左边距离：-x:j距屏幕右边距离：+y:距屏幕上边距离：-y:距离屏幕下面距离
        ● root.minsize(宽，高)           #设置窗口最小值
        ● root.maxsize(宽，高)            #设置窗口最大值
        ● root.resizable(0, 0)  # 窗口大小固定
     ● 窗口标题：root.titel("标题”)
     ● 设置窗口背景颜色: 窗口对象.config(bg='black')     
     ● 几何管理：Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，以下是Tkinter公开的几何管理类：包、网格、位置
           ● 几何方法	   描述
             pack()	       包装；
             grid()	       网格；
             place()	   位置；
    ● Label 组件的属性说明及示例
       ● 使用语法 ● widget = Label( master, parameter=value, ... )
              # master："组件控件的父容器  parameter："组件的参数  value：参数对应的值 各参数之间以逗号分隔。
       ● 参数说明：
           ● text	"组件文字，可以在"组件上添加文字
           ● relief	"组件边框样式，设置控件3D效果，  relief = SUNKEN
                   可选的有：FLAT（平坦）、SUNKEN（凹陷）、RAISED（凸起）、GROOVE（凹槽）、RIDGE（脊状）。 
           ● bg	"组件文字背景颜色，dg='背景颜色'
           ● fg	"组件文字前景色，fg='前景颜色'
           ● bd	"组件文字边框宽度，bd=‘边框宽度’。边框宽度显示需要配合边框样式才能凸显。
           ● font	"组件文字字体设置，font=('字体', 字号, "样式")    
             ● 示例：import tkinter.font as tk
                         ft = tk.Font(family=' ', size=40,weight='',slant='',underline='',overstrike='') 
                 ● 字体：family 为字体类型，如family='Times'（新罗马字体）,family=' 微软雅黑'等
                 ● Courier  (a monospaced “typewriter” font) 单频“打字机”字型
                 ●  Times     (a serifed “newspaper” font) 有锯齿状的“报纸”字型
                 ● Helvetica (a sans-serif “European” font) 无衬线“欧洲”字体
                 ● 字号：size =20
                 ● 样式：weight = "bold" 加粗
                    ● bold(粗体) 默认值为normal(正常粗细)
                    ● italic(斜体) 默认值为roman(正常直立)
                    ● underline(下划线) 默认值为false
                    ● overstrike(删除线)) 默认值为false
                    ● justify	"组件文字对齐方式，可选项包括LEFT, RIGHT, CENTER
                    ● underline	下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，第两个字符带下划线，以此类推
                    ● wraplength	按钮达到限制的屏幕单元后换行显示
                    ● height	字体高度，height='高度'。和relief结合使用才会凸显效果。
                    ● width	字体宽度，width='宽度'。和relief结合使用才会凸显效果。
                    ● image	"组件插入图片，插入的图片必须有PhotImage转换格式后才能插入，并且转换的图片格式必须是.gif格式
    __________________________________________________________________________________________________________________
    ++++         tkinter   pack/grid/place窗口部件三种放置方式  pack()包装；  grid()网格； place()位置；
    ------------------------------------------------------------------------------------------------------------------
    ● grid布局方法及参数
      ● 语法：grid( 参数….. ) grid 是方格, 所以所有的内容会被放在这些规律的方格中。
       参数：
         ●  row ：组件定位表格的行,
        　●  column： 组件定位表格的列     表格的行，列都是从0开始的，
        　 ● ipadx/ipady： 填充表格框，让表格框在X/Y方向上变胖 （内边距）
        　 ● padx/pady： 决定组件跟邻近表格线或窗体边界的距离  （外边距）
             ● padx(左,右)   pady(上，下)
        　●  rowspan： 组件跨多少列表格框，默认1个组件占用1行1列
        　●  columnspan ：组件跨多少行表格框，默认1个组件占用1行1列
        　●  sticky ：当表格框大小组件的大小，组件默认居中显示，那这个表格框周围的空白部分，如何分配，这就由sticky来决定。具体规定如下：
        　　　  默认组件在表格框中是居中对齐显示的，但通过sticky可以设定N/S/W/E 即上/下/左/右 对齐，N/S/W/E 也可以组件使用，如：
        　●　 sticky=N+S 拉高组件，让组件上下填充到表格框的顶端和底端。
        　●  sticky=N+S+E 拉高组件，让组件上下填充到表格框的顶端和底端，同时，让组件靠右对齐。
        　●  sticky=N+W+W+E 拉高并拉长组件，让组件填充满一个表格框。
        　　　  其它的，以此类推……
            表格中的每一行的高度，以这一行最高组件为基准。
            表格中的第一列的宽度，以这一列最宽组件为基准。
   ● pack(布局管理器(流式)
       ● after：将组件置于其他组件之后
       ● before：将组件置于其他组件之前
       ● anchor：组件对齐方式  center (居中显示)默认值
             n (顶对齐) s (底对齐) W (左对齐) e (右对齐)   n:上（北）s:下（南），w:左（西），E:右（东）
       ● side：组件在主窗口的位置 -选项：left, right, top, bottom
            　la1.pack( side=’top’) # 向上停靠 默认
            　la1.pack( side=’bottom) # 向下停靠
            　la1.pack( side=’left’) # 向左停靠
            　la1.pack( side=’right’) # 向右停靠
       ● fill：填充方式(Y，垂直，X，水平，BOTH，水平+垂直)，是否在某个方向充满窗口
              fill=”none” # 不填充 默认
            　fill=”x” # 横向填充
            　fill=”y” # 纵向填充
            　fill=”both” # 横向纵向都填充  -- padx/pady: 组件外，组件跟邻近组件或窗体边界的距离(外边距)  默认值0
       ● padx/pady: 组件外，组件跟邻近组件或窗体边界的距离(外边距)  默认值0
       ● ipadx/ipady: 组件内，组件文本跟组件边界之间的距离(内边距) 默认值0
       ● expand：1可扩展，O不可扩展，代表控件是否随窗口缩放   设置为1时组件可自由扩展
       ● expand: 决定组件的“势力范围”是否扩大到“扩展范围”　选项：True, False  默认值：False (标签只在自己的势力范围内活动)
   ● 部件放置 Place（）：
 　　         root.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')
       ● 再接下来我们来看place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的(50, 100)，
       ● 就是将这个部件放在坐标为(x=50, y=100)的这个位置, 后面的参数 anchor='nw'，就是前面所讲的锚定点是西北角。例如：
    __________________________________________________________________________________________________________________
    ++++         tkinter.filedialog --用于创建文件/目录选择窗口的类和函数；                                         ++++
    ------------------------------------------------------------------------------------------------------------------
   ● tkinter.filedialog --用于创建文件/目录选择窗口的类和函数
      ● askopenfile(mode='r',**options)  #以只读模式打开文件  返回一个只读模式打开的文件
      ● askopenfiles(mode='r',**options) #以只读模式打开文件夹 返回一个只读模式打开的文件夹列表
      ● 保存- asksaveasfile(**options) #选择文件存储路径并命名，参数：title、filetypes、initialdir、efaultextension
                   如果 filetypes=[(“文本文档”, “.txt”)] ，可以不写文件扩展名，扩展名自动为txt；
                   如果 *filetypes=[(‘All Files’, ’ ')] ，一定写文件扩展名，否则无扩展名；
                   如果 filetypes=[(“文本文档”, “.txt”)] ，defaultextension=‘.tif’，可以不写文件扩展名，扩展名自动为tif。
      ● 打开  - askopenfilename(***options)    #打开已存在文件，并返回选择中的文件名  (含路径)
      ● 打开 - askopenfilenames(**options)    #同时选择多个文件，返回一个元组，包括所有选择文件的路径。参数：title、filetypes、initialdir
      ● 查看- askdirectory(**options) #选择一个文件夹，返回文件夹路径；这里有一个关键字参数，mustexist—— 确定是否必须为已存在的目录
      ● class tkinter.filedialog Open(master=None,**options)  #用于加载文件的原生对话窗口
      ● class tkinter.filedialog.SaveAs(master=None,**options) #用于保存文件的原生对话窗口
         ● 参数（**optinon) 和返回值
      ● 上述函数，提供了文件对话窗口，这些窗口带有原生外观，具备可定制行为的配置项。以下关键字参数适用于上述类和函数：
        ● 参数 : parent
             对话框窗口显示，●  如果不指定该选项，那么对话框默认显示在根窗口上；
                            ● 如果想要将对话框显示在子窗口 win 上，那么可以设置 parent=win
        ● 参数 : title 窗口的标题
        ● 参数 : initialdir
                 对话框的启动目录 : ● 指定打开/保存文件的默认路径；● 默认路径是当前文件夹
        ● 参数 : initialfile   打开对话框时选中的文件
        ● 参数 : filetypes
            （ 标签，匹配模式）元组构成的列表，允许使用 “*” 通配符 ; 指定筛选文件类型的下拉菜单选项； 该选项的值是由 2 元祖构成的列表； 
             每个 2 元祖由（类型名，后缀）构成，例如：filetypes=[("TXT", ".txt"), ("JPG", ".jpg"), ("GIF", ".gif")])
        ● 参数名 : defaultextension
              默认的扩展名，用于加到文件名后面（保存对话框）。例如：defaultextension=".txt"，那么当用户输入一个文件名 “哈啊” 的时候，
              文件名会自动添加后缀为 “哈啊.txt”；如果用户输入文件名包含后缀，那么该选项不生效
        ● 参数名 : multiple    控制是否可以多选，为True则表示可以多选
        |      返回值 : 上面有提到返回值，这里再补充一个，就是如果用户点击取消的话，返回值是空字符串
    __________________________________________________________________________________________________________________
    ++++                                                  变量类型 变量追踪                                        ++++
    ------------------------------------------------------------------------------------------------------------------
    ● tkinter的变量类别   
    ● textvariable 这个属性绑定一个变量后，它们的Text就会以变量方法来呈现。
                    Button，Lable，Entry 这3个组件，它们都有text这个属性，
    ● textvariable=var  #绑定变量var  var.set() :设置变量    var.get() ：获取变量
      ● 我们可以通过config()，insert() 等方式来设置text，其实还有一个方法就是通过变量的方法，
      ● tkinter说的变量，不是pyhton里的一般变量，而是tkinter模块里的变量类(Variable)以及其下的4个子类别：
        var=IntVar() # 整型变量，默认值为：0
        var=StringVar() # 字符串变量，默认值为：“” (空字符串)
        var=DoubleVar() # 浮点型变量，默认值为：0.0
        var=BooleanVar() # 布尔型变量，默认值 为：False
   ● 变量的设置方法set()
        获取变量用 get() 方法，设置变量用 set() 方法。
   ● StringVar 顾名思义，是一个“字符串变量”对象，可以与Entry、Label等控件绑定，这里的绑定是双向绑定，
     ● StringVar对象的创建 只需要使用tkinter.StringVar()方法即可。例如：
        import tkinter as tk
        root = tk.Tk()
        entry_var = tk.StringVar()   #创建了一个名为entry_var的StringVar对象，
        entry = tk.Entry(root, textvariable=entry_var)   #   将它与一个Entry部件绑定
            # 绑定StringVar对象的方法是在创建Entry部件时，使用textvariable参数。textvariable参数必须接收一个StringVar对象作为值。
            # 也就是既可以通过该变量来获取Entry、Label等控件中的值，也可以通过更改该变量来改变Entry、Label等控件中的值。
        -entry_var.set("设置字符串内容")   #注意 这个代码写创建对象之后
        root.mainloop()
       # 一个StringVar对象可以被多个Entry部件绑定，这样可以在多个Entry部件中显示同一份文本信息
   ● 变量的追踪trace()方法
       ● 语法：变量.trace(‘模式’，回调函数)
       ● ’w’模式：write写模式，即变量有变化，就会启动回调函数
       ●  ’r’模式 ：read 读柜式，即变量被读取，就会启动回调函数
       ●  注意：回调函数必须有3个参数，但这3个参数暂时对我们没有什么用，我们用*args代替（当然用别的名字也行）
       ● 回调函数的定义和基本概念 回调函数是一种特殊的函数，它作为参数传递给另一个函数， 
                    ● 事件处理回调函数 传参为event     例如： def call_event(event)
                    ● 并在被调用函数执行完毕后被调用。回调函数通常用于事件处理、异步编程和处理各种操作系统和框架的API。
       ● *args 表示任何多个无名参数， 他本质上是一个 tuple
       ●  ** kwargs 表示关键字参数， 它本质上是一个 dict
       ● callback -- 回调   指任何无需调用参数的 Python 函数。 例如：def print_it():
                                                                       print("hi there")
                                                               fred["command"] = print_it
    ==================================================================================================================
    ++++                                              绑定和事件                                                  ++++
    ------------------------------------------------------------------------------------------------------------------
    ● 绑定和事件:tkinter 提供的事件处理机制允许我们为“控件”绑定相应的事件和事件处理函数（即 callback函数），从而实现控件与用户的交互。
       ● 事件绑定可选项 1.command= 命令   2. tk.bind (事件，回调函数)     3.tk.protocol (关闭窗口事件，回调函数)
       ● 常用事件：<Button-1> :按下鼠标第一个键（左键）  <ButtonRelease> #松开鼠标   
                  <B1-Motion> :按住鼠标左键移动（拖动） B1,B2,B3 代表鼠标左键，右键，中键   <Motion> 鼠标移动
                  <Return>: 回车键，其他同类型的键有<Shift>/<Tab>/<Control>/<Alt>/<Space>/<UP>/<Down>/<Left>/<Right>
                  <Release> :关闭（销毁）小部件
                  <Enter> : 鼠标进入控件范围；    <Leave> ：鼠标离开控件范围
                  <KeyPress-H> :按下键盘 H 键        <KeyRelease-H> :松开H 键  <Key>:任意键
                  <Control-Shift-KeyPress-H>: 组合键ctrl+shifit+H
                  <FocusOut> #组件失去焦点；  进入<FocusIn>：组件获得焦点
                  <Configure > :控件的大小发生变化
                  <Deactivate>：控件的状态由“激活”变为“未激活”
                  <Expose>	当窗口或组件的某部分不再被覆盖的时候触发事件
                  <Visibility>	当应用程序至少有一部分在屏幕中是可见状态时触发事件
       ● 事件修饰符：
           Double ：两个间隔时间很短的事件   如<Double-Button-1> 表示双击鼠标左键事件
           Triple ：快速连续的3个事件
           Any ：   一类事件               如<Any-KeyPress> 表示任意按键按下事件
           Ait , Shift ,coctrol, 表示：当用户按下此键 ，则该属性为Ture
           Lock,  用户按下Capslk 键是则该属性为Ture
           空格符写法：'<…>''<space>'<'<less>' 
         ● 也可以使用短形式 如  '<1>'是相同。'<Button-1>'   'x'是相同。'<KeyPress-x>'
         ● 一个具体事件如<Button-1>是事件类（event class）的一个实例，事件类中设定了众多属性
             属性	属性说明	适用事件类型
            .widget  发生事件是哪一个控件
            .num     1/2/3 中的一个 代表鼠标的左键，右键，中键
            .keycode  按键编码
            .char	如果按键事件产生通用ASCII字符，这个字符将赋值给event.char。（特殊ASCII字符，如delete等不属于该属性）
                                                             适用事件类型： <KeyPress> <KeyRelease>等按键事件
            .keysym	如果按键事件产生特殊ASCII字符，这个字符将赋值给event.keysym。	
                    如按下空格键：char: code:32 Keysym: space                      适用事件类型：<KeyPress><KeyRelease>等按键事件
            .x	鼠标当前位置横坐标，相对于组件左上角	  父容器
            .y	鼠标当前位置纵坐标，相对于组件左上角	  父容器
            .x_root	鼠标当前位置横坐标，相对于屏幕左上角	 整个屏幕 
            .y_root	鼠标当前位置纵坐标，相对于屏幕左上角	 整个屏幕
            .width	组件大小发生改变后的宽度	                适用事件类型：<Configure>
            .height	组件大小发生改变后的高度	                适用事件类型：<Configure>
            .type	事件类型	
    ● bind 绑定方法可觉察某些事件，并在事件发生时触发一个回调函数。bind 方法的形式是：
        ● 部件. bind(self, sequence, func, add=''):  #注意绑定小部件要在 放置小部件一前绑定  书写是代码在pack() 前
          ● sequence -- 序列
               是一个表示事件的目标种类的字符串。（详情请看 280 页。）
          ● func
               是带有一个参数的 Python 函数，发生事件时将会调用。传入的参数为一个 Event 实例。（以这种方式部署的函数通常称为 回调函数。）
          ● add
            可选项， '' 或 '+' 。传入空字符串表示本次绑定将替换与此事件关联的其他所有绑定。传递 '+' 则意味着加入此事件类型已绑定函数的列表中。
          例如   def turn_red(self, event):        #回调函数 
                     event.widget["activeforeground"] = "red"      # 访问事件的 widget 字段   前景变红
                     self.button.bind("<Enter>",self.turn_red)    #按钮绑定绑定回车键   触发回调函数
   ●Tk  Tkinter事件字段
        ● %f:焦点   ● %A:字符   ● %h:身高   ● %E: 发送事件（_E） ● %k:密钥码  ●  %K:符号码   ● %s:状况   ● %N:keysym_num
        ● %t:时间   ● %T:类型   ● %w:宽度   ● %W: 小部件         ● %x:x       ●  %X:x_root  ●  %y:y     ●  %Y：y_root
   ● Event:事件发生后的处理程序
         def handlerName(event):  #正则函数的调用序列event
   ● tprotocol-创建销毁窗口 事件绑定
         root.protocol("WM_DELETE_WINDOW",回调函数)
   __________________________________________________________________________________________________________________
    ++++                        kinter.Text  文本框（Text）组件的属性说明                                         ++++
    ------------------------------------------------------------------------------------------------------------------
--tkinter.Text  文本框（Text）组件的属性说明及示例   组件用于tkinter GUI里添加文本、图片、按钮
  语法：  widget = Text( master, parameter=value, ... ) 
      # master 文本框控件的父容器  parameter：文本框的参数  value：参数对应的值
  参数说明：  height	设置文本框的高度，高度值每加1则加一行
            width	设置文本框的宽度，宽度值每加1则加一个字节
            insert	文本框插入数据，可以指定插入数据的位置
            delete	删除文本框中的数据，可以通过数据位置，指定删除的数据
            get	    获取文本框中的数据，可以通过数据位置，指定获取的数据
            relief	文本框样式，设置控件显示效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。
            bd	    设置文本框的边框大小，值越大边框越宽
            bg	    设置文本框默认背景色
            fg	    设置文本框默认前景色，即字体颜色
            font	文本字体，文字字号，文字字形。字形有overstrike/italic/bold/underline
            state	            文本框状态选项，状态有DISABLED/NORMAL，DISABLED状态文本框无法输入，NORMAL状态可以正常输入
            highlightcolor  	设置文本框点击后的边框颜色
            highlightthickness	设置文本框点击后的边框大小
         示例：   
                import tkinter as tk
                root = tk.Tk()
                text = tk.Text(root, width=20, height=5)
                text.pack(padx=10, pady=10)
                # 设置文本格式tag
                text.tag_config('tag_1', background='yellow', foreground='red')  # bg,fg 并不是它的缩写 
                # insert 索引表示插入光标的当前位置，并可以设置文本格式
                text.insert('insert', '我今天想吃')  # 在光标位置插入
                text.insert('end','麻辣小龙虾', 'tag_1') # 在最后位置插入
                root.mainloop()  #运行结果 在 “今天我想吃”后面插入 黄底红字“ 麻辣小龙虾”
    __________________________________________________________________________________________________________________
    ++++                                               焦点 多线程  定时器                                         ++++
    ------------------------------------------------------------------------------------------------------------------
    ● focus_set方法获得焦点: 语法： 对象.focus_set()
      ● 使用focus_force方法强制获取焦点
      ● super() 函数是用于调用父类(超类)的一个方法。  
           ● super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，
                               会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
                              ● MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
           ● 语法： super(type[, object-or-type])#type:类    object-or-type 类：一般是 self
             ● python3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
   ● after方法  多线程 定时器
     ● 方法定义：after(self, ms, func=None， *args)
        ● 在给定时间后调用函数一次。MS以毫秒为单位指定时间。函数给出了要调用的函数。额外的参数作为函数调用的参数。 
              返回使用after_cancel取消调度的标识符。
        ● tk类提供的after方法不是循环的计时器  它相当于不会堵塞进程的sleep 需要循环计时的话，就再在函数里面再次after
        ● 此方法执行后，将会在规定的时间间隔之后，执行一个特定的您指定的函数。如果在您指定的这个定时执行的函数中，
        ● 再次调用after方法，就可以起到一个定时器的效果。其实，python中简单的定时器基本都是这个思路。
=========================================================================================================================
=====               end                  end                 end                 ene              edn            =======