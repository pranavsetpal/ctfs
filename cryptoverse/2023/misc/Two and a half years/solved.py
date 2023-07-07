from pwn import *
from random import choices

p = remote("20.169.252.240", 4202)

def r():
    global prob_n1, prob_0, prob_p1
    return choices([-1,0,1], weights=[prob_n1, prob_0, prob_p1])[0]

def fix(y):
    global h
    if y < 0: return 0
    if y <= h: return y
    if h < y: return h

def y(n):
    global a
    ys = [a]
    for _ in range(1,n+1):
        ys.append(fix(ys[-1] + r()))

    return ys

def area_under_graph(points):
    area = 0
    for i in range(1, len(points)):
        low  = min(points[i-1], points[i])
        high = max(points[i-1], points[i])
        rec_area = low
        tri_area = (high-low) / 2

        area += rec_area + tri_area

    return area


for i in range(20):
    p.recvuntil(b':\n')
    n, h, a, prob_n1, prob_0, prob_p1 = [int(n) for n in p.recvline().decode().split(' ')]
    # n, h, a, prob_n1, prob_0, prob_p1 = 4,10,3,100,0,0
    # n, h, a, prob_n1, prob_0, prob_p1 = 2,10,5,50,0,50

    print(n, h, a, prob_n1, prob_0, prob_p1)

    points = y(n)
    area = area_under_graph(points)
    area = str(round(area,3)).encode()

    p.sendline(area)
    print(area)

print(p.recvall().decode())
p.close()
