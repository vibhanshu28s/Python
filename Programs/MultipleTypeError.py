 # 18. Multiple Type Error Handeling

try:
    n1=int(input("Enter First Number "))
    n2=int(input("Enter Second Number "))
    e=n1/n2
    print("Answer=",e)
    
except ZeroDivisionError:
    print("Division By zero Not Allowed")
except TypeError:
    print("Type Error")
except ValueError:
    print("Invalid Value Not Accepted")
