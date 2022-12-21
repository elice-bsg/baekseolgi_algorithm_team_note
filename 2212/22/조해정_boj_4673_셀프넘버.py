n = 1
dn = []
while n <= 10000:
    temp = n
    nw = n

    for i in range(4):
        nw += temp % 10
        temp //= 10
    dn.append(nw)
    if n not in dn:
        print(n)
    n += 1