flag = open('./enc', 'r').read()
# flag = open('./flag.txt', 'r').read()

# output = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

for i in range(0, len(flag)):
    print(chr(ord(flag[i]) >> 8), end="")
    print(chr(ord(flag[i]) - (ord(flag[i]) >> 8 << 8)), end="")
