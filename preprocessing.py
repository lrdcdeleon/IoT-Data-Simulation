import pandas as pd
import numpy as np
from web3 import Web3

# 1. Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 2. Contract Configurations
contract_address = Web3.to_checksum_address("0xCaddCE47bf3682AAB3fBb8F905bb6756290F0013")
abi = [
    {"inputs": [], "name": "getTotalRecords", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "getRecord", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}, {"internalType": "string", "name": "", "type": "string"}, {"internalType": "string", "name": "", "type": "string"}, {"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}
]
contract = web3.eth.contract(address=contract_address, abi=abi)

# 3. Get total stored records
total_records = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_records}")

# 4. Fetch all stored IoT data
data = []
print("Downloading records from blockchain... (This takes a few seconds)")
for i in range(total_records):
    record = contract.functions.getRecord(i).call()
    data.append({
        "timestamp": record[0],
        "device_id": record[1],
        "data_type": record[2],
        "data_value": record[3]
    })

# 5. Convert to DataFrame & Format Timestamps
df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
print("\n--- Raw Data ---")
print(df.head())

# 6. Extract numeric values & Handle Missing Values
df["numeric_value"] = df["data_value"].str.extract(r'(\d+\.?\d*)').astype(float)
df.fillna(0, inplace=True)
print("\n--- Cleaned Data ---")
print(df.head())

# 7. Save to CSV
df.to_csv("cleaned_iot_data.csv", index=False)
print("\n✅ Cleaned IoT data saved successfully as cleaned_iot_data.csv")