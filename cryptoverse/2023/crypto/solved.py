encrypted = '彳宀彳马辶{飞广口川彳门巴川彳大广彳飞彐大川巴头}'

print("Encrypted: ")
for c in encrypted:
    print(ord(c), end=' ')

print("\ncvctf: ")
for c in 'cvctf':
    print(ord(c), end=' ')


# shift = ord(encrypted[0]) - ord('c')
#
# print(shift)
# print(ord(encrypted[1]) - shift)
# # print(chr(ord(encrypted[1]) - shift))
