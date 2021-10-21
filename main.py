"""
Challenge 8: Stellar.toml
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("Shhh")
quest_account_pub_key = GBKABTRM7EHU23S4TMLXW547JDRBLAJ4JYKZOYY3D235UGHXZEGFPH32
quest_account_priv_key = SDIDVISRSTMTI4YOFQRMMJ5UJS4BW6FGWPSTGK4WY6R5TJOFVLEDBWYN

# 2. Use Stellar Quest Account and set multisign
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(quest_account_pub_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_set_options_op(
        home_domain = "steelo347.github.io"
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")

