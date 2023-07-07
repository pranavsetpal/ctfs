from pwn import *
import rstr

r = remote("puzzler7.imaginaryctf.org",11003)
for i in range(100):
    r.recvuntil(b'\t')
    rx = r.recvline()[:-1].decode("utf-8")
    r.recvuntil(b'Enter string:\n')
    r.sendline(bytes(rstr.xeger(rx), "utf-8"))
# r.sendafter(b'Enter string:\n', rstr.xeger(rx))
# print("RECEIVED REGEX:", rx)
# print("COR STRING:", rstr.xeger(rx))

r.interactive()
# r.sendafter("Enter string:\n", rstr.xeger(rx))
