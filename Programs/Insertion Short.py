 # 16. Insertion Short

def insertionshort(list):
    l=len(list)
    for i in range (1,l):
        t=list[i]
        p=i-1
        while(t<list[p] and p>=0):
            list[p+1]=list[p]
            p-=1
        list [p+1]=t
        print("After Pass No.",i,"",list)

list=[24,22,-6,34,80,-43]
insertionshort(list)
print(list)

