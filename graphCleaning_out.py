import pandas as pd
import matplotlib.pyplot as plt
# apply matplotlib on cleaninig_output.csv

# Step 1: Read CSV file
df = pd.read_csv("cleaning_output.csv")

# Step 2: Clean data (optional – remove rows where salary is 0)
df = df[df["Salary"] > 0]

# Step 3: Create a bar graph
plt.bar(df["Name"], df["Salary"], color='skyblue')

# Step 4: Customize graph
plt.title("Salary of Each Person")
plt.xlabel("Name")
plt.ylabel("Salary (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

# Step 5: Show the graph
plt.show()


