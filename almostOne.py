# -*- coding:UTF-8 -*-

# sum = 0
# x = 1.
# for i in range(1, 1000000):
#     u = 1 / x
#     v = 1 / (x+1)
#     sum += u * v
#     print sum
#     x += 1



def iteritem(limit):
    x = 1.
    while 1:
        v = 1 / x
        u = 1 / (x+1)
        print v
        if v < limit:
            raise StopIteration
        yield u*v
        x += 1


print sum([n for n in iteritem(limit=0.00001)])