 # 14. To Find Cube of A Number

def cube(n):
    for i in range (n,n+1):
        yield i**3
a=int(input("Enter A number "))
o=cube(a)
for i in range (10):
    print("->",i)
    print(o.__next__())
    print("--------------")
    
