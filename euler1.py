def euler_1():
    n = 0
    for x in range(1000):
        if x % 3 == 0:
            n += x
        elif x % 5 == 0:
            n += x
        else:
            continue
    print n

def euler_2():
    x = 1
    y = 2
    a = 0
    s = 2
    while y <= 4000000:
        a = x + y
        x = y
        y = a
        if a % 2 == 0:
            s += a
    print s