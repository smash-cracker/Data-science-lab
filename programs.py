import numpy as np
# elementwise comparison of 2 given arrays (>, >= , <, <=)

x = [3, 5,6]
y = [2, 5,7]
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))


# array of all even integers from 30 to 70
evenArray = np.arange(30,50,2)
print("Array\n",evenArray)


# 3*3 identity matrix
id = np.identity(3)


# create a vector with values from 0 to 20 and change sign of numbers in the range from 9 to 15
a = np.arange(21)
for i,x in enumerate(a):
    print(i)
    if x >=9 and x<=15:
        a[i]=-x
print(a)


# create 5*5 zero matrix with elements on the main diagonal = 1,2,3,4,5

z = np.zeros([5,5],dtype=int)
np.fill_diagonal(z,[1,2,3,4,5])
print(z)

# numpy program to computer sum of all elements, column, row
sumArray = np.random.randint(20,size=(3,3))
print("Array\n",sumArray)
columnArray = np.sum(sumArray,axis=0) #column
for i,x in enumerate(columnArray):
    print("sum of column", i+1," is",x)
rowArray = np.sum(sumArray,axis=1) #row
for i,x in enumerate(rowArray):
    print("sum of row", i+1," is",x)
print("sum of elements",np.sum(sumArray)) #elements


# save a given array to a text file and load it
textArray = np.random.randint(20,size=(3,3))
np.savetxt("file.txt",textArray,fmt="%.d")
np.loadtxt("file.txt",dtype="int")

# check whether 2 arrays are equal or not (elementwise)
array1 = np.random.randint(1,size=(3,3))
array2 = np.random.randint(1,size=(3,3))
np.array_equal(array1,array2)


# create 4*4 arrays with randow values. create new array swapping 1st and last rows
array1 = np.random.randint(5,size=(4,4))
array1[[3,0]]=array1[[0,3]]
print(array1)

# element wise multiplication

array1 = np.random.randint(5,size=(3,3))
array2 = np.random.randint(5,size=(3,3))
print("element wise multiplication\n")
array3 = np.multiply(array1,array2)
