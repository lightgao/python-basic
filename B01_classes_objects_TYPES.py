#!/usr/bin/python
#coding=utf-8


# ======= Python Basic Tutorial
# http://www.tutorialspoint.com/python/index.htm





# ================== Creating Class & Creating Instance Object

class Employee:
   'Common base class for all employees'
   empCount = 0                                         # [public class variable], can be accessed with "Employee.empCount" inside or outside
   __secretCount = 0                                    # [private class variable]

   def __init__(self, name, salary):                    # [class constructor or initialization method]
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):                              # [normal class methods] the first argument to each method is "self". but you do not need to include it when you call the methods.
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary    # [instance variable] self.xxx


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)                                   # create [instance object]
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

assert ( hasattr(Employee, '__secretCount')==False )         # invisible







# ================== Accessing Attributes
emp1.age = 7                                                    # [attributes of objects] can be add, remove, or modify at any time
del emp1.age
assert( hasattr(emp1, 'age') == False )                         # [hasattr(obj, name)], check if an attribute exists or not.

Employee.empCount = 0                                           # [attributes of classes] can be add, remove, or modify at any time
del Employee.empCount
assert( hasattr(Employee, 'empCount') == False )                # [hasattr(class, class variable)]

# getattr(obj, name[, default])                             # 动态读取或调整 object 或 class(也是一种object) 属性的方法
# hasattr(obj,name)                                             # [ has / get / set / del ]  attr ...
# setattr(obj,name,value)
# delattr(obj, name)




# ================== Class内建属性（Built-In Class Attributes
print "Employee.__doc__:", Employee.__doc__                     # Class documentation string or none, if undefined.
print "Employee.__name__:", Employee.__name__                   # Class name.
print "Employee.__module__:", Employee.__module__               # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print "Employee.__bases__:", Employee.__bases__                 # possibly empty tuple containing the base classes
# print "Employee.__class__:", Employee.__class__               #
print "Employee.__dict__:", Employee.__dict__                   # Dictionary containing the class's namespace.






# ================== Destroying Objects (Garbage Collection)

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):                                       # [ class destructor ], __del__
      class_name = self.__class__.__name__
      print class_name, "destroyed"

pt1 = Point()               # Increase ref.
pt2 = pt1                   # Increase ref.
pt3 = pt1                   # Increase ref.
del pt1                     # Decrease ref.
del pt2                     # Decrease ref.
del pt3                     # Decrease ref. __del__ will be called




# ================== Class Inheritance & Overriding Methods

# class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite

class Parent(object):        # define parent class
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def hello(self):
      print 'Hello from parent!'

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

   def hello(self):
      print 'Hello from child!'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.hello()            # child calls overridden method



# ====================== Generic functionality can be overridden in sub classes
# __init__ ( self [,args...] )        # constructor, obj = classname()
# __del__( self )                     # destructor, del obj
# __repr__( self )                    # ？？？ evaluatable string representation, repr(obj)
# __str__( self )                     # 字符串化 Printable string representation, str(obj)
# __cmp__ ( self, x )                 # 对象比较 Object comparison, cmp(obj, x)
# __add__(self,other)                 # +操作符重载



# ====================== Check Inheritance & Instantiation
#
# issubclass(sub, sup)
assert ( issubclass(Child, Parent)==True )
assert ( issubclass(Child, object)==True )
#
# isinstance(obj, Class)
assert ( isinstance(c, Child)==True )
assert ( isinstance(c, Parent)==True )
#





# http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html
# http://blog.csdn.net/cpp_chen/article/details/17146649

# There are two kinds of objects in Python:
#     Type objects - can create instances, can be subclassed.
#     Non-type objects - cannot create instances, cannot be subclassed.
# <type 'type'> and <type 'object'> are two primitive objects of the system.
#
# objectname.__class__ exists for every object (type or non-type) and points the type of the object.
# objectname.__bases__ exists for every type object and points the superclasses of the object. It is empty only for <type 'object'>.
#
#
#
# Python里面只有两种类型： type object(有 实例&子类), non-type object(无 实例&子类)
#
# objectname.__class__ 可查看 type & non-type object 的 type信息, 与 type(objectname) 作用一样
#       所有type object的type信息始终是<type 'type'>
#       non-type object的type信息则是实例化该object的type object
c = Child()
print c.__class__
print Child.__class__

# objectname.__bases__ 可查看 type object 的 parent信息
#       只有type object才有 继承概念
print Parent.__bases__
print Child.__bases__







# “object + type + function + 基础类型(int,list...)" 一起 为用户构建其它复杂领域提供支持
#           object高度抽象 是 用户构建其它领域的根本
#           type 是 让计算机理解用户领域的接口
#           function 是 让计算机操作用户领域实例的接口
#           基础类型(int,list...) 是 从数学理论而来的，可用于描述用户领域中任何type的基础常用types
#

# type是一种object
#       class 是 type 的实例
# function也是一种object
#       def 是 function 的实例

object.__bases__
type.__bases__

object.__class__ == type(object)


# object
# type                      # 继承自 object
# int, float, list ...      # type为‘int/float/...‘的object
# function                  # type为‘function’的object


# 描述空间维度 用 组合        --> non-type object （客观域／目标域）
# 描述时间维度 用 函数行为     |
#
# 描述抽象维度 用 继承        -> type object     （抽象域）
#
# 实例化(non-type object) 是在 目标抽象级别 上的现实投影，该级别是 组合&函数 发挥作用的场地（即程序运行时，真正的现实作用都是由non-type object完成的；所以说思维是跨越时间与空间的法宝）
# 目标领域的type objects 都是在做 基础抽象级别 与 目标抽象级别 的跨越时产生的 思维中间抽象物；
#       计算机需要这些中间抽象物来操作和管理non-type object，人也需要这些中间抽象物来做该问题领域的沟通交流


# 模糊？？？：螺旋上升，量变到质变，函数式编程，自类型，对象突破，实例繁殖，目标驱动／行为自建／实例繁衍／类型推导


# 类型：包含了 数据结构和行为定义
#
# 软件之所以不能智能的原因是，软件运行起来后，软件中类型系统中类型的种类和数量是永远不会变的，而对象系统中的数量是可以变得，但种类依然受类型所控制不能改变
# 函数式编程，部分实现了类型推导的功能，推导出的类型都是已知类型的组合或子集
#
# 软件之所以整体呈现智能，是因为人脑作为了丰富类型系统的工具；人因为有学习能力，自身的类型系统是不断增加的；
# 学习的根本动力源是对原始欲望的追求，过程则是一系列正向反向的刺激












































# check if a variable exists in Python?
# http://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists-in-python
#
# To check the existence of a local variable:
#
# if 'myVar' in locals():
#   # myVar exists.
# To check the existence of a global variable:
#
# if 'myVar' in globals():
#   # myVar exists.
# To check if an object has an attribute:
#
# if hasattr(obj, 'attr_name'):
#   # obj.attr_name exists.





# stat -f %Sm -t %Y%m%d-%H%M%S ./-622800265
# for i in *; do echo "./$i" "`stat -f %Sm -t %Y%m%d-%H%M%S ./$i`"; done
# for i in *; do mv -v "./$i" "`stat -f %Sm -t %Y%m%d-%H%M%S ./$i`"; done

# jhead -n%Y%m%d-%H%M%S ./*






# 对规律的把握无需尽善尽美，明确预期，把握住与预期相关的部分关键规律，就可以引导事物朝向预期

# 正确的规律也可能由于无法帮助大部分人达成预期而遭到误判 ／ 任何规律的正确定都是在一定的限定条件下的

