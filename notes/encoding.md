# Day 18 — Categorical Encoding

## 🎯 Why are we learning this?

ML models generally work with numerical representations, but real-world datasets contain categories such as "Fiber optic" or "Month-to-month". Encoding converts those categories into usable numerical features without accidentally changing their meaning.

## What problem does encoding solve?

Encoding solves the fundamental problem of translation between different data formats so that digital systems can store, process, and transmit information correctly.Bridging Human and Machine Language
The Problem: Computers only understand binary numbers (0s and 1s), but humans use rich symbols, letters, and images.
The Solution: Character Encoding assigns unique numbers or binary values to characters (like mapping the letter "A" to a specific binary code) so computers can process text

## Nominal vs Ordinal

### Nominal

which follows no order.
Categories have no natural order.
foe ex: colors red, green, white

### Ordinal

has some order
for ex: grades, a,b,c

## Manual classification

### PaymentMethod

Nominal as the values have no natural order

### Satisfaction

ordinal as they follws an order.
low indicates lowest value which can be represented as 1. and medium 2 and high 3

### Contract

Month-to-month
One year
Two year

ordinal- as month to month< One year < Two year

### T-shirt size

S,M,L,XL
ordinal as they follows the order

5.

Create your own example of:

one nominal variable
genre in movies
Action
comedy
horror
drama

one ordinal variable
grade system like A, B, C

## One-hot encoding

My understanding:
data processing technique that converts categorical data into binary 1 or 0 so machine can understand.
each category gets its own col.
pd.get_dummies()
it doesnt modify the orginal df
returns bool(true'false) matrix

## Practical implementation

What happened?

## drop_first=True

My understanding:
it wil drop the first column in the matrix as if we can findout its value using other col values

## Before vs After

Before columns: (7043, 19)
After columns: (7043, 30)

Why did the columns increase?
because i can see that categorical column has been divded like Contract_oneyear, partner_Yes etc
each value of the(categorical column) has been fragmented into a new columns with bool value

## Interview Questions

### Q1

What is categorical encoding?
it is the process of transforming categorical value into numerical as the machine can understand only numeric values

### Q2

What is one-hot encoding?
the type of encoding where it replaces the value into binary forms that is 0 /1 and each value gets its own column

### Q3

When would you use ordinal encoding?
when the values of categorical col follow natural order
ex: sixes s>m>l

### Q4

Why shouldn't we simply assign 1, 2, 3 to every categorical variable?
we can do it only if values follows the natural order as it will indicate the greaterness of previous values.
when categorical values have no order assigning 1,2,3 will create a Wrong logic

### Q5

Why might we use drop_first=True?
it will reduce the redundancy or reduce the burdern

<!-- google -->

If you keep all the columns, you create a mathematical loop where one column can be perfectly predicted by the others.Let's look at the car example again (Red, Green, Blue):If you know a car is not Green (0) and not Red (0), it must be Blue (1).Because Green + Red + Blue = 1 always, the columns are perfectly tied together.

### Q6

What is the difference between nominal and ordinal data?
nomial - follows no natural order ex: colors like red, blue, green
ordinal - has orders ex: grades

## What confused me

the output and types of the df after encoding and still not clear
my question - we applied get_dummies() to all the columns of data, what if it has ordinal data??
i know get_dummies will ignore the numerical col

## What became clearer

nomial, ordinal, one hot encoding

## AI/ML connection

data preprocessing
