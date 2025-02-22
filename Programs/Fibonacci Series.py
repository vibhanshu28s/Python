 # 15. To Find Fibonacci Series 

def fibonacci():
    a=0
    b=1
    print(a,end=' ')
    while True:
        yield b
        c=a+b
        a=b
        b=c
n=int(input("Enter the value "))
ob=fibonacci()
for i in range (1,n):
    print(ob.__next__(),end=' ')
