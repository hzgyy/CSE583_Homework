import pandas as pd
import matplotlib
# Use a non-interactive backend in WSL
matplotlib.use("Agg")

import matplotlib.pyplot as plt

df = pd.read_csv('bicycle_data.csv')

# Display the first five rows
print(df.head())

# Display column names
print(df.columns)

# Display the data type of each column
print(df.dtypes)

# Display a complete summary
df.info()

# Date                                                                   object
# Fremont Bridge Sidewalks, south of N 34th St Total                    float64
# Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk    float64
# Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk    float64
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)

# Add the total bicycle count
df["Total"] = df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"] +\
        df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]

# Extract the hour and year from the Date column
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

#print(df.head())
#print(df.dtypes)
# Create a new DataFrame containing only data from 2016
df_2016 = df[df["Year"] == 2016].copy()

#print(df_2016.head())
#print(df_2016.shape)
# Check the number of missing values in each column
print(df_2016.isna().sum())

# Find rows containing at least one missing value
missing_mask = df_2016.isna().any(axis=1)
missing_points = df_2016[missing_mask]

print(missing_points)
print("Number of time points with missing data:", missing_mask.sum())
# There are 1 time points with missing data.
# Rows with missing data are removed so they do not affect later analysis.
df_2016_clean = df_2016.dropna().copy()
# Question 5
# Calculate the total bicycle count for each hour of the day
counts_by_hour = (
    df_2016_clean
    .groupby("Hour")["Total"]
    .sum()
)

# Create the plot using pandas and matplotlib
ax = counts_by_hour.plot(
    kind="line",
    marker="o",
    figsize=(9, 5)
)

ax.set_title("Total Bicycle Counts by Hour in 2016")
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Total Bicycle Count")
ax.set_xticks(range(24))
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(
    "counts_by_hour.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()
# question 7
max_hour = counts_by_hour.idxmax()
print(f"hour with max bycycles:",max_hour)
# hour 17 is the busiest hour
