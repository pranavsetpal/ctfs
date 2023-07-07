from pwn import *

r = remote("159.65.81.51", 30650)

r.recv()
r.sendline(b'2')

r.recvuntil(b'\n\n')

lines = r.recvuntil(b'\n\n').decode("utf-8").split('\n')[:-2]
for line in lines:
    print(line)
print()
lines = lines[:-1]

left = []
right = []

for line in lines:
    words = line.split()
    left.append((int(words[4]), int(words[1])))

order = []

def move(origin, dest, n_people, time):
    people = []
    for i in range(n_people):
        people.append(time(origin))
        origin.remove(people[i])
    dest.extend(people)
    order.append([person[1] for person in people])
    print(f"ORIG: {origin}")
    print(f"DEST: {dest}\n")

if len(lines) % 2 == 0:
    while True:
        move(left, right, 2, min)
        if len(left) == 0: break
        move(right, left, 1, min)
        move(left, right, 2, max)
        move(right, left, 1, min)
        print()
else:
    while True:
        move(left, right, 2, min)
        move(right, left, 1, min)
        move(left, right, 2, max)
        if len(left) == 0: break
        move(right, left, 1, min)
        print()


for i in range(len(order)):
    order[i].sort()
order = ''.join(str(order).split(' '))[1:-1]
print(order)

r.recv()
r.sendline(bytes(order, "utf-8"))
print(r.recv().decode("utf-8"))

r.close()
