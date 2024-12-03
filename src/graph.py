import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    "Country": ["India", "China", "USA", "Germany", "Brazil", "Australia"],
    "Pollutant": ["PM2.5", "PM10", "Ozone", "PM2.5", "PM10", "Ozone"],
    "Death_Rate_per_100k": [112, 98, 28, 35, 67, 12],
    "Year": [2021, 2021, 2021, 2021, 2021, 2021]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
colors = ["blue", "green", "orange", "purple", "red", "cyan"]

# Save DataFrame to a CSV file
df.to_csv("air_pollution_death_rates.csv", index=False)
print("DataFrame has been exported to 'air_pollution_death_rates.csv'")

# Create a bar chart
colors = ["blue", "green", "orange", "purple", "red", "cyan"]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Country"], df["Death_Rate_per_100k"], color=colors, edgecolor="black")
plt.title("Air Pollution Death Rates by Country (2024)", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Death Rate per 100k Population", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Add legend to indicate pollutant type for each country
for i in range(len(df)):
    plt.text(i, df["Death_Rate_per_100k"][i] + 1,  # Add text above each bar
             f"{df['Pollutant'][i]}",
             ha='center', fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()