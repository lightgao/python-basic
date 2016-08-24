#!/usr/bin/python
#coding=utf-8


# ======= Python Basic Tutorial
# http://www.tutorialspoint.com/python/index.htm




# -------- Language Features:
# Interpreted
# Interactive
# Object-Oriented
# Portable
# a Beginner's Language : easy to learn, read, maintain
# broad standard library : databases, gui, maths ...



# -------- Five standard data types
# Numbers   (int, long, float, complex
# String
# List
# Tuple
# Dictionary



# -------- Python Command:
# -d (debug
# -v (verbose
# -c cmd (run python scripts in command





# ======================================================================
#       语法:
#            变量定义，单行拆多行 \，多行并单行 ;
#            if ... elif ... else ...
#            三引号（字符串段落）
#       标准输出：
#            print的使用

print "Hello, Python!"                          # print string on one line

fname = 'Liang'
sname = "Gao"
print "Hello,",\
    fname,sname                                 # print mutiple variables, space will be added between each of them automatically
                                                # multiple lines statements: '\'

word = 'word'
sentence = "This is a sentence."                # " = '
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""         # triple quotes are used to span the string across multiple lines

import sys; x = 'foo'; sys.stdout.write(x + '\n')   # multiple statements in one line: ';'

case = 1
if case==0 :                                    # if statement: 'if ... elif ... else ...'
   strcase = 'zero'
elif case==1 :
   strcase = 'one'
else :
   strcase = '> one'
print strcase




# ======================================================================
#
# 不必读懂下面的程序，留意点：
#       语法：
#            变量定义，if，while, try...except...
#            字符串相等==
#       标准输入输出：
#            raw_input, print
#       标准文件读写:
#            open, FileIO.read / write / close
#       程序退出:
#            sys.exit
#

import sys

file_name = "temp.txt"
file_finish = "END"
try:                                                # " try ... except ... "
  file = open(file_name, "w")                       # open(): Open a file, returns a file object.
except IOError:
  print "There was an error writing to", file_name
  sys.exit()                                        # exit(status=None): Exit the interpreter by raising SystemExit(status)
print "Enter '", file_finish, "' When finished"
file_text = ""
while file_text != file_finish:                     # loop statement: " while ... : "
  file_text = raw_input("Enter text: ")             # raw_input(): read string from stdin.
  if file_text == file_finish:                      # string equal with " == "
    file.close
    break
  file.write(file_text)                             # FileIO.write(): not all of the data may be written. The number of bytes actually written is returned
  file.write("\n")
file.close()                                        # FileIO.close(): may be called more than once without error


file_name = raw_input("Enter filename: ")
if len(file_name) == 0:                             # if statement: " if ... : "
                                                    # len(): Return the number of items of a sequence or mapping
  print "Next time please enter something"
  sys.exit()
try:
  file = open(file_name, "r")
except IOError:
  print "There was an error reading file"
  sys.exit()
file_text = file.read()     # FileIO.read(): read at most size bytes, returned as bytes.
                            #                Only makes one system call, so less data may be returned than requested
                            #                In non-blocking mode, returns None if no data is available.
                            #                On end-of-file, returns ''.
file.close()
print file_text


# ======================================================================
#       语法:
#          number & del
#          string, tuple, list
#          dict
#       功能：
#          互相转换

test_number = 123L
print "number = ", test_number
del test_number                                                 # delete the reference to a number object : 'del'
# print "after deleting reference, number = ", test_number      # 'test_number' is not defined

str = 'Hello World!'
print str
print str[0]
print str[2:5]          # string与数组的关系
print str[2:]
print str * 2           # 重复操作: "*"
print str + "TEST"      # 合并: "+"
str[1] == 'e'           # 数组化操作1 读单字符: "[x]"
str[7:-2] == 'orl'      # 数组化操作2 提取子串: "[..:..]"                # 字符串相等: '=='
str[8:] == 'rld!'       #            不指定结束下标
# len(str)              # 计算长度: "len()"


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list
print list[0]
print list[1:3]         # list的使用
print list[2:]
print tinylist * 2      # 打印两次
print list + tinylist   # 合并
list[3] == 2.23                   # 数组化操作1 读元素值: "[x]"
list[2:-1] == [2.23, 'john']      # 数组化操作2 读子列表: "[..:..]"       # list相等: '=='
list[3:] == ['john', 70.2]        #            不指定结束下标
del list[3]             # 删除item
list[2] = 2001          # 修改item
# ['Hi!'] * 4               # ['Hi!', 'Hi!', 'Hi!', 'Hi!'], 重复操作: "*"
# [1, 2, 3] + [4, 5, 6]     # [1, 2, 3, 4, 5, 6], 合并操作: "+"
# len([1, 2, 3])            # 计算长度: "len()"


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple[1:3]            # tuple的使用
print tuple[2:]
print tinytuple * 2         # 重复操作
print tuple + tinytuple     # 拼接操作
len(tuple) == 5             # 计算长度
# tuple[0] = 100            # will throw Error
del tuple                   # 删除整个tuple："del xxx"


dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"         # 数字 和 字符串 都可以为 key
print dict
print dict['one']
print dict[2]
print dict.keys()               # dict.keys()   key的集合
print dict.values()             # dict.values()   value的集合
dict['one'] = "number one"      # 修改某个key的value
del dict['Name'];               # 删除某个key和value
del dict ;                      # 删除整个dict


# int(x[,base]), long(x[,base]), float(x), complex(real[,imag])   # to number
#
# str(x)                  # object x -> string
#
# repr(x)                 # object x -> expression string   ???
# eval(str)               # Evaluates a string and returns an object.   ???
#
# tuple(s), list(s)       # sequence -> tuple / list
#
# set(s), frozenset(s)    # to set ???
#
# dict(d)                 # d must be a sequence of (key,value) tuples.   ???
#
# chr(x), unichr(x)       # integer -> character
# ord(x)                  # character -> integer
#
# hex(x)                  # integer -> hexadecimal string
# oct(x)                  # integer -> octal string




# ======================================================================

10.2//4 == 2.0        # Floor Division 向下取整除法 : "//"
10**2 == 100          # exponential (power) calculation 次方 : "**"


# 与C一致的操作：
#       比较操作, bit操作


# a and b, a or b, not (a and b)                    # Logical Operators 逻辑操作："and, or, not"


1 in [1,2,3] == True                                # Membership Operators : "in, not in"


ss='abc'; s1=ss; s2=ss; s1 is s2 == True         # Identity Operators : "is, is not"
                                                    # 与 “id(x) == id(y)” 一个效果
id(ss)                                             # 返回数据的内存地址



type(ss) == str                                           # 判断数据的类型 type()
isinstance(ss, str)                                       #              isinstance()

i=123; isinstance(i, int)==True
s='abc'; isinstance(s, str)==True
b=b'ACSII'; isinstance(b, bytes)==True

# >> 基础 Types in python:
# str                       # 由字符组成的不可更改序列
# bytes                     # 由字节组成的不可更改序列
# list, tuple               # 有序的
# set, frozenset            # 无序的，每个元素唯一
# dict
# int, float, complex
# bool

# >> 基础 types 之间的继承关系
# object
#     int
#         bool              # bool是一种int
#     long                  # long 与 int 同级别
#     float, complex
#     basestring            # basestring
#         str
#         unicode
#         bytes
#     list, tuple, dict
#     set, frozenset



# =======================================================================
# 语法：for ... in ... :
#
for letter in 'Python':                     # string
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']      # list
for fruit in fruits:
   print 'Current fruit :', fruit

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):            # number "range"
   print 'Current fruit :', fruits[index]
for num in range(10,20):                    # between [10, 20)
   print 'number :', num



# =======================================================================
# 数学函数 :
import math

# cmp(x, y)                   # will return 0, 1, -1

# abs(x), fabs(x)

# ceil(x), floor(x)           # 向上取整ceil，向下取整floor
# round(x[,n])                # 四舍五入取整
# modf(3.5) -> (0.5, 3.0)     # 取得数字的 整数部分 & 小数部分

# max(x1, x2,...), min(x1, x2,...)

# exp(x), log(x), log10(x), pow(x,y), sqrt(x)

# acos(x), asin(x), atan(x), atan2(y,x)
# cos(x), sin(x), tan(x)
# hypot(x,y), degrees(x), radians(x)


math.e          # mathematical constant 数学常量 e
math.pi         # mathematical constant 数学常量 pi 圆周率




# =======================================================================
# 随机函数 :
#     import random

# seed([x])                                 # x随意给，一般是时间秒数
#
# random()                                  # 随机一个[0,1)的浮点数
# uniform(x, y)                             # 随机一个[x,y)的浮点数
# randrange ([start,] stop [,step])         # 在给定的range中 随机选择一个整数
#
# choice(seq)                               # 在一个seqence(list, tuple, or string)中，随机选一项.
#
# shuffle(lst)                              # 就地随机一个list中的所有元素




# =======================================================================
# String：

print r'C:\\nowhere'        # C:\\nowhere           # raw string : "r ..."
print 'C:\\nowhere'         # C:\nowhere

print u'Hello, world!'                              # unicode string : "u ..."

# decode(encoding='UTF-8',errors='strict')
# encode(encoding='UTF-8',errors='strict')


print "My name is %s and weight is %d kg!" % ('Zara', 21)       # string formation : "%"
# %c	character
# %s	string conversion via str() prior to formatting
# %i	signed decimal integer
# %d	signed decimal integer
# %u	unsigned decimal integer
# %o	octal integer
# %x	hexadecimal integer (lowercase letters)
# %X	hexadecimal integer (UPPERcase letters)
# %e	exponential notation (with lowercase 'e')
# %E	exponential notation (with UPPERcase 'E')
# %f	floating point real number
# %g	the shorter of %f and %e
# %G	the shorter of %f and %E


# len(string)
#
# isalnum(), isdigit(),  isnumeric(), isdecimal()
# isspace()
# isalpha(), islower(), istitle(), isupper()
#
# upper(), title(), capitalize(), lower(), swapcase()
#
# strip([chars]), lstrip(), rstrip()
#
# center(width, fillchar)
# rjust(width,[, fillchar]), ljust(width[, fillchar])
# expandtabs(tabsize=8)
# zfill (width)
#
# find(str, beg=0 end=len(string))        # return index, -1 not found
# index(str, beg=0, end=len(string))      # same as find, but raises an exception if str not found.
# rfind(str, beg=0,end=len(string))       # Same as find(), but search backwards in string.
# rindex( str, beg=0, end=len(string))    # search backwards in string
# count(str, beg= 0,end=len(string))      # how many times str occurs in string or in a substring of string
# startswith(str, beg=0,end=len(string))      # Determines if string or a substring of string starts with substring str
# endswith(suffix, beg=0, end=len(string))    # Determines if string or a substring of string ends with suffix
#
# join(seq)
# replace(old, new [, max])       # Replaces all occurrences of old in string with new or at most max occurrences if max given.
# split(str="", num=string.count(str))    # Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
# splitlines( num=string.count('\n'))     # Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.
#
# max(str), min(str)
# maketrans(), translate(table, deletechars="")


# https://docs.python.org/2/library/string.html
print '{0}, {1}, {2}'.format('a', 'b', 'c')
print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')


# =======================================================================
# List：


# len(list)
#
# cmp(list1, list2)
#
# list(seq)       # tuple -> list
#
# max(list), min(list)


# list.count(obj)         # how many times obj occurs in list 元素重复次数
# list.index(obj)         # Returns the lowest index in list that obj appears 元素第一次出现位置
#
# list.append(obj)        # Appends object obj to list 加一个元素
# list.insert(index, obj) # Inserts object obj into list at offset index 插入一个元素
# list.remove(obj)        # Removes object obj from list 删除一个元素
# list.pop(obj=list[-1])  # Removes and returns last object or obj from list 提出最后一个或指定元素
#
# list.extend(seq)        # Appends the contents of seq to list 拼接一个sequence
#
# list.reverse()          # Reverses objects of list in place 就地反转list
# list.sort([func])       # Sorts objects of list, use compare func if given 对list进行排序


# =======================================================================
# Tuple：

tup1 = ();      # empty tuple
tup1 = (50,)    # tuple with only one element，注意 ","


# len(tuple)
#
# cmp(tuple1, tuple2)
#
# tuple(seq)      # list -> tuple
#
# max(tuple), min(tuple)


# =======================================================================
# Dict：

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict['Name']


len(dict)
#
# cmp(dict1, dict2)
#
str(dict)       # dict -> string
#
# type(variable)      # is dict?


# dict.has_key(key)

# dict.get(key, default=None)               # returns value or default if key not in dictionary
# dict.setdefault(key, default=None)        # will set dict[key]=default if key is not already in dict

# dict.clear()
# dict.copy()
# dict.update(dict2)                        # 合并

# dict.keys()                   # list of dictionary dict's keys
# dict.values()                 # list of dictionary dict's values

# dict.items()        -> [ ('Age', 7), ('Name', 'Zara'), ... ]
                                # list of dict's (key, value) tuple pairs

# dict.fromkeys( ('item1', 'item2') )        -> {'item2': None, 'item1': None}
# dict.fromkeys(('item1', 'item2'), 10)      -> {'item2': 10, 'item1': 10}




# =======================================================================
# Time

import time

ticks = time.time()     # [Ticks] : Number of ticks/seconds since the Epoch [12:00am, January 1, 1970] : "time()"

# [TimeTuple] : time as a tuple of 9 numbers
#                   year, month[1,12], day[1,31],
#                   hour[0,23], minute[0,59], second[0,61],
#                   day of week[0,6], day of year[1,366], daylight savings[-1,0,1]
# [struct_time] structure : same as [TimeTuple]
#                   tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst

utctime = time.gmtime(ticks)          # Ticks -> struct_time, with the UTC time. Note : t.tm_isdst is always 0
# time.gmtime([secs])
localtime = time.localtime(ticks)     # Ticks -> struct_time, with the local time (t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules).
# time.localtime([secs])

ticks = time.mktime(localtime)        # struct_time -> Ticks
ticks1 = calendar.timegm(utctime)     # struct_time -> Ticks, inverse of time.gmtime

print time.asctime( localtime )     # struct_time -> readable 24-character string, eg. 'Tue Dec 11 18:07:14 2008'.
# time.asctime([tupletime])
print time.ctime(ticks)             # Ticks -> readable 24-character string, eg. 'Tue Dec 11 18:07:14 2008'.
# time.ctime([secs])

struct_time = time.strptime("30 Nov 00", "%d %b %y")     # string -> struct_time, http://www.tutorialspoint.com/python/time_strptime.htm
# time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
print time.strftime("%b %d %Y %H:%M:%S", struct_time)          # struct_time -> string 自定义格式, http://www.tutorialspoint.com/python/time_strftime.htm
# time.strftime(fmt[,tupletime])

time.timezone == -36000             # the offset in seconds of the local time zone (without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).
time.altzone == -39600              # offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Only use this if daylight is nonzero.
time.tzname == ('AEST', 'AEDT')     # a pair of locale-dependent strings, which are the names of the local time zone without and with DST, respectively.
# time.tzset()                      # Resets the time conversion rules with environment variable TZ

cputime = time.clock()              # Cpu time, 线程自启动以来或从第一次调用clock()到现在的时间, 一般来讲测试程序耗时这个是最准确的

time.sleep(1)                       # 挂起线程，Suspends the calling thread for secs seconds.



import calendar

# calendar.isleap(year)             # leap year? 闰年
# calendar.leapdays(y1,y2)          # total number of leap days in the years within range(y1,y2).

print calendar.month(2008, 1)           # 输出格式化后的日历表
# calendar.month(year,month,w=2,l=1)    # multiline string with a calendar for month month of year year, one line per week plus two header lines.
# calendar.calendar(year,w=2,l=1,c=6)   # multiline string with a calendar for year year formatted into three columns separated by c spaces
# calendar.prcal(year,w=2,l=1,c=6)      # = calendar.calendar(year,w,l,c).
# calendar.prmonth(year,month,w=2,l=1)  # = calendar.month(year,month,w,l).
# calendar.setfirstweekday(weekday)      #??? 可能跟输出日历表时的起始weekday有关
# calendar.firstweekday()                #??? 同上， Returns the current setting for the weekday that starts each week.

# calendar.weekday(year,month,day)      #
calendar.weekday(2015,11,1) == 6        # 6是周日，日期与周的关系

# calendar.monthcalendar(year,month)    # a list of lists of ints. Each sublist denotes a week. Days outside month month of year year are set to 0; days within the month are set to their day-of-month, 1 and up.
calendar.monthcalendar(2015,11)         # 月份与星期的int数组关系表
    # [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 0, 0, 0, 0, 0, 0]]

ticks1 = calendar.timegm(utctime)     # struct_time -> Ticks, inverse of time.gmtime



# Other Modules:
# The “datetime” Module, http://docs.python.org/library/datetime.html#module-datetime
# The “pytz” Module, http://www.twinsun.com/tz/tz-link.htm
# The “dateutil” Module, http://labix.org/python-dateutil




# =======================================================================
# Function
#
# def functionname( parameters ):                   # 一般函数定义
#    "function_docstring"
#    function_suite
#    return [expression]
#
# def functionname([formal_args,] *var_args_tuple ):        # 可变参函数定义
#    "function_docstring"
#    function_suite
#    return [expression]


# All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.
# Python中所有都是入参都是 引用reference. 所以注意在函数中是可以修改入参的，谨慎


# A return statement with no arguments is the same as return None.
# 不明确写return语句时，返回None；有return语句但没有参数时，也返回None

def mindatapos( a, s, e ) :
    if e<=s :
        return 0, -1;
    minvar = a[s]
    minpos = s
    for i in range(s+1,e) :
        if a[i] < minvar :
            minvar = a[i]
            minpos = i
    return minvar, minpos                             # 返回多个参数

def maxdatapos( a, s, e ) :
    if e<=s :
        return 0, -1;
    maxvar = a[s]
    maxpos = s
    for i in range(s+1,e) :
        if a[i] > maxvar :
            maxvar = a[i]
            maxpos = i
    return maxvar, maxpos                             # 返回多个参数



def printinfo( name, age = 35 ):                      # 参数默认值
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return

printinfo("Liang")                                    # 使用 一般调用方式
printinfo( name = "Yezi")                             # 使用 Keyword arguments 调用方式



def printinfo1( arg1, *vartuple ):                    # 可变长参数
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

printinfo1( 10 )
printinfo1( 70, 60, 50 )



# Anonymous Functions
#   lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2;                 # Lambda 表达式
print "Value of total : ", sum( 10, 20 )



# Global vs. Local variables : Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
# 函数中定义的变量就只有 函数作用域
# http://blog.csdn.net/vipygd/article/details/7797778

total = 0; # This is global variable.

def sum( arg1, arg2 ):
   # print "Inside the function global total : ", total         # 会得到UnboundLocalError异常，因为total已经在下面定义了
   total = arg1 + arg2; # Here total is local variable.         # 注意：这是定义！！！不是赋值，只要有＝号，total就变为local变量了
   print "Inside sum function local total : ", total
   return total;

def sum1( arg1, arg2 ):
   global total                                                 # 使用global关键字声明使用全局变量: "global"
   total = arg1 + arg2                                          # 注意：这是赋值！！！不是定义，因为global关键字
   print "Inside sum function global total : ", total

sum(10,20); print total                                                 # => 0
sum1(10,20); print total                                                # => 30





# =======================================================================
# Modules
#
# import module1[, module2[,... moduleN]
#
# from modname import name1[, name2[, ... nameN]]       # import specific attributes from a module
# from modname import *
#

# Module搜寻逻辑
# 1. current directory
# 2. PYTHONPATH
# 3. /usr/local/lib/python/


# dir()         # built-in function, returns a sorted list of strings containing the names defined by a module.
                # 返回module中的所有 属性名称，函数名称 。。。
import math; dir(math)


# help()        # python的内建函数, 返回传入的module的详细使用说明
                # 非常有用~~~!!!!!
help(math)



locals()
#               it called from within a function,
#               it will return a dict with all variables/methods that can be accessed locally from that function.

globals()
#               it called from within a function,
#               it will return a dict with all variables/methods that can be accessed globally from that function.


# When the module is imported into a script, the code in the top-level portion of a module is executed only once.
# if you want to reexecute the top-level code in a module, you can use the reload() function.
# 模块中top-level code仅仅在模块被加载时执行一次；
# 有必要的话，使用reload函数可以再加载一次
#
# reload(xxx)          # imports a previously imported module again
reload(math)



# =======================================================================
# Package

# A package is a hierarchical file directory structure

# === 'Phone' Package ===
# Phone/Pods.py file haveing function Pods()
# Phone/Isdn.py file having function Isdn()
# Phone/G3.py file having function G3()
#
# Phone/__init__.py
#     from Pots import Pots
#     from Isdn import Isdn
#     from G3 import G3
#
# === use 'Phone' Package ===
# import Phone
#
# Phone.Pots()
# Phone.Isdn()
# Phone.G3()




# =======================================================================
# I/O


inputs = raw_input()       # inputs -> string

# input()           # inputs -> valid Python expression, will returns the evaluated result to you.
str = input("Enter your input: ");
print "Received input is : ", str
    # Enter your input: [x*5 for x in range(2,10,2)]
    # Recieved input is :  [10, 20, 30, 40]



# file object = open(file_name [, access_mode][, buffering])
#               mode: r(只读), rb, r+(读写), rb+(二进制读写)
#                     w(只写), wb, w+(读写), wb+
#                     a, ab, a+, ab+
#               buffering:
#                       0       no buffer
#                       1       line buffering
#                       x>1     buffer with size x
#                       <0      system default
file = open('a.txt', 'r+')

file.closed                 # is closed?
file.mode                   # which mode?
file.name                   # file name
file.softspace              # ???

file.tell()                     # get file position，文件读写指针位置

file.write("content to write")  #

# file.read([count=-1])
file_content = file.read()      #



import os

os.rename('a.txt', 'new_name.txt')              # 文件重命名
os.remove('a.txt')                              # 删除文件

os.mkdir("newdir")
os.chdir("newdir")
os.rmdir('dirname')                               # 文件夹操作

os.getcwd()                                       # 当前工作目录



# Other Modules
#   http://www.tutorialspoint.com/python/file_methods.htm
#   http://www.tutorialspoint.com/python/os_file_methods.htm





# =======================================================================
# exceptions
# assert(...)
# rails(...)
# try ... except ... else ... finally ...
#

# BaseException       # Base class for all exceptions
#     KeyboardInterrupt   # user interrupts program execution, usually by pressing Ctrl+c
#     SystemExit          # sys.exit()
#     Exception           # Common base class for all non-exit exceptions
#         StopIteration       # Signal the end from iterator.next()
#         StandardError       # Base class for all standard Python exceptions that do not represent interpreter exiting.
#             ArithmeticError     # Base class for arithmetic errors.
#                 OverflowError
#                 FloatingPointError
#                 ZeroDivisionError
#             AssertionError      # Assertion failed.
#             AttributeError      # in case of failure of attribute reference or assignment.
#             EOFError            # no input from either the raw_input() or input() function and the end of file is reached.
#             ImportError         # can't find module, or can't find name in module
#             LookupError
#                 IndexError
#                 KeyError
#             NameError           # Name not found globally.
#                 UnboundLocalError   # Local name referenced but not bound to a value.
#             EnvironmentError    # Base class for I/O related errors.
#                 IOError
#             SyntaxError         # Invalid syntax.
#                 IndentationError
#             ValueError          # Inappropriate argument value (of correct type)
#             RuntimeError        # Unspecified run-time error.
#                 NotImplementedError # Method or function hasn't been implemented yet.
#             SystemError         # Internal error in the Python interpreter.


# assert Expression[, Arguments]
assert (-1 >= 0),"impossible here, Colder than absolute zero!"



# try:
#    You do your operations here;
#    ......................
# except:
#    If there is any exception, then execute this block.        # 有任何异常时都会来这里
#    ......................
# else:
#    If there is no exception then execute this block.


# try:
#    You do your operations here;
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.               # 分类捕获异常
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# except(Exception1[, Exception2[,...ExceptionN]]]):                # 归类捕获异常
#    If there is any exception from the given exception list,
#    then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.          #注意是：try中的code没有抛出任何异常时，会执行此处code
#                                                                       如果有异常抛出，不论被捕获还是未被捕获，此处code都不会执行


# try:
#    ...
# finally:                                                      # 无论是否有异常抛出，始终会被执行
#    This would always be executed.


# try:
#    fh = open("testfile", "w")
#    try:                                                               # try的嵌套
#       fh.write("This is my test file for exception handling!!")
#    finally:
#       print "Going to close the file"
#       fh.close()
# except IOError:
#    print "Error: can\'t find file or read data"


# def temp_convert(var):
#    try:
#       return int(var)
#    except ValueError, Argument:                                       # 异常中带入 参数，不同异常参数个数类型可能不同???
#       print "The argument does not contain numbers\n", Argument
#
# temp_convert("xyz");         # invalid literal for int() with base 10: 'xyz'




# raise [Exception [, args [, traceback]]]              # raise 一个异常
#     Exception is the type of exception (for example, NameError) and argument is a value for the exception argument.
#
#
#     An exception can be a string, a class or an object.
#       Most of the exceptions that the Python core raises are classes, with an argument that is an instance of the class.
# -== Example 1 异常可以时一个字符串，一个class，或一个object
raise "Invalid level!", level
#
#
#     Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions.
# -== Example 2 自定义异常
#
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args


