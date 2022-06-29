val = "Male-40,Female-21,Female-31,Male-25,Male-35"
b=val.replace("-",",")
b=b.split(",")
# print(b)
d=[[],[]]
for i in range(0,len(b)):
    if b[i] == "Male":
        d[0].append(b[i+1])
    if b[i] == "Female":
        d[1].append(b[i+1])
print(d)



