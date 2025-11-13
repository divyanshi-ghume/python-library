import pandas as pd
# apply pandas on cleaning_output.csv


df = pd.read_csv("cleaning_output.csv")
print(df)
print("Missing values in each column:")
print(df.isnull().sum())
df.fillna(0, inplace=True)
print(df)
df.drop_duplicates(inplace=True)
df.to_csv("cleaned_sample_with_nulls.csv", index=False)
print("\n Cleaned dataset saved as 'cleaned_sample_with_nulls.csv'")

# querying and filtering dataset
print("\n People with Age >= 30:\n")
print(df[df['Age'] >= 30])
print("\n People from Delhi:\n")
print(df[df['City'] == 'Delhi'])
print("\n People from Delhi with Salary > 60000:\n")
print(df[(df['City'] == 'Delhi') & (df['Salary'] > 60000)])

# sorting and data analysis
print("\n Sorted by Salary (High to Low):\n")
print(df.sort_values('Salary', ascending=False))

print("\n Average Salary by City:\n")
print(df.groupby('City')['Salary'].mean())

print("\n Total Salary by City and Age:\n")
print(df.groupby(['City', 'Age'])['Salary'].sum())

print("\n Count of People by City:\n")
print(df['City'].value_counts())

# renamining multiple columns
df.rename(columns={'Name':'Employee_Name', 'City':'Location'}, inplace=True)
print(df)

# Add a new column ‘Profit’ = Salary - Cost
df['Cost'] = [30000, 25000, 28000, 26000, 27000, 24000, 0, 29000, 31000, 25000,
              22000, 23000, 26000, 27000, 28000, 30000, 25000, 26000, 27000, 29000][:len(df)]

df['Profit'] = df['Salary'] - df['Cost']

df['Discounted_Salary'] = df['Salary'] * 0.9

print("\n Updated Dataset:\n")
print(df)

# summary of data  
print("\n Average Salary:", df['Salary'].mean())

print("\n Total Profit:", df['Profit'].sum())

print("\n Median Salary:", df['Salary'].median())
print("\n Minimum Salary:", df['Salary'].min())
print("\n Maximum Salary:", df['Salary'].max())

print(df['Profit'].describe())

