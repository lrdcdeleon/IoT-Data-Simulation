import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the cleaned data
df = pd.read_csv("cleaned_iot_data.csv")

# 2. Ensure timestamp is in the correct format for plotting
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 3. Set the visual style
sns.set_theme(style="whitegrid")

# 4. Create the Line Plot
plt.figure(figsize=(12, 6))
plot = sns.lineplot(data=df, x="timestamp", y="numeric_value", hue="data_type", marker="o")

# 5. Add Titles and Labels
plt.title("IoT Sensor Readings Over Time", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Sensor Value", fontsize=12)
plt.xticks(rotation=45)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# 6. Save the plot as an image for your Word doc
plt.savefig("iot_sensor_plot.png")
print("✅ Plot saved as iot_sensor_plot.png")

# 7. Show the plot on screen
plt.show()