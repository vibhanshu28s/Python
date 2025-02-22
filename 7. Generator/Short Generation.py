def fun(n):
    while(True):
        yield n
        n=n+5
g1=fun(100)
for i in range(11):
    print(g1.__next__())
