#coding=utf-8

import numpy as np


# http://docs.scipy.org/doc/
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html





# ================================= Types in Numpy



# There are 5 basic numerical types representing booleans (bool), integers (int), unsigned integers (uint) floating point (float) and complex.
# Those with numbers in their name indicate the bitsize of the type (i.e. how many bits are needed to represent a single value in memory).
# Some types, such as int and intp, have differing bitsizes, dependent on the platforms (e.g. 32-bit vs. 64-bit machines).
# This should be taken into account when interfacing with low-level code (such as C or Fortran) where the raw memory is addressed.
#   >>> 五大基本类型: bool_, int_, uint, float_, complex_
#   >>> bool_, int_, uint, float_, complex_所占的bit数已经有numpy控制；但是其它如intp/intc所占bit数，则是受具体的系统平台影响

np.bool_.__bases__      # -> (<type 'numpy.generic'>,)
np.generic.__bases__    # -> (<type 'object'>,)
# bool_ ~  generic  ~  object

np.int_.__bases__           # -> (<type 'numpy.signedinteger'>, <type 'int'>)
np.signedinteger.__bases__  # -> (<type 'numpy.integer'>,)
np.integer.__bases__        # -> (<type 'numpy.number'>,)
np.number.__bases__         # -> (<type 'numpy.generic'>,)
np.generic.__bases__        # -> (<type 'object'>,)
# int_  ~  signedinteger + python int  ~  integer  ~  number  ~  generic  ~  object

# 更多类型的继承关系 看下面


#
# ---- Basic types : http://docs.scipy.org/doc/numpy/user/basics.types.html
#
# bool_	    Boolean (True or False) stored as a byte
#
# int_	    Default integer type (same as C long; normally either int64 or int32)
# intc	    Identical to C int (normally int32 or int64)
# intp	    Integer used for indexing (same as C ssize_t; normally either int32 or int64)
# int8	    Byte (-128 to 127)
# int16	    Integer (-32768 to 32767)
# int32	    Integer (-2147483648 to 2147483647)
# int64	    Integer (-9223372036854775808 to 9223372036854775807)
# uint8	    Unsigned integer (0 to 255)
# uint16	Unsigned integer (0 to 65535)
# uint32	Unsigned integer (0 to 4294967295)
# uint64	Unsigned integer (0 to 18446744073709551615)
#
# float_	Shorthand for float64.
# float16	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
#
# complex_	    Shorthand for complex128.
# complex64	    Complex number, represented by two 32-bit floats (real and imaginary components)
# complex128	Complex number, represented by two 64-bit floats (real and imaginary components)
#

# ----------------- numpy实现的 types，以及别名
# void: void0, Void0, V,
#
# object_: object, object0, Object0, O, O8,
#
# string_: str_, string_, bytes_, str, string, string0, String0, S, a,
# unicode_ : unicode, unicode0, Unicode0, U,
#
# bool_: bool, bool8, Bool, b1, ?,
#
# int8: byte, Int8, i1, b,
# int16: short, Int16, i2, h,
# int32: Int32, intc, i4, i,
# int64: int_, int, int0, intp, Int64, longlong, i8, q, L, P, l, p,
#
# uint8: ubyte, UInt8, u1,  B,
# uint16: ushort, UInt16, u2, H,
# uint32: uintc, UInt32, u4, I,
# uint64: uint, uint0, uintp, ulonglong, UInt64, u8, Q,
#
# float16: half, Float16, f2, e,
# float32: single, Float32, f4, f,
# float64: float_, float, double, Float64, f8, d,
# float128: longfloat, longdouble, Float128, f16, g,
#
# complex64: singlecomplex, Complex32, csingle, c8, F,
# complex128: complex_, complex, Complex64, cfloat, cdouble, c16, D,
# complex256: longcomplex, Complex128, clongfloat, clongdouble, c32, G,
#
# datetime64: datetime_, Datetime64, d8, M8[us], m8[us], M,
#
# timedelta64: timedelta_, Timedelta64, t8, m,
#

# ----------------- numpy 中 types 之间的继承关系。
#                   可以使用 np.issubdtype(A, B) 判断继承关系
#                           http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#arrays-scalars-built-in
# [generic]
#     object_
#     bool_
#     [number]
#         [integer]
#             [unsignedinteger]
#                 uint8, uint16, uint32, uint64
#             [signedinteger]
#                 int8, int16, int32
#                 int64 *
#                 [timeinteger]
#                     datetime64
#                     timedelta64
#         [inexact]
#             [floating]
#                 float16, float32, float128
#                 float64 *
#             [complexfloating]
#                 complex64, complex256
#                 complex128 *
#     [flexible]
#         void
#         [character]
#             string_ *
#             unicode_ *
# 上表 * 表示: 在我测试的计算机上，numpy使用了python内建的类型，而非自己的numpy实现

# 》》 using python build-in types
# float
# long
# str
# int
# bool
# complex,
# unicode,

np.issubdtype(np.int32, np.integer) == True                             # numpy 自己实现的subdtype判断
np.issubdtype(np.float32, np.integer) == False
np.issubdtype(np.complex64, np.integer) == False
np.issubdtype(np.uint8, np.integer) == True
np.issubdtype(np.bool, np.integer) == False
np.issubdtype(np.void, np.integer) == False




# ------------------ numpy中的 数组类型ndarray，数组 元素类型dtype
# [python object]
#     ndarray
#     dtype

type(np.dtype)        # -> <type 'type'>
np.dtype.__bases__    # -> (<type 'object'>,)

type(np.ndarray)        # -> <type 'type'>
np.ndarray.__bases__    # -> (<type 'object'>,)


# 虽然 dtype 和 numpy中的types 没有直接继承关系，但是numpy自己认为所有types都归属于dtype概念下
issubclass(np.float32, np.dtype) == False       # 没有直接继承关系
np.issubdtype(np.float32, np.dtype) == True     # numpy认为所有types都归属于dtype概念下
np.issubdtype(np.int64, np.dtype) == True

    # Data type objects (dtype)
    # http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types

    # Numpy numerical types are instances of dtype (data-type) objects, each having unique characteristics.
    #   >>> dtype 所有numpy中type的原形，我们也可以用它自定义类型；包含了bit-width and its byte-order





# ------------------  各种创建 numpy 类型的方式

x = np.float32(1.0)             # python float -> numpy float32

y = np.int_([1,2,4])            # python list -> numpy list with int_ dtype

a = np.array([1,2,3])           # python list -> numpy list
a.dtype                         # dtype('int64')
a.dtype.name == 'int64'
b = np.array([1,2,3], dtype='float')    # python list -> numpy list with float dtype
b.dtype                                 # dtype('float64')
b1 = np.array([1, 2, 3], dtype='f')

c = a > 1;  c.dtype     # dtype('bool')     # numpy list with bool_ dtype

z = np.arange(3, dtype=np.uint8)          # int8
fz = z.astype(float)                      # float, z本身不改变
iz = np.int16(z)                          # int16, z本身不改变

















# ================================= 得到np.array，Array Creation

# Create an array from a regular Python list or tuple using the array function.                 从list或tuple创建np.array
# The type of the resulting array is deduced from the type of the elements in the sequences.    np自推导元素类型

a = np.array([2,3,4])
print a.dtype             # dtype('int64')

b = np.array([1.2, 3.5, 5.1])
print b.dtype             # dtype('float64')




# array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.

b = np.array([(1.5,2,3), (4,5,6)])      # array([[ 1.5,  2. ,  3. ], [ 4. ,  5. ,  6. ]])




# function zeros creates an array full of zeros,                函数 zero()
# the function ones creates an array full of ones,              函数 ones()
# and the function empty creates an array whose initial content is random and depends on the state of the memory.       函数 empty()
# By default, the dtype of the created array is float64.        创建的数组元素类型都是float64

print np.zeros( (3,4) )                             # 默认得到元素类型为float64
# array([[ 0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.]])

np.zeros(6, dtype=np.uint16)
# array([0, 0, 0, 0, 0, 0], dtype=uint16)

print np.ones((2,3), dtype=int)                     # 但可以用dtype指定元素类型为int
# array([[1, 1, 1],
#        [1, 1, 1]])




# create sequences of numbers, NumPy provides a function analogous()
# but it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. linspace() provided
#   函数analogous() 和 linspace() , 代替Python中的range

print np.arange( 0, 2, 0.3 )
# array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])

print np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
# array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])





# array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, numpy.random.rand, numpy.random.randn, fromfunction, fromfile




# ================================= np.array运算，Basic Operations, Universal Functions

a = np.array( [20,30,40,50] )
b = np.arange( 4 )  # array([0, 1, 2, 3])

a.size == 4                                     # array的长度


c = a-b                                         # -> array([20, 29, 38, 47])
d = b**2                                        # -> array([0, 1, 4, 9])
a<35                                            # -> array([ True, True, False, False], dtype=bool)
10*np.sin(a)                                    # -> array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])

a+=b
print a                                         # -> array([20, 31, 42, 53])



a = np.random.random((2,3))                     # 随机数
# array([[ 0.18626021,  0.34556073,  0.39676747],
#        [ 0.53881673,  0.41919451,  0.6852195 ]])

a.sum()                                         # -> 2.5718191614547998

a.max()                     # return max value
np.max(a)

a.argmax()                  # return index of the max value
np.argmax(a)


B = np.arange(3)
np.exp(B)                                       # 常见数学函数 ...
np.sqrt(B)

C = np.array([2., -1., 4.])
np.add(B, C)                                    # 集合加法 np.add()，似乎与 B+C 无异



np.shape(C) == C.shape              # array 的shape属性 & shape方法; 用看查看是几维数组

# np.reshape()
# np.resize()



a = np.array([2, 3, 3, 0, 1, 4, 2, 4])
c, idx = np.unique(a,return_index=True)                 # numpy.unique()
    # c -> array([0, 1, 2, 3, 4])
    # idx -> array([3, 4, 0, 1, 5])（元素出现的起始位置）



# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where







# ================================= Indexing, Slicing and Iterating


a = np.arange(10)

a[2:5]
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
a[1:7:2]           # -> array([1, 3, 5])
a[ : :-1]          # reversed a


for i in a:
    print(i)

a = np.arange(5); a[[1,3,4]] = 0                          # -> array([0, 0, 2, 0, 0])
a = np.arange(5); a[[0,0,2]]=[1,2,3]                      # -> array([2, 1, 3, 3, 4])
a = np.arange(5); a[[0,0,2]]+=1                           # -> array([1, 1, 3, 3, 4])


#-------- Indexing arrays (indices), Boolean / “mask” index arrays

indices = np.array( [ 1,3,8,5 ] )             # an array of indices
a[indices]                                    # -> array([ 1,  1,  9, 64, 25])

a = np.arange(5)
b = a>2                                 # b将被用来筛选a中的元素
a[b]                                    # -> array([3, 4])



#------- multiple dimensional array indexing

x = np.arange(10)
x.shape = (2,5)     # now x is 2-dimensional, array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
x[0][2] == x[0,2] == 2
x[0]    # [0, 1, 2, 3, 4]






# Indexing, Indexing (reference), newaxis, ndenumerate, indices




# ================================= Sorting & Equality & Empty checking


x = np.array([99, 12, 83, 45])
y =  np.sort(x)                     # => array([12, 45, 83, 99])    sort() 返回排序后的数组
i = np.argsort(x)                   # => array([1, 3, 2, 0]),       argsort() 返回排序后的下标
np.array_equal(y,x[i])              # numpy中判断 array相等          array_equal(,)

e = np.array([])
e.size == 0                         # use .size to check empty




# ================================= Copies and Views

a = np.arange(12)

b = a                   # no new object is created
b is a == True          # a and b are two names for the same ndarray object

c = a.view()
c is a == False
c.base is a == True                   # c is a view of the data owned by a
c.flags.owndata == False

d = a.copy()                          # a new array object with new data is created
d is a == False
d.base is a == False                  # d doesn't share anything with a


x = np.arange(0, 50, 10)        # -> array([ 0, 10, 20, 30, 40])
x[np.array([1, 1, 3, 1])] += 1  # -> array([ 0, 11, 20, 31, 40])
# Where people expect that the 1st location will be incremented by 3. In fact, it will only be incremented by 1. The reason is because a new array is extracted from the original (as a temporary) containing the values at 1, 1, 3, 1, then the value 1 is added to the temporary, and then the temporary is assigned back to the original array. Thus the value of the array at x[1]+1 is assigned to x[1] three times, rather than being incremented 3 times.
