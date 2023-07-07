from pwn import *
from base64 import b64encode

r = remote('20.169.252.240', 4203)

f = open("./test.png", "rb")
img = b64encode(f.read())
f.close()

r.sendline(img)
print(r.recvall().decode())
r.close()
