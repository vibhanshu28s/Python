 # 22. To Find Value Present or Not

def fun(list,n):
    l=len(list)
    f=0
    if(1!=0):
        for i in range(0,l):
            if(list[i]==n):
                f=1
                print("Value Found")
                break
            if(f==1):
                for j in range(i,l-1):
                    list[j]=list[j+1]
                    print(list)
                    del list[l-1]
                    
        else:
            print("Value Not Found")

    else:
        print("Empty List")

lst=[2,5,9,15,22,29]
a=int(input("Enter the value "))
fun(lst,a)


            
