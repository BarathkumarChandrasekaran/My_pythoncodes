List1= [2, "India35", True]
List2= [3, False, "123Usa"]
List3= [4, [".......England", "Aus", 0 ] ]
l1=[]
# for lup in List1:
#     if lup.isalnum():
#         l1.append(lup)
l1=[]
b=l1.append(List1[1])
b=l1.append(List2[2])
b=l1.append(List3[1][0])
b=l1.append(List3[1][1])
print(l1)

for i in l1:
    if i.isalnum() or i.isalpha():
        c=[]
        for j in i:
            if j.isalpha():
                c.append(j)
        print("".join(c))
        c=[]
    else:
        d=[]
        for k in i:
            if k.isalpha():
                d.append(k)
        print("".join(d))