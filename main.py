from evmoswallet import Wallet

seed = (
    'report spend crisp crisp world shock morning hour spoon problem one hole program piano donkey width today view canoe clap brick bundle rose book'  # NOQA: E501
)

w = Wallet(seed)
print(w.eth_address)
print(w.private_key)
