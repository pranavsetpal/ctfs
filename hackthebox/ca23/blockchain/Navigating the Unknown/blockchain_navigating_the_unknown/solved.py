from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://209.97.134.50:32352"))
# print(w3.eth.block_number)
# print(w3.is_connected())
# print(w3.is_address("0x02b4f7A34B23cf13A26583A1919E091AB54C279F"))

# print(w3.eth.accounts)
# > ['0xE7625dd8E703b958D63d1FfD47063AD3C69b4714', '0x02b4f7A34B23cf13A26583A1919E091AB54C279F']

w3.eth.send_transaction({
    'to': '0xE7625dd8E703b958D63d1FfD47063AD3C69b4714',
    'value': 8
})

# w3.eth.get_block('0x02b4f7A34B23cf13A26583A1919E091AB54C279F')
# w3.eth.get_code
# print(w3.eth.get_block('latest'))
# print(w3.eth.get_block('0xE7625dd8E703b958D63d1FfD47063AD3C69b4714'))

# block = w3.eth.get_block('latest')
# print(block)
