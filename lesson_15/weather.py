import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WEATHER_tokyo_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert temperature safely
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Drop bad rows
df = df.dropna(subset=['temperature'])

# ---------------------------------------------------
# CREATE SIMPLE TIME INDEX (NO DATE ERRORS)
# ---------------------------------------------------

df = df.reset_index()

# Fake "month grouping" (safe method even if no real dates)
df['Month'] = (df.index // 30) + 1

# ---------------------------------------------------
# BASIC STATS
# ---------------------------------------------------

print("Average Temperature:", df['temperature'].mean())
print("Max Temperature:", df['temperature'].max())
print("Min Temperature:", df['temperature'].min())

# ---------------------------------------------------
# MONTHLY AVERAGE
# ---------------------------------------------------

monthly_avg = df.groupby('Month')['temperature'].mean()

print("\nMonthly Average Temperature:")
print(monthly_avg)

# Plot monthly average
plt.figure(figsize=(8,5))
plt.bar(monthly_avg.index, monthly_avg.values, color='skyblue')

plt.title("Tokyo Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")

plt.show()

# ---------------------------------------------------
# TREND GRAPH
# ---------------------------------------------------

plt.figure(figsize=(10,5))
plt.plot(df['temperature'], color='red')

plt.title("Tokyo Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature")

plt.grid(True)
plt.show()