from web3 import Web3

# 1. Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 2. Contract Configurations (Using your fresh deployed address)
contract_address = Web3.to_checksum_address("0x4f78b869e89FC48368379D215EAca9414Ff2f700")

# Pristine ABI layout matching your exact Solidity contract variables
abi = [
    {
        "inputs": [],
        "name": "getTotalRecords",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}],
        "name": "getRecord",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

try:
    contract = web3.eth.contract(address=contract_address, abi=abi)
    
    # 3. Call and print contract totals
    total_records = contract.functions.getTotalRecords().call()
    print(f"\nTotal IoT records stored: {total_records}")
    
    if total_records > 0:
        first_record = contract.functions.getRecord(0).call()
        print(f"First Stored Record: {first_record}\n")
    else:
        print("Contract is reachable, but array records are empty.\n")
        
except Exception as e:
    print(f"❌ Verification Error: {e}")