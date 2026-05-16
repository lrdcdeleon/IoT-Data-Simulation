import pandas as pd

# 1. Load the simulated data
# Using the exact filename from your Week 2 output
input_file = "MO-IT148 Homework IoT Data Simulation S2101 Group 28.csv"
df = pd.read_csv(input_file)

print("--- Original Data Preview ---")
print(df.head())

# 2. Check for missing values
print("\nChecking for null values:")
print(df.isnull().sum())

# 3. Robust Data Cleaning Function
def clean_value(val):
    if isinstance(val, str):
        # FIX: If it's a GPS coordinate pair, take only the first part (Latitude)
        if ',' in val:
            val = val.split(',')[0]
        
        # Keep only digits and the first decimal point found
        numeric_part = ""
        has_decimal = False
        for char in val:
            if char.isdigit():
                numeric_part += char
            elif char == '.' and not has_decimal:
                numeric_part += char
                has_decimal = True
        
        try:
            return float(numeric_part) if numeric_part else 0.0
        except ValueError:
            return 0.0
    return float(val) if pd.notnull(val) else 0.0

# Create the numeric column for analysis
df['numeric_value'] = df['data_value'].apply(clean_value)

# 4. Convert timestamp to actual datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 5. Save the cleaned data
output_file = "cleaned_iot_data.csv"
df.to_csv(output_file, index=False)

print(f"\n✅ Data cleaning complete! Saved as: {output_file}")
print("--- Cleaned Data Preview ---")
print(df[['timestamp', 'data_type', 'numeric_value']].head())