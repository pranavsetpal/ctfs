from pwn import *

unpack = make_unpacker(32, endian='little', sign='unsigned')

DAT_18=unpack(b'\xff\xd4\xb5\x20')
DAT_1c=unpack(b'\xc7\x8f\x37\x32')
DAT_20=unpack(b'\x67\x87\x5f\xd5')
DAT_24=unpack(b'\xad\xa1\x4a\x10')

flag = 0

def magic_func():
    global DAT_18,DAT_1c,DAT_20,DAT_24
    n = DAT_18 ^ DAT_18 << 0xb
    DAT_18 = DAT_1c
    DAT_1c = DAT_20
    DAT_20 = DAT_24
    DAT_24 = DAT_24 ^ DAT_24 >> 0x13 ^ n ^ n >> 8

    return n

for i in range(5):
    output = magic_func()
    input = output #maybe
    flag = input % 1337 + flag

print(f"input=DAT_24: {flag}")
