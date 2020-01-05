
b=1
g=0
list=[]
sorted_list=[]
inpt = int(input("Enter the number of details to be sorted:"))
while True:
    a = input("enter the "+str(b)+"st person Name:")
    d = input("enter the "+str(b)+"st person age:")
    e = input("enter the "+str(b)+"st person marks:")
    list.append(a)
    list.append(d)
    list.append(e)
    c = tuple(list)
    sorted_list.append(c)
    list.clear()
    g+=1
    b+=1
    if inpt == g:
        break;

o = sorted(sorted_list)
print(o)
