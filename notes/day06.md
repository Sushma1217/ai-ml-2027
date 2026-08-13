ndim - return the number of dimensions
shape - attribute returns a tuple of integers that represents the number of elements in each dimension of an array
(rows,cols)
size - in NumPy counts the total number of elements(same for 2d array as well it will count and return the count)
dtype (short for data type) is an object that defines the exact type, size, and layout of data elements stored in an array.

Vectorization is a technique used to perform operations on entire arrays at once instead of iterating through elements using Python loops. It improves performance by using optimised implementations provided by libraries such as NumPy.

last number accessing -
negative slicing syntax: array[-3:]
which means from the last 3 numbers

slicing :: - syntax
is the extended slicing syntax used to extract specific elements from sequences like lists, strings, or tuples. It separates the start, stop, and step values inside the index brackets: sequence[start:stop:step]

When you omit the start and stop values but include the step value (e.g., [::step]),

:- all the rows

axis=1 (NumPy): Operates row by row (calculates stats for each student across subjects).

axis=0 (NumPy): Operates column by column (calculates stats for each subject across all students).

np.argmax()- returns the index or indices of the maximum values along a specified axis

The enumerate() function in Python is used to iterate over an iterable while keeping track of both the index and the value.

where- to find indices of elements that meet a condition or to conditionally replace values in an array.

What is NumPy?
a open source library allows vectorization and faster, cleaner to work with data set
array- collection of elements, fixed memory size

Vectorization- intead of iternating using loops when we work with huge dataset, we can use numpy a simple library which saves time, uses optimized code, less num of lines(cleaner)

NumPy vs Python list
numpy - easy way, less and cleaner code as we have many predefined methods which mainly eleminates the loops, manual calculation etc
python list- main differece is more number of code, loops, takes time

Why do you think ML libraries prefer arrays/matrices rather than ordinary Python lists?
less execution time(fast)
easy to process or perform operation on large set of data
optimized code
no loops

What took you the longest?
numpy method to search, understand as there are many

interview questions
What is NumPy?
Python list vs NumPy array?
What is vectorization?
What does shape mean?
What does ndim mean?
What is a 2D array?
What is the difference between array.size and array.shape?
Why is NumPy useful in ML?
