
import json
from web3 import Web3, HTTPProvider


# truffle development blockchain address
blockchain_address = 'HTTP://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:/Users/sures/OneDrive/Desktop/forensic_eviden/forensic_eviden/forensic_eviden/node_modules/.bin/build/contracts/forensic.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x843C8031B39059c80E98c41bf9631a2C59A0cddb'
syspath=r"C:\Users\sures\OneDrive\Desktop\forensic_eviden\forensic_eviden\forensic_eviden\static\\"
