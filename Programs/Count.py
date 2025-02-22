 # 3. Count Alphabets, Digits, Space, Special Character

file=open('H:\\Python\\5. File Handeling\\vibhanshu.txt','r')
co1=0
co2=0
co3=0
co4=0
s=' '
while s:
    s=file.read()
    #print(s)
    if(s.isalpha()):
        co1+=1
    elif(s.isdigit()):
        co2+=1
    elif(s.isspace()):
        co3+=1
    else:
        co4+=1

print("Alphabets= ",co1)
print("Digits=",co2)
print("Space=",co3)
print("Special characters=",co4)
