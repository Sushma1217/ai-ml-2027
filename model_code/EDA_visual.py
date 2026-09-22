import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Part 2 — Your first plot
# Create a simple histogram
plt.hist(df["tenure"])
plt.xlabel("Tenure")
plt.ylabel("No of Customers")
plt.title("Customer Tenure Distribution")
plt.show()

# Look at the graph and answer:

# What does the shape of this distribution tell me about customer tenure?
# # u shape, more number of customer falls between 0-5 and followed by 65-70 tenure 
# normaly distributed, no much outliers

# Part 3 — Histogram of MonthlyCharges
plt.hist(df["MonthlyCharges"])
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.title("Monthly Charges Distribution")
plt.show()

# Answer:

# Where are most customers concentrated? - between 70-110 range
# Is the distribution roughly symmetric? - no i can see more distribution towards 20-30 compared to other range
# Do you see any extreme values? yes. between 0-30

# Part 4 — Churn distribution
df["Churn"].value_counts().plot(kind="bar")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.title("Customer Churn Distribution")
plt.show()
# Think:

# Is the target balanced? - No
# Part 5 — 🔴 MANUAL challenge
# Try to create a bar chart showing the number of customers in each Contract type.
df["Contract"].value_counts().plot(kind="bar")
plt.xlabel("Contract")
plt.ylabel(" No of Customers")
plt.title(" Customer contract distribution")
plt.show()

# Part 6 — Compare churn and MonthlyCharges

# Now we're getting closer to actual EDA.
df.boxplot(column="MonthlyCharges", by="Churn")
plt.title("Monthly Charges by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.show()

# Answer:
# What difference do you observe between customers who churned and customers who didn't?
# ans- (90-25) 65 for no and (95-55) 40 for Yes so the difference is somewhere around 15

# Part 7 — Compare churn and tenure
df.boxplot(column="tenure", by="Churn")
plt.title("Tenure by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Tenure")
plt.show()

# Answer:
# Does the visualization support what you discovered on Day 12 using groupby()?
# matched with who did not churn but mismatching with who churn(i can see some outliers)
# some confusion in interpreting the box plot is there