#coding=utf-8

import numpy as np


# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html



# np.array.dtype

# np.array.dtype.name




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

print np.zeros( (3,4) )
# array([[ 0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.]])

print np.ones((2,3), dtype=int)
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




# ================================= np.array运算，Basic Operations

a = np.array( [20,30,40,50] )
b = np.arange( 4 )  # array([0, 1, 2, 3])

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

a.min()
a.max()





# ================================= Universal Functions

B = np.arange(3)
np.exp(B)                                       # 常见数学函数 ...
np.sqrt(B)

C = np.array([2., -1., 4.])
np.add(B, C)                                    # 集合加法 np.add()，似乎与 B+C 无异




# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where







# ================================= Indexing, Slicing and Iterating

a = np.arange(10)

a[2:5]
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
a[ : :-1]          # reversed a

for i in a:
    print(i)

i = np.array( [ 1,3,8,5 ] )             # an array of indices
a[i]                                    # -> array([ 1,  1,  9, 64, 25])

a = np.arange(5); a[[1,3,4]] = 0                          # -> array([0, 0, 2, 0, 0])
a = np.arange(5); a[[0,0,2]]=[1,2,3]                      # -> array([2, 1, 3, 3, 4])
a = np.arange(5); a[[0,0,2]]+=1                           # -> array([1, 1, 3, 3, 4])

a = np.arange(5)
b = a>2                                 # b被用来筛选a中的元素
a[b]                                    # -> array([3, 4])


# Indexing, Indexing (reference), newaxis, ndenumerate, indices





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




