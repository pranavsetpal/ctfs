maskArray = [67,0,20,3,2,16,57,4,0,25,5,2,18,65,1,2,64,17,2,0,1,6,18,65,1,0,4,2,0,0,64,16,16,64,2,4,0,3,9,0,0,1,0,8,8,0,65,24,22,64,0,0,0,5,0,2,65,16,22,65,1,6,4,0,66,21,1,0,0,2,24,65,67,24,24,67,2,8,65,18,16,64,2,0,68,19,19,64,72,2,2,117,0]

switch = True
val = 0
flag = ""

for mask in maskArray:
    if switch:
        # Apply next mask with OR operator
        val = val | mask
    else:
        # Apply next mask with XOR operator
        val = val ^ mask
        flag += (chr(val))
    switch = not switch

print(flag)
