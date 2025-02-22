 # 21. To Generate Table of a Given Number

def table(N):
    while True:
        yield N
        N=N+a

a=int(input("Enter The Number To Find The Table "))
g1=table(a)
for i in range(10):
    print(g1.__next__())
