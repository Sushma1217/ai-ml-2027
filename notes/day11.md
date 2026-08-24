# Day 11 — Data Types & Inconsistent Data

## Data types

## astype()

convert column from one data type to another

## pd.to_numeric()

attempts to convert values to numeric types. Because conversion can fail. and with error="coerce" failed conversions become missing values.
pd.to_numeric(arg, errors='raise', downcast=None)
arg- dataframe number
errors- how invalid or unparseable data is handled

## errors="coerce"

errors="coerce" means roughly:
If something can't be converted to a number, turn it into a missing value instead of crashing.

## unique()

used to find the unique values of the column

## value_counts()

pandas counts the occurrences of unique values in a dataset.
returns pandas Series sorted in descending order, putting the most frequent items at the top

## Category standardization

making all the values follows same pattern or cases etc

replace()- replaces specific values across a full DataFrame or a targeted column

## String operations

making the value uniform like converting to upper, lower etc
.str- makes whole column as string so we can apply upper, lower

strip()- removes a speci char if params is provided else removes leading and trailing whitespace and new lines will be removed.

## What confused me

too many methods or functions like valu_counts, pd.to_numeric(), strip so hard to remember all

## What became easier

dtypes, unique, value assigment, performing string operations

## AI/ML connection

Make sure your data types actually represent the meaning of the data.

pipeline
Raw data
↓
Inspect dtypes
↓
Fix numeric columns
↓
Handle invalid numeric values
↓
Inspect categories
↓
Standardize categories
↓
Check final data

## Decisions I made

replacing na value of age with mean- I chose mean because the age values don't contain an obvious extreme outlier; in a real dataset I'd inspect the distribution before choosing mean vs median.
Int64- for converting age with unknown val
int64 → normal integer, cannot represent NaN
Int64 → Pandas nullable integer, can represent missing values

## Interview questions

Why do we standardize categorical values
What does astype() do?
What is pd.to_numeric()?
What does errors="coerce" mean?
What is categorical data?
Why do "IT", "it" and "Information Technology" create a problem?
What does .unique() do?
What does .value_counts() do?

What is the difference between "cleaning data" and "transforming data"?
cleaning the data - Fixing problems in the data.
missing values
duplicates
invalid values
inconsistent categories
wrong data types

transforming- Changing data into a form that is more useful for analysis/modeling.
Changing data into a form that is more useful for analysis/modeling.

<!-- MCP -->

Why would an AI application need access to external tools or data instead of relying only on the LLM?
to increase the accuracy, handle and understand user need efficiently.

Then give 3 examples of things an AI assistant might need to access:
API, DATABase, code

User - asks the question
↓
LLM- a layer or interface to read and understand what user is asking
↓
Tool- to connect the code
↓
Pandas / Python- a code, to fetch the data or perform the action
↓
employees.csv- data set
↓
Result- result after finding out the end output by performing required action
↓
LLM- will take this result and process to give answer to user
↓
Natural-language answer - end result to user in human readable form
