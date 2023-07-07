message = open("message.txt", "r").read().split()

decode = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "_"]

for n in message:
    n = int(n) % 41

    for i in range(41):
        if (n*i) % 41 == 1:
            n = i
            break
    print(decode[n-1], end='')
