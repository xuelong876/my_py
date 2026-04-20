
    ***********************************************************************************************************************************
    **                                              python 内置函数   基本操作                                                        **
    **   数据容器 json 字符串格式 转义 排序  流程控制 运算符 逻辑运算符  函数  对象和类  模块和包  字符串格式化详解  *和**号 快捷方式     **
    ***********************************************************************************************************************************
    ....................................................................................................................................
	1. abs(x) - 计算绝对值，x 是一个数值。
	2. all(iterable) - 检查可迭代对象中的所有元素是否为True，iterable 是一个可迭代对象。
	3. any(iterable) - 检查可迭代对象中的任意元素是否为True，iterable 是一个可迭代对象。
	4. ascii(object) - 返回对象的可打印字符串表示，object 是任何Python对象。
	5. bin(x) - 将整数转换为二进制字符串，x 是一个整数。
	6. bool(x) - 将值转换为布尔值，x 是任何Python对象。
	7. bytearray(source[, encoding[, errors]]) - 创建一个新的字节数组，source 可以是整数、字符串或其他可迭代对象，encoding 和 errors 用于字符串编码。
	8. bytes(source[, encoding[, errors]]) - 创建一个新的不可变字节数组，参数同bytearray。
	9. callable(object) - 检查对象是否可调用，object 是任何Python对象。
	10. chr(i) - 返回Unicode码点为i的字符，i 是一个整数。
	11. classmethod(function) - 将方法转换为类方法，function 是一个函数对象。
	12. compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) - 将source编译成代码或AST对象，source 是字符串或AST节点，
	                 filename 是文件名，mode 是编译模式。
	13. complex(real[, imag]) - 创建一个复数，real 是实部，imag 是虚部。
	14. delattr(object, name) - 删除对象的属性，object 是对象，name 是属性名。
	15. dict(**kwarg) - 创建一个新的字典，**kwarg 是关键字参数。
	16. dir(object) - 返回对象的所有属性和方法的列表，object 是任何Python对象。
	17. divmod(a, b) - 返回a除以b的商和余数，a 和 b 是数值。
	18. enumerate(iterable, start=0) - 返回一个枚举对象，iterable 是可迭代对象，start 是起始索引。
	19. eval(expression, globals=None, locals=None) - 计算字符串中的表达式，expression 是字符串，globals 和 locals 是全局和局部变量字典。
	20. exec(object, globals=None, locals=None) - 执行字符串中的Python代码，参数同eval。
	21. filter(function, iterable) - 构建一个迭代器，function 是函数，iterable 是可迭代对象。
	22. float(x) - 将数字或字符串转换为浮点数，x 是数字或字符串。
	23. format(value[, format_spec]) - 格式化指定值，value 是要格式化的值，format_spec 是格式说明符。
	24. frozenset(iterable) - 创建一个新的不可变集合，iterable 是可迭代对象。
	25. getattr(object, name[, default]) - 返回对象的属性值，object 是对象，name 是属性名，default 是默认值。
	26. globals() - 返回当前全局符号表的字典。
	27. hasattr(object, name) - 检查对象是否具有指定属性，object 是对象，name 是属性名。
	28. hash(object) - 返回对象的哈希值，object 是任何Python对象。
	29. help(object) - 调用内置帮助系统，object 是任何Python对象。
	30. hex(x) - 将整数转换为十六进制字符串，x 是一个整数。
	31. id(object) - 返回对象的内存地址，object 是任何Python对象。
	32. input(prompt=None) - 读取用户输入，prompt 是提示字符串。
	33. int(x[, base]) - 将数字或字符串转换为整数，x 是数字或字符串，base 是进制数。
	34. isinstance(object, classinfo) - 检查对象是否是指定类的实例，object 是对象，classinfo 是类或元组。
	35. issubclass(class, classinfo) - 检查类是否是另一个类的子类，class 是类，classinfo 是类或元组。
	36. iter(object[, sentinel]) - 返回对象的迭代器，object 是可迭代对象，sentinel 是哨兵值。
	37. len(s) - 返回对象的长度，s 是序列或集合。
	38. list(iterable) - 创建一个新的列表，iterable 是可迭代对象。
	39. locals() - 返回当前局部符号表的字典。
	40. map(function, iterable, ...) - 对可迭代对象中的每个元素应用函数，function 是函数，iterable 是可迭代对象。
	41. max(iterable, *[, key, default]) - 返回可迭代对象中的最大值，iterable 是可迭代对象，key 是函数，default 是默认值。
	42. memoryview(obj) - 返回对象的内存视图，obj 是字节序列。
	43. min(iterable, *[, key, default]) - 返回可迭代对象中的最小值，参数同max。
	44. next(iterator[, default]) - 获取迭代器的下一个元素，iterator 是迭代器，default 是默认值。
	45. object() - 返回一个新的特征不明显的对象。
	46. oct(x) - 将整数转换为八进制字符串，x 是一个整数。
	47. open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) - 打开文件并返回文件对象，
	               一般在open 前加 with 语句                              file 是文件路径，mode 是打开模式:r-自读；w-读写；a-追加。
	48. ord(c) - 返回字符的Unicode码点，c 是一个字符。
	49. pow(base, exp[, mod]) - 计算幂运算，base 是基数，exp 是指数，mod 是模数。
	50. print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) - 打印对象，objects 是要打印的对象，sep 是分隔符，end 是结束符。
	51. property(fget=None, fset=None, fdel=None, doc=None) - 返回属性属性。
	52. range(start, stop[, step]) - 创建一个整数范围迭代器，start 是起始值，stop 是结束值，step 是步长。
	53. repr(object) - 返回对象的可打印表示，object 是任何Python对象。
	54. reversed(seq) - 返回序列的逆序迭代器，seq 是序列。
	55. round(number[, ndigits]) - 四舍五入数字，number 是数字，ndigits 是小数位数。
	56. set(iterable) - 创建一个新的集合，iterable 是可迭代对象。
	57. setattr(object, name, value) - 设置对象的属性值，object 是对象，name 是属性名，value 是值。
	58. slice(start, stop[, step]) - 返回切片对象，start 是起始索引，stop 是结束索引，step 是步长。
	59. sorted(iterable, *, key=None, reverse=False) - 返回一个新的排序列表，iterable 是可迭代对象，key 是排序键，reverse 是是否反转。
	60. staticmethod(function) - 将方法转换为静态方法，function 是函数对象。
	61. str(object='') - 创建一个新的字符串，object 是任何Python对象。
	62. sum(iterable, /, start=0) - 返回可迭代对象的总和，iterable 是可迭代对象，start 是起始值。
	63. super([type[, object-or-type]]) - 返回父类对象，type 是子类，object-or-type 是对象或子类。
	64. tuple(iterable) - 创建一个新的元组，iterable 是可迭代对象。
	65. type(object) - 返回对象的类型，object 是任何Python对象。
	66. vars(object) - 返回对象的属性和属性值的字典，object 是任何Python对象。
	67. zip(*iterables) - 创建一个聚合了多个可迭代对象的迭代器，iterables 是可迭代对象。
	=====================================================================================================================
	====    数据容器    列表（list）、集合（set）、字典（dict）和字符串（str） 元组（tple）                             ====
    =====================================================================================================================
    ●【列表list】
	1.  append(self, item)            # 在列表末尾添加一个元素
	2.  clear(self)                   # 移除列表中的所有元素
	3.  copy(self)                    # 返回列表的浅拷贝
	4.  count(self, value)            # 返回列表中某个值的出现次数
	5.  extend(self, iterable)        # 在列表末尾一次性追加另一个序列中的多个值
	6.  index(self, value, start=0, stop=len(list))  # 返回列表中某个值的第一个匹配项的索引
	7.  insert(self, index, item)     # 在指定位置插入一个元素
	8.  pop(self, index=-1)           # 移除并返回列表中的一个元素（默认最后一个）
	9.  remove(self, value)           # 移除列表中第一个匹配的值
	10. reverse(self)                 # 反转列表中的元素
	11. sort(self, *, key=None, reverse=False)  # 对列表中的元素进行排序
	●【集合set】
	  ●创建集合  set=(value1,value2)
	  ●空集合   empty_set= set()
	1.  add(self, elem)               # 向集合中添加一个元素
	2.  clear(self)                   # 移除集合中的所有元素
	3.  copy(self)                    # 返回集合的浅拷贝
	4.  difference(self, *others)     # 返回一个新集合，包含在第一个集合中但不在其他集合中的元素
	5.  difference_update(self, *others)  # 从集合中移除在其他集合中存在的元素
	6.  discard(self, elem)           # 如果元素在集合中，则移除该元素
	7.  intersection(self, *others)   # 返回一个新集合，包含在所有集合中都存在的元素
	8.  intersection_update(self, *others)  # 更新集合，只保留存在于所有集合中的元素
	9.  isdisjoint(self, other)       # 如果两个集合没有交集，则返回 True
	10. issubset(self, other)         # 如果集合是另一个集合的子集，则返回 True
	11. issuperset(self, other)       # 如果集合是另一个集合的超集，则返回 True
	12. pop(self)                     # 移除并返回集合中的一个任意元素
	13. remove(self, elem)            # 如果元素在集合中，则移除该元素（如果元素不存在则抛出 KeyError）
	14. symmetric_difference(self, other)  # 返回一个新集合，包含在两个集合中但不同时存在于两者中的元素
	15. symmetric_difference_update(self, other)  # 更新集合，只保留在两个集合中但不同时存在于两者中的元素
	16. union(self, *others)          # 返回一个新集合，包含所有集合中的元素
	17. update(self, *others)         # 使用其他集合中的元素更新当前集合
	●【字典dict】
	1.  clear(self)                   # 移除字典中的所有项
	2.  copy(self)                    # 返回字典的浅拷贝
	3.  fromkeys(cls, iterable, value=None)  # 创建一个新字典，以 iterable 中的元素作为键，value 作为所有键的初始值
	4.  get(self, key, default=None)  # 返回指定键的值，如果键不存在则返回默认值
	5.  items(self)                   # 返回一个包含字典键值对的视图对象
	6.  keys(self)                    # 返回一个包含字典键的视图对象
	7.  pop(self, key, default=None)  # 移除并返回指定键的值，如果键不存在则返回默认值
	8.  popitem(self)                 # 移除并返回字典中的一个键值对（Python 3.7+ 保证按插入顺序返回）
	9.  setdefault(self, key, default=None)  # 如果键不存在，则插入键并设置默认值，返回键的值
	10. update(self, E=None, **F)     # 使用来自 E 或 **F 的键值对更新字典
	11. values(self)                  # 返回一个包含字典值的视图对象
	●【元组 tple】
	 ●创建元组 tple={ value1,value2}  ，可以省略括号
	 ●创建空元组（必须使用 ()）  empty_tuple = ()
     ●不可变性：元组是不可变的，因此没有像列表那样的 append()、remove()、pop() 等修改方法。
     ●有限的方法：元组的方法主要集中在查找和计数操作上，因为这些操作不需要修改元组的内容。
     ●性能优势：由于元组的不可变性，Python 可以对其进行优化，使得元组在某些情况下比列表更高效，特别是在用作字典的键时。
	1.  tuple.count(value)                            #返回元组中指定值出现的次数
	2.  tuple.index(value, start=0, stop=len(tuple))  #返回元组中指定值第一次出现的索引 
	●【字符串str】
	1.  capitalize(self)              # 返回字符串的副本，首字母大写
	2.  casefold(self)                # 返回字符串的副本，用于大小写不敏感的比较
	3.  center(self, width, fillchar=' ')  # 返回一个指定宽度的新字符串，原字符串居中
	4.  count(self, sub, start=0, end=len(string))  # 返回子字符串在字符串中出现的次数
	5.  encode(self, encoding='utf-8', errors='strict')  # 使用指定的编码对字符串进行编码
	6.  endswith(self, suffix, start=0, end=len(string))  # 如果字符串以指定的后缀结尾，则返回 True
	7.  expandtabs(self, tabsize=8)   # 将字符串中的制表符扩展为空格
	8.  find(self, sub, start=0, end=len(string))  # 返回子字符串在字符串中第一次出现的索引
	9.  format(self, *args, **kwargs) # 格式化字符串
	10. format_map(self, mapping)     # 使用映射对象格式化字符串
	11. index(self, sub, start=0, end=len(string))  # 返回子字符串在字符串中第一次出现的索引（如果未找到则抛出 ValueError）
	12. isalnum(self)                 # 如果字符串至少有一个字符且所有字符都是字母或数字，则返回 True
	13. isalpha(self)                 # 如果字符串至少有一个字符且所有字符都是字母，则返回 True
	14. isdecimal(self)               # 如果字符串只包含十进制数字，则返回 True
	15. isdigit(self)                 # 如果字符串只包含数字，则返回 True
	16. islower(self)                 # 如果字符串中的所有字母字符都是小写，则返回 True
	17. isnumeric(self)               # 如果字符串只包含数字字符，则返回 True
	18. isspace(self)                 # 如果字符串只包含空白字符，则返回 True
	19. istitle(self)                 # 如果字符串是标题化的（每个单词的首字母大写），则返回 True
	20. isupper(self)                 # 如果字符串中的所有字母字符都是大写，则返回 True
	21. join(self, iterable)          # 使用字符串作为分隔符连接可迭代对象中的元素
	22. ljust(self, width, fillchar=' ')  # 返回一个指定宽度的新字符串，原字符串左对齐
	23. lower(self)                   # 返回字符串的副本，所有字母字符都转换为小写
	24. lstrip(self, chars=None)      # 移除字符串左侧的空白字符（或指定字符）
	25. partition(self, sep)          # 在指定分隔符第一次出现的位置分割字符串，返回一个包含三部分的元组
	26. replace(self, old, new, count=-1)  # 返回字符串的副本，其中所有出现的子字符串都被替换
	27. rfind(self, sub, start=0, end=len(string))  # 返回子字符串在字符串中最后一次出现的索引
	28. rindex(self, sub, start=0, end=len(string))  # 返回子字符串在字符串中最后一次出现的索引（如果未找到则抛出 ValueError）
	29. rjust(self, width, fillchar=' ')  # 返回一个指定宽度的新字符串，原字符串右对齐
	30. rpartition(self, sep)         # 在指定分隔符最后一次出现的位置分割字符串，返回一个包含三部分的元组
	31. rstrip(self, chars=None)      # 移除字符串右侧的空白字符（或指定字符）
	32. split(self, sep=None, maxsplit=-1)  # 使用指定的分隔符分割字符串，返回一个列表
	33. splitlines(self, keepends=False)  # 根据换行符分割字符串，返回一个列表
	34. startswith(self, prefix, start=0, end=len(string))  # 如果字符串以指定的前缀开头，则返回 True
	35. strip(self, chars=None)       # 移除字符串两侧的空白字符（或指定字符）
	36. swapcase(self)                # 返回字符串的副本，所有字母字符的大小写互换
	37. title(self)                   #用于返回字符串的标题化版本，标题化意味着每个单词的首字母大写，而其余字母小写
	38. translate(self, table)         # 根据给定的翻译表对字符串进行翻译
	39. upper(self)                   # 返回字符串的副本，所有字母字符都转换为大写
	40. zfill(self, width)            # 返回字符串的副本，左侧用零填充到指定宽度
	41. isidentifier(self)            # 如果字符串是有效的 Python 标识符，则返回 True
	42. isprintable(self)             # 如果字符串中的所有字符都是可打印的或字符串为空，则返回 True
	43. isascii(self)                 # 如果字符串中的所有字符都是 ASCII 字符，则返回 True
	44. encode(self, encoding='utf-8', errors='strict')  # （重复列出但为完整性）使用指定的编码对字符串进行编码
	45. maketrans(self, *args)        # 返回一个翻译表，可用于 translate 方法
		# 特定于正则表达式的字符串方法（通常结合 re 模块使用，但字符串有一些简单支持）
		# 严格来说，这些不是 str 的直接方法，但常用于字符串处理
    47. (通过 re 模块) re.match(), re.search(), re.findall(), re.sub() 等
        ------------------------------------------------------------------------
		# 字符串的迭代与索引（虽然不是方法，但常用操作）
		# 可以通过索引访问字符串中的字符，例如 s[0]，也可以通过 for 循环迭代字符串
		# 额外的一些字符串操作（通过内置函数或模块）
	 48. len(s)                      # 返回字符串的长度
	 49. ord(c)                      # 返回字符的 Unicode 码点
	 50. chr(i)                      # 返回 Unicode 码点对应的字符
	 51. str.join(iterable)          # （前面已列出，但强调其作为类方法的使用）
        -------------------------------------------------------------------------
		# 字符串的编码解码（高级用法）
	 52. decode(encoding='utf-8')    # 通常用于字节对象的解码，但理解字符串编码过程很重要
	   # 实际上字符串对象没有 decode 方法，这是字节对象的方法，但理解编码/解码有助于处理字符串
       # 字符串的比较操作 # 字符串支持 ==, !=, <, <=, >, >= 等比较操作符
	   # 字符串的切片  # 可以通过切片操作访问字符串的子串，例如 s[start:end:step]
	 ======================================================================================
     ====                         字符串格式forma 拼接         文后有详细介绍           ==== 
     ======================================================================================
	1.使用 % 操作符：这是较旧的字符串格式化方法，通过 %s、%d 等占位符来指定格式。
	      # return "My name is %s and I am %d years old." % (name, age)
    2.使用 str.format() 方法：这是较新的方法，通过 {} 占位符来指定格式，并使用 .format() 方法来填充这些占位符。
          # return "My name is {} and I am {} years old.".format(name, age)
    3.使用 f-string：这是 Python 3.6 引入的新特性，通过在字符串前加上 f，并在字符串内部使用 {} 占位符来直接嵌入变量。
          # return f"My name is {name} and I am {age} years old."
    4.字符格式化拼接 多个变量占位，变量要有括号括起来，并按照占位的顺序填入。
         #print("%d * %d = %d" %(i,j,k),end=" ")  输出 i*j=k 不换行结尾加空格（end=" ")
       ● %s 将内容装换成字符串放入占位位置，%d 将内容装换成整数，放入占位位置，%f 将内容转换成浮点型放入占位位置。
       ● m,控制数字宽度， 小于数字本身不生效，.n,控制小数精度，要求是数字，会进行小数四舍五入
     ======================================================================================
     ====                             json    import json                              ==== 
     ======================================================================================
     ● 解析 JSON（反序列化） 将json字符转为python字典dicts
     ● json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
        ● s: 包含 JSON 文档的字符串。
        ● cls（可选）：自定义的 JSONDecoder 子类。
        ● object_hook（可选）：一个函数，用于解码 JSON 对象。这个函数会接收一个字典参数，并返回一个替换的 Python 对象。
        ● parse_float（可选）：用于解析浮点数的函数。
        ● parse_int（可选）：用于解析整数的函数。
        ● parse_constant（可选）：用于解析字符串常量的函数，比如 -Infinity, Infinity, NaN。
        ● object_pairs_hook（可选）：一个函数，用于解码 JSON 对象，但会保留键值对的顺序。
     ● 生成 JSON（序列化）  将python字典转为json字符串
     ● json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None,
                                                                                ● default=None, sort_keys=False, **kw)
        ● obj: 要序列化的 Python 对象。
        ● skipkeys（可选）：如果为 True，则跳过非基本类型的键（默认 False）。
        ● ensure_ascii（可选）：如果为 True，则所有非 ASCII 字符会被转义（默认 True）。
        ● check_circular（可选）：如果为 True，则检查循环引用（默认 True）。
        ● allow_nan（可选）：如果为 True，则允许 NaN, Infinity, 和 -Infinity 作为 JSON 值（默认 True）。
        ● indent（可选）：指定缩进的空格数，用于美化输出。
        ● separators（可选）：指定项之间的分隔符，例如 (',', ': ')。
        ● default（可选）：一个函数，用于处理无法序列化的对象。
        ● sort_keys（可选）：如果为 True，则输出字典的键会按字母顺序排序（默认 False）。
     ======================================================================================
     ====                          字符串 转义字符 格式化                               ==== 
     ======================================================================================
	一： 转义字符 在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。如下表：
	        转义字符        	描述
	        \(在行尾时)     	续行符
	        \\	            反斜杠符号
	        \'	            单引号
	        \"	            双引号
	        \a	            响铃
	        \b	            退格(Backspace)
	        \e	            转义
	        \000	        空
	        \n	            换行
	        \v	            纵向制表符
	        \t	            横向制表符
	        \r	            回车
	        \f	            换页
	        \oyy	        八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
	        \xyy	        十六进制数，以 \x 开头，yy代表的字符，例如：\x0a代表换行
	        \other	        其它的字符以普通格式输出
	二：Python字符串运算符  下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
	    操作符	描述                      	实例
	    +	    字符串连接	                >>>a + b    'HelloPython'
	    *	    重复输出字符串	            >>>a * 2    'HelloHello'
	    []	    通过索引获取字符串中字符	    >>>a[1]     'e'
	    [ : ]	截取字符串中的一部分	        >>>a[1:4]   'ell'
	    in	    成员运算符 - 如果字符串中包含给定的字符返回 True	>>>"H" in a             True
	    not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	>>>"M" not in a     True
	    r/R 	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 
	            原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
	            >>>print r'\n'   \n
	            >>> print R'\n'   \n
	    %	格式字符串	请看下面
	三： 1）python 字符串格式化符号:
	          符号	 描述
	          %c	 格式化字符及其ASCII码
	          %s	 格式化字符串
	          %d	 格式化整数
	          %u	 格式化无符号整型
	          %o	 格式化无符号八进制数
	          %x	 格式化无符号十六进制数
	          %X	 格式化无符号十六进制数（大写）
	          %f	 格式化浮点数字，可指定小数点后的精度
	          %e	 用科学计数法格式化浮点数
	          %E	 作用同%e，用科学计数法格式化浮点数
	          %g	 %f和%e的简写
	          %G	 %F 和 %E 的简写
	          %p	 用十六进制数格式化变量的地址
	    2）格式化操作符辅助指令:
	            符号	    功能
	            *	    定义宽度或者小数点精度
	            -	    用做左对齐
	            +	    在正数前面显示加号( + )
	            <sp>	在正数前面显示空格
	            #	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
	            0	    显示的数字前面填充'0'而不是默认的空格
	            %	    '%%'输出一个单一的'%'
	            (var)	映射变量(字典参数)
	            m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
	            Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
    ========================================================================================
    ====                              排序 sorted                                       ====
    ========================================================================================
    ● sorted() 是一个内置函数，用于返回一个新的排序后的列表（不会修改原列表）
    ● sorted(iterable, key=None, reverse=False)
	    ● iterable：需要排序的可迭代对象（如列表、元组等）。
		● key：一个函数，用于指定排序的依据（默认按元素本身排序）。
		● reverse：布尔值，True 表示降序排序，False 表示升序排序（默认）

    ============================================================================================================================
    ====                   流程控制 （循环 判断 异常处理）  列表推导式  三元表达式                                            ====
    ============================================================================================================================
    [expression for item in iterable if condition]
	   ● expression 是对 item 进行处理的表达式。
	   ●item 是从 iterable 中获取的元素。
	   ●iterable 是一个可迭代对象，如列表、元组、字符串等。
	   ●condition 是一个可选的条件语句，用于过滤 iterable 中的元素
   【三元表达式】
       max_value = x if x > y else y    #如果 x > y 为 True，则 max_value 被赋值为 x。否则，max_value 被赋值为 y
   【条件判断 (if-elif-else)】
	    if 条件1:
		    执行代码1
		elif 条件2:
		    执行代码2
		else:
    		执行代码3
   【循环控制结构】
   		【for循环控制】
   			 for 变量 in 可迭代对象:
   				循环体代码
   				break -跳出迭代
   		【while循环控制】
   		     while 条件:
                循环体代码
                continue - 跳过当前迭代
   【异常处理 (try-except-else-finally)】
	   	try:
	   		 # 可能出错的代码
	    	 result = 10 / 0
		except ZeroDivisionError:
			# 处理特定异常
			print("不能除以零")
		except Exception as e: #捕获所有异常并改名为e
			# 处理其他异常
			print(f"发生错误: {e}")
		else:
			# 没有异常时执行
			print("计算成功")
		finally:
			# 无论是否异常都会执行
			print("执行结束")
	【上下文管理 (with语句)】
	 	 with open('file.txt', 'r') as f:
		     content = f.read()
		     # 文件会自动关闭 
	=================================================================================
	====                           运算符                                        ====
	=================================================================================
		& 按位与运算符
		| 按位或运算符
		^ 按位异或运算符
		~ 按位取反运算符
		<< 3 左移3位，高位丢弃，低位补0
		>> 3 右移3位，低位丢弃，高位补0
		%取余数（取模）    // 取整数    **指数
	================================================================================
	====                        逻辑运算符 a=10 b=20                           =====
    ================================================================================
	● and	    x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
	● or   	x or y	布尔"或" - 如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值。	(a or b) 返回 10。
	● not 	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
	======================================================================================
	====                           函数 匿名函数                                      ====
	======================================================================================
	●【匿名函数Anonymous Function】
	 ● ambda 参数1, 参数2, ... : 表达式
	 ● add = lambda x, y: x + y   #l定义了一个匿名函数，接受两个参数 x 和 y，返回它们的和。将匿名函数赋值给变量 add
     ● add(3,5)                   #通过 add(3, 5) 调用匿名函数。
    ●【函数】
     ● def fonction(形参1，形参2，形参n)     #位置参数：按顺序传递的参数
     ● def fonction(形参1，形参2=默认参数)   #可以为参数提供默认值，调用时可以选择不传递该参数
     ● def fonction(*args)                  # *args：接收任意数量的位置参数，以元组形式传递。
     ● def fonction(***kwargs)              #**kwargs：接收任意数量的关键字参数，以字典形式传递                                   
     ● return                               #函数返回值
        #关键字参数：调用函数时，通过参数名指定参数值，可以不按顺序传递
    ======================================================================================
	====         Python中，星号（*）和双星号（**）是非常强大的工具                      ====
	======================================================================================
	1. 星号（*）
        • 解包（Unpacking）： 将一个可迭代对象（如列表、元组）解包成单独的元素。
              numbers = [1, 2, 3, 4]
              print(*numbers)  # 输出：1 2 3 4
        • 可变数量参数： 在函数定义中，接收任意数量的位置参数
    2. 双星号（**）
        • 解包字典（Unpacking Dictionaries）： 将一个字典解包成关键字参数。： 
                def display_info(name, age):
                    print(f"Name: {name}, Age: {age}")
                person = {"name": "Alice", "age": 30}
                display_info(**person) # 输出 ：Name: Alice, Age: 30
        • 可变数量关键字参数： 在函数定义中，接收任意数量的关键字参数。 
    ======================================================================================
	====                           对象 和类                                          ====
	======================================================================================
	● class ClassName:         #创建类
	    """类的文档字符串"""
、	    # 类属性（所有实例共享）
	    class_attribute = "我是类属性"
、	      # 初始化方法（构造函数）
	    def __init__(self, attribute1, attribute2):
	        self.attribute1 = attribute1  # 实例属性
、	    # 类方法
	    def method1(self):
	        pass
、	    @classmethod          #装饰器
	    def class_method(cls):
	        pass
    ● 类的属性和方法：
		● 属性：
			● 实例属性：每个对象独有的属性，通过 self 定义。
			● 类属性：所有对象共享的属性，直接在类中定义。
		● 方法：
			● 实例方法：第一个参数为 self，操作实例属性。
			● 类方法：使用 @classmethod 装饰器，第一个参数为 cls，操作类属性。
			● 静态方法：使用 @staticmethod 装饰器，不依赖实例或类。
		● 继承
			● 类可以继承其他类，子类会继承父类的属性和方法。
			● class Car(父类ClassName):  # Car 继承自 父类ClassName
			    代码区：子类属性和方法
        ● 多态 :子类可以重写父类的方法，实现多态。
        ● 封装
			● 封装是将数据（属性）和操作数据的方法绑定在一起，隐藏对象的内部实现细节。
			● 使用私有属性（以双下划线开头）实现封装。
			  ● self.__balance = balance  # 私有属性
		● 总结
			● 类是对象的模板，定义了对象的属性和行为。
			● 对象是类的实例，具有类定义的属性和行为。
			● 继承允许子类继承父类的属性和方法，实现代码复用。
			● 多态允许子类重写父类的方法，实现不同的行为。
			● 封装隐藏对象的内部实现细节，提供公共接口。
    ● 对象的创建:
        ● account = ClassName(形参)   #使用类名加括号来创建对象（实例化）
    ●【内置装饰器Decorator】
		● @staticmethod：将方法转换为静态方法。
		● @classmethod：将方法转换为类方法。
		● @property：将方法转换为属性访问。
		● @functools.lru_cache：用于缓存函数结果，提高性能。
	●【装饰器】
		● 装饰器是 Python 中的一种高级特性，用于在不修改原函数代码的情况下，动态地扩展函数或方法的功能。
		● 装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个新的函数。
			def my_decorator(func):            #装饰器函数，它接收 say_hello 函数作为参数，并返回一个新的函数 wrappe
			    def wrapper(*args, **kwargs):  #wrapper 函数在调用 say_hello 的前后添加了额外的功能
			        print("函数开始执行")
			        result = func(*args, **kwargs)
			        print("函数执行结束")
			        return result
			    return wrapper
			 # @my_decorator 等价于 say_hello = my_decorator(say_hello)
			@my_decorator                  #使用 @decorator_name 语法糖将装饰器应用到函数上
			def say_hello(name):
			    print(f"Hello, {name}!")
			say_hello("Alice")
			# 输出：# 函数开始执行 # Hello, Alice! # 函数执行结束
	● 装饰器的堆叠：
   			● 多个装饰器可以叠加使用，执行顺序是从内到外。
 	● 保留原函数的元数据
			● 装饰器会覆盖原函数的元数据（如函数名、文档字符串）。
			● 使用 functools.wraps 保留原函数的元数据。
				def my_decorator(func):
				    @functools.wraps(func)
	● 类装饰器
			● 特点：使用类实现装饰器，通过 __call__ 方法使类的实例可调用
				class MyDecorator:                      #类装饰器 MyDecorator
				    def __init__(self, func):           #__init__ 方法：接收被装饰的函数 func，并将其保存为实例属性
				        self.func = func
				    def __call__(self, *args, **kwargs): #当装饰后的函数被调用时，实际上调用的是 MyDecorator 实例的 __call__ 方法。
				        print("函数开始执行")                 # 在函数执行前添加逻辑
				        result = self.func(*args, **kwargs)  # 调用被装饰的函数
				        print("函数执行结束")                 # 在函数执行后添加路径
				        return result                        #返回被装饰函数的返回值
				@MyDecorator         #使用类装饰器 装饰函数say_hellol(),将say_hello()作为参数传递给MyDecorator类的实例来实现装饰
				def say_hello(name): #被装饰函数
				    print(f"Hello, {name}!")
				say_hello("Alice")：
				#输出：# 函数开始执行  # Hello, Alice!   # 函数执行结束
	● 装饰器工厂
			● 特点：返回装饰器的函数，常用于动态生成装饰器。
			def decorator_factory(prefix):      #接收一个 prefix 参数，用于生成装饰器时的前缀信息，返回一个装饰器函数 decorator
			    def decorator(func):            #装饰器函数 接收一个目标函数 func 并返回一个包装函数 wrapper
			        def wrapper(*args, **kwargs):      #在目标函数执行前，打印前缀和提示信息。调用目标函数 func，并传递参数。
			            print(f"{prefix} 函数开始执行")
			            result = func(*args, **kwargs) #调用目标函数 func，并传递参数
			            print(f"{prefix} 函数执行结束")
			            return result                  #返回目标函数的执行结果
			        return wrapper             #返回一个包装函数 wrapper
			    return decorator               #返回一个装饰器函数 decorator。
			@decorator_factory("DEBUG")    # 使用装饰器工厂创建一个装饰器，并应用到 say_hello 函数 ，装饰器本身需要参数，通过嵌套函数实现。
			def say_hello(name):
			    print(f"Hello, {name}!")       #目标函数的实际逻辑，打印问候语
			say_hello("Alice")				   # 调用被装饰后的 say_hello 函数
			# 输出：	# DEBUG 函数开始执行 # Hello, Alice! # DEBUG 函数执行结束
			●在 Python 中，装饰器语法 @ 是一种语法糖，它会在函数定义时立即执行装饰器相关的操作。
			1. 在执行定义装饰器函数 say_hello 之前，先执行decorator_factoy("DBUG") 装饰工场函数，返回decorator新的函数
			2. 应用装饰函数，decorator 函数被应用到say_hello函数上，也就是 say_hello 函数会作为参数传递给decorator函数
			3. 返回包装函数，decorator返回的wrapper 包装函数会替代原来的 say_hello函数
	● 装饰器的实际应用
			● 日志记录：记录函数的调用信息。
			● 性能测量：计算函数的执行时间。
			● 权限验证：在执行函数前检查用户权限。
			● 缓存：缓存函数的计算结果。
    ======================================================================================
	====                    python    模块 包                                         ====
	======================================================================================
    ● 模块的快捷导入 输入模块名 点击模块名 按Ait +Enter 然后选中要导入的包
    ● 模块的导入语法： [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]   #中括号表示可选
    ● 常用的组合方式：  as 别名 就是对这个功能（函数）改名字
         ● import 模块名      #import 翻译：导入        调用内部函数（类，变量）： 模块名.函数（实参）
         ● from 模块名 import 类、变量、方法等          #from 导入的模块 可以直接调用内部函数  不要写模块名
         ● from 模块名 import *
         ● import 模块名 as 别名
         ● from 模块名 import 功能名 as 别名      #从模块导入 一部分功能 
    ● 自定义模块（python 文件）：创建一个python文件， 调用时用 import 文件名
    ● 调试模块：
         ● if__main__ = __main__  变量 的功能是当程序是直接执行的才会进入if 内部，如果是被导入的，则if无法进入。
         ●  直接输入main 自动变成 if__main__ = __main__
         ● 添加 __all__= [变量] 当使用 from xxx import * 导入时 只能导入这个变量列表的元素  只限于 improt * 有效
    ● python包：就是一个文件夹，内部包含了 一个 __init__.py 文件，该文件夹可包含多个python 模块
       ● 新建包  my_package                           #新建→python package→ 输入包名
       ● 新建包内模块： my_module1和my_module2
       ● 导入包：improt 包名.模块名
           ● 使用：  包名,模块名.目标
    ● 安装第三方包：命令提示符下 输入 pip install 包名称  ：即可通通过网络快速安装第三方包
           ● 国内镜像站安装： pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple 包名   #网址为清华站
           ● 在pycharm 中安装:settings → Project Interpreter → "+"→  (勾选options 填写 -i 镜像网址)
    ======================================================================================
	====            字符串格式：% 、str.format()、f-string、format()                   ====
	======================================================================================
    ● % 语法："%[(name)][flags][width][.precison]type" % 待格式化数据
    ● 参数：format()是python的一个内置函数，其使用频率不高，语法和str.format()大同小异，可以结合lambda函数使用或在其它一些特定情况下使用。
          (1)name:字典参数  不用字典参数时可以不写 直接写%d %s
          (2）flags:1）-: 左对齐，，正数不加，负数加-号
                    2)+: 右对齐，如果是正数，显示的数字前面有+号 ，负数加-号， 如：%+10 %25   #右对齐 +25
                    2) 空格: 右对齐(默认的对齐方式)，正数前加空格，负数前加负号;
                    3) 0: 右对齐，以0填充，正数无符号，负数加负号，并将符号放置在0最左侧;
          (3) width: 占位宽度, 若指定宽度小于原数据长度则按原长度数据输出;
          (4) .precison: 小数点后保留位数；在字符串中则表示截取/字符串切片;
          (5) type: 详见如下...
                (1) s: string, 字符串;
                (2) d: decimal integer, 十进制数;
                (3) l: integer, 用法同%d; 表示长整型（long integer） 在Python 3中所有的整数类型都是“长整型”
                (4) u: unsigned integer, 无符号十进制数;
                (5) f: float, 浮点数(默认保留小数点后6位);
                (6) F: Float, 浮点数(默认保留小数点后6位);
                (7) e: exponent, 将数字表示为科学计数法(小写e, 默认保留小数点后6位);
                (8) E: Exponent, 将数字表示为科学计数法(大写E, 默认保留小数点后6位);
                (9) o: octal, 八进制数(即0-7);
                (10) x: hexdecimal, 十六进制数(即0-9a-f);
                (11) X: Hexdecimal, 十六进进制数(0-9A-F);
                (12) g: general format, 通用格式，详见如下...;
                (13) G: General format, 通用格式，详见如下...;
                (14) %c: character, 将十进制数转换为所对应的unicode值;
                (15) %r: representation, 调用__repr__魔法方法输出;
                (16) %%: 转义%，输出百分号。
    ● str.format()格式化
       ● 语法："{[index][:[[fill]align][sign][#][0][width][grouping_option][.precision][type]]}".format()
       ● 参数详解
        (1) index: 待格式化字符的索引或键，若占位符数量和参数数量不一致时必须指定索引;
        (2) fill: 填充字符，可为任意字符;
        (3) align: 对齐方式(常配合width使用)，可选:
         # 和Excel中输入文本和数字的默认对齐方式一致
            1) <: 左对齐(字符串默认对齐方式);
            2) >: 右对齐(数字默认对齐方式);
            3) ^: 居中对齐;
            4) =: 内容右对齐，将符号(+或-)放置在填充字符的左侧，仅对数字类型有效;
        (4) sign: 有无符号，可选：
            1) +: 正数加正号，负数加负号；
            2) -: 正数不变，负数加负号(默认)；
            3) 空格: 正数加空格，负数加负号；
        (5) #:  
               a. 对于整数，在输出值分别添加响应的0b, 0o, 0x前缀;
               b. 对于浮点数和复数, 在输出值保留小数点符号;
               c. 在g/G模式下，保留末尾的0；
        (6) 0: 若未设置对齐方式，在width前加一个0将为数字类型启用感知正负号的零填充，等同于设置fill为0, align为"=";
        (7) width: 字段总宽度(十进制整数), 所有前缀，分隔符和其它格式化字符之和;  
        (8) grouping_option: 设置分组(分隔):
               1) ",": 使用逗号作为千位分隔符;
               2) "_": 使用_作为分隔符:
                  a. 对于十进制数, 使用_作为千位分隔符;
                  b. 对于b, o, x/X，使用_每4位数插入一个下划线；
        (9) .precision(十进制数):  
               a. 整数型不允许设置precison, 如果设置即被转换为浮点数;
               b. 浮点型表示小数点"后"显示多少位小数位数;
               c. 以g或G格式化表示在小数点"前后"共显示多少个数位;
               d. 字符型表示截取多少个字符；
        (10) {{或}}: 转义{或}，当需要输出{或}的使用使用;
        (11) type: 详见如下...
             format()格式化与%格式化的type大同小异，
            (1) b: binary, 二进制;
            (3) g: general formatting, 
            (4) G: General formatting, 
    ● f-string格式化
       ● 语法：f"{变量1}{变量2}{变量n}"
       ● python3.6以后开始支持f-string字符串。f-string即formatting string, 它是str.format()的一个变种，其语法形式之殊途同归
       ● 很多时候使用f-string可以有效减少代码量，更为清晰易读
    ● format()
       ● 语法：format(x, formatter) # x为需要格式化的数据，formatter为格式化表达式，不需要指定{}
 ===================================================================================================================================
    ● Ctrl+d 复制上一行到下一行   ● Ctrl+y 删除一行，      ● shift+Enter 快速回到下一行行首，        ● Ctrl+/  批量注释和取消批量注释；
    ● 选中几行代码 按Tab 键缩进   ● ctrl+p 调出可用参数    ● 按shift+tab 取消缩进 ctrl+- 折叠代码    ● Ctrl+shift 全部展开代码  
    ● 按Ait 键 鼠标左键选几行，可以对选中的几行同时输入字符，
    ● 按ctrl 鼠标左键点击 python 模块名 可显示模块代码内容
    ●  python中使用DocStrings ： 注释 在定义函数时 第二行 输完三对英文双引号 按回车键 加入注释 变量说明
 =====================================================================================================================================
 ====                    end              end              end             end               end                              ========
 -------------------------------------------------------------------------------------------------------------------------------------



  

	
    
