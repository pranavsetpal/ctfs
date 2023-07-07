password = "cvpbPGS{P7e1S_54I35_71Z3}"

decoded = ""

for i in password:
    if i.isalpha():
        if ord(i.lower())-13 < ord("a"):
            decoded += chr(ord(i)+13)
        else:
            decoded += chr(ord(i)-13)
    else:
/bin/bash: line 1: :q: command not found
print(decoded)
