 # 19. Raise A User Define Error

class myError(Exception):
    pass
msg1=myError("This age is not allowed for job")
msg2=myError("This age not allowed for job, he/she too old to job")

try:
    age=int(input("Enter The Age "))
    if age>60:
        raise msg2
    elif age<18:
        raise msg1
    else:
        print("Valid For Job")
except myError as msg1:
    print(msg1)
except myError as msg2:
    print(msg2)
