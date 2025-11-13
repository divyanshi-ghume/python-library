import pandas as pd

# Read the dataset 
df = pd.read_csv('data.csv')
print(df.to_string())

female_entries = df[df['Dim1'] == 'Female']

print(female_entries.to_string())

count_female = len(female_entries)

print("Number of Female Entries:", count_female)

print(df.iloc[2738])

filtered = df[df["Period"] >= 2015]

print(filtered)

count_period = len(filtered)
print("Number of entries with Period >= 2015:", count_period)

print("Missing values per column:")
print(df.isnull().sum())

df = df[df["First Tooltip"] != 0]


print("Entries after deleting rows where 'First Tooltip' == 0:")
print(df.shape)            
print(df.head())           

df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_data.csv'")

