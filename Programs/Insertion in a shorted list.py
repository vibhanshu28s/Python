 # 24. Insesrtion In A Shorted List

def fun(list):
    l=len(list)
    list.append(None)
    n=int(input("Enter The element to be inserted "))
    for i in range(l,-1,-1):
        if(list[i-1]>n and i!=0):
            list[i]=list[i-1]
        else:
            list[i]=n
            break
    print("After Element Insertion")
    print(list)
lst=[2,5,9,15,22,29,39,45,51,58]
fun(lst)
