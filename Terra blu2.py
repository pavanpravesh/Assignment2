import re

list=[]
sorted=[]
a = 0
b = int(input("Enter the number of passwords to be entered:"))
while True:
    p=input("Ënter the password:")
    list.append(p)
    a+=1
    if a==b:
        break;

for pswd in list:
    if re.match(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$]).{6,12})', pswd):
        if len(pswd)<=12 and len(pswd)>=6:
            sorted.append(pswd)
if len(sorted)>0:    
    print("Vaild Passowrds:"",".join(sorted))        
else:
    print("None of the Passwords are valid")
