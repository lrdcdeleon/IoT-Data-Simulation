import json
from web3 import Web3

# 1. Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("✅ Successfully connected to Ganache!")
else:
    print("❌ Connection failed. Is Ganache open?")
    exit()

# 2. Contract Details
# This is the contract address you just copied
contract_address = Web3.to_checksum_address("0x0EC699C49fa756CF8E0A59fD7d5aEfE753A2F8Da")

# This is your contract ABI
abi = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "deviceId", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "dataType", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "dataValue", "type": "string"}
        ],
        "name": "DataStored",
        "type": "event"
    },
    {
        "inputs": [
            {"internalType": "string", "name": "_deviceId", "type": "string"},
            {"internalType": "string", "name": "_dataType", "type": "string"},
            {"internalType": "string", "name": "_dataValue", "type": "string"}
        ],
        "name": "storeData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getTotalRecords",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# 3. Initialize Contract
contract = web3.eth.contract(address=contract_address, abi=abi)

# 4. Perform a Test Transaction
# This uses the first account in your Ganache list
web3.eth.default_account = web3.eth.accounts[0]

try:
    print(f"Current Total Records: {contract.functions.getTotalRecords().call()}")

    print("Sending test data to blockchain...")
    tx_hash = contract.functions.storeData("IOT-DEV-01", "Status", "Verified").transact()

    # Wait for the transaction to be mined
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Transaction Successful! Block Number: {receipt.blockNumber}")
    print(f"Updated Total Records: {contract.functions.getTotalRecords().call()}")

except Exception as e:
    print(f"❌ Error: {e}")