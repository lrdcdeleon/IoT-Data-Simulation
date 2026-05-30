import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the cleaned IoT data you just generated
df = pd.read_csv("cleaned_iot_data.csv")

# 2. Convert timestamp column to actual datetime format for accurate plotting
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 3. Set the visualization style
sns.set_theme(style="whitegrid")

# 4. Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="timestamp", y="numeric_value", hue="data_type", marker="o")

# 5. Add titles, labels, and format the layout
plt.xticks(rotation=45)
plt.title("IoT Sensor Readings Over Time", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Sensor Value", fontsize=12)
plt.legend(title="Sensor Type")
plt.tight_layout()

# 6. Save the plot as an image and display it
plt.savefig("iot_sensor_plot.png")
print("✅ Plot saved successfully as iot_sensor_plot.png")
plt.show()