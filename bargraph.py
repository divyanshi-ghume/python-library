import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset and make the graph for both sex suicide rate for male, female and both sex in afghanisthan
df = pd.read_csv("cleaned_data.csv")

country = "Afghanistan"   
year = 2015              

data = df[(df["Location"] == country) & (df["Period"] == year)]


plt.bar(data["Dim1"], data["First Tooltip"], color=['#66b3ff', '#ff9999', '#99ff99'])

plt.title(f"Suicide Rates in {country} ({year})")
plt.xlabel("Gender / Group")
plt.ylabel("Suicide Rate per 100,000 population")
plt.tight_layout()


plt.show()
