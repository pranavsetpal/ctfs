from pwn import *
from ctypes import CDLL
from time import time

libc = CDLL("/lib/libc.so.6")
choices = ["paper", "rock", "scissors"]

r = remote("159.65.81.51", 30102)
# r = process("./janken")
r.recvuntil(b'>> ')
r.sendline(b'1')

for i in range(99):
    r.recvuntil(b'>> ')
    libc.srand(int(time()))
    choice = choices[libc.rand() % 3]
    print(choice)
    r.sendline(bytes(choice, "utf-8"))

print(r.recvall().decode().strip())

