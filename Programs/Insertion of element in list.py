 # 23. Insertion of element in list

def insertion(list,val,pos):
    l=len(list)
    list.append(None)
    for i in range(l,pos-1,-1):
        list[i]=list[i-1]
    list[i-1]=val

lst=[23,45,3,6,85,41,76,5,9,8]
print("Before Insertion= ",lst)
v=int(input("Enter The value to be inserted "))
p=int(input("Enter The Position "))
insertion(lst,v,p)
print("After Insertion= ",lst)
