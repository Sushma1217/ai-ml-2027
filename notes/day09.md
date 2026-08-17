# Day 9 — Pandas

## loc vs iloc

in slicing -
iloc[0:3]- gives row till 2(0,1,2)
loc - gives 4 record which means it includes the end value also

loc[row_indexer, column_indexer]

## groupby

group the items
groupby()- stand alone does not return any value so we have to add method for it like size, count, mean, max

groupby("department")["salary"].mean()?
ans- group the data based on department and take its avg salary

## aggregation

## agg()

used to apply one or more maths ops like mean, median, min, max etc to dataframe
mostly paired with groupby

## What confused me

iloc vs loc
7th qus- got almost correct but failed to filter the records(bool mask condition was right)

## What became easier

bool masking
applying methods like mean, max etc

## AI/ML connection

asusual conditional based data filtering

## Interview questions

loc vs iloc?
shape vs size?
What does groupby() do?
What is aggregation?
