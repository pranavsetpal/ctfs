flag = [char for char in open("./out.bin", "rb").read()]

key = flag[0] ^ ord('i')
print(key)
key = flag[1] ^ ord('c') ^ ord('c')
print(key)

for i in range(64):
    for j in range(i+1):
        flag[i] = flag[i] ^ key

flag = ''.join([chr(char) for char in flag])
print(flag)
