 # 17. Linear Search 

def lsearch(lst,val):
    f=0
    l=len(lst)
    for i in range (0,l):
        if val==lst[i]:
            print("Value Found At",(i+1),"position")
            f=1
            break
    if f==0:
        print("Value Not Found")
        
l=[34,56,98,25,4,5,66,12,79,6,3,45,2,98,10]
v=int(input("Enter The Value To Search "))
lsearch(l,v)
