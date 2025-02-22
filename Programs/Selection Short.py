 # 25. Selection Short

def selection(lst):
    l=len(lst)
    for i in range(0,l):
        min=i
        for j in range(i+1,l):
            if lst[min]>lst[j]:
                min=j
        t=lst[i]
        lst[i]=lst[min]
        lst[min]=t
        print("After",(i+1),"pass",lst)

l=[37,25,2,14,16,4]
selection(l)
