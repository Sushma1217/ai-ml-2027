# Day 8 — Pandas

## Mental model

What is a DataFrame?
collection of data, combo of num and string with rows and cols

## DataFrame vs NumPy array

## shape

returns num of row,col - eg(4,3)

## columns

returns col names with dtype - format ([])

## dtypes

tyeps of the col

## info

basically an overview i think
col names
index
null data count for each col
dtype of the col
memory usage

## describe

col wise mathematical data like mean, std, max, 50%, 25%, 75%

<!--  -->

passing list or selecting the >1 col we will use [a,b]- wrapping

## Filtering

iloc- to extract the rows in dataframe
numbers only,
multiple rows we can filter
df.iloc[row_number, column_number]
Slicing rows - [star,end]

## Sorting

sort_values() - sort col, default val is ascending
syntax - df.sort_values(by='column_name')

we have sort by index too - df.sort_index(axis=0)

size - Counts rows (total number of elements/items, regardless of columns or missing data).count()
Count()- valid values per column (excluding NaN / null values).

## What confused me

nothing much- asusual syntax
size vs count - bit

## What became easier

filtering
bool masking

## AI/ML connection

practicing wiht real data set, filering, grouping, bool masking to get the results based on the condition

## Interview questions
