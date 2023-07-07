from pwn import *

r = remote("178.62.64.13", 31475)
print(r.recvuntil(b'> ').decode('utf-8'))
r.sendline(b'1')
print("1\n")

for i in range(500):
    r.recvuntil(b': ')
    exp = r.recvuntil(b'=').decode()[:-1].strip()
    print(exp)
    exp = exp.split(' ')
    res = None
    for i in range(1, len(exp), 2):
        if exp[i] not in ["+", "-", "*", "/"]:
            res = "SYNTAX_ERR"
            break
        if exp[i] == "/" and exp[i+1] == "0":
            res = "DIV0_ERR"
            break
    else:
        exp = ' '.join(exp)
        res = round(eval(exp), 2)
        res = "MEM_ERR" if abs(res) > 1337 else str(res)

    print(res)
    r.sendline(res)

print(r.recvall().decode('utf-8'))

r.close()

