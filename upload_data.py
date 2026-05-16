import pandas as pd
import time
from web3 import Web3

# 1. Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

# 2. Contract Details (Your verified address)
contract_address = Web3.to_checksum_address("0x0EC699C49fa756CF8E0A59fD7d5aEfE753A2F8Da")
abi = [
    {"inputs": [{"internalType": "string", "name": "_deviceId", "type": "string"}, {"internalType": "string", "name": "_dataType", "type": "string"}, {"internalType": "string", "name": "_dataValue", "type": "string"}], "name": "storeData", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "getTotalRecords", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}
]
contract = web3.eth.contract(address=contract_address, abi=abi)

# 3. Load your Logistics CSV (Week 2 Data)
df = pd.read_csv("MO-IT148 Homework IoT Data Simulation S2101 Group 28.csv")

print(f"Starting bulk upload of {len(df)} records...")

# 4. Loop through the CSV and send to Blockchain 
for i, row in df.iterrows():
    try:
        txn = contract.functions.storeData(
            str(row["device_id"]), 
            str(row["data_type"]), 
            str(row["data_value"])
        ).transact()
        
        # Wait for receipt to confirm storage [cite: 431]
        receipt = web3.eth.wait_for_transaction_receipt(txn)
        print(f"✅ [{i+1}/100] Data Stored! Txn: {receipt.transactionHash.hex()[:10]}...")
        
        # Small delay to avoid flooding Ganache [cite: 436]
        time.sleep(0.1) 
    except Exception as e:
        print(f"❌ Error at row {i}: {e}")

print(f"\n🚀 SUCCESS: {contract.functions.getTotalRecords().call()} total records now on the blockchain!")