list = ["0100","0011","1010","1001","1111"]
list1 = [ for a in list]

for a in list:
    b = int(a,2)
    if b%5 == 0:
        list1.append(a)

print(",".join(list1))        
        
