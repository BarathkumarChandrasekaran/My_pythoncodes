l1 =[["a","b","c"],[1,2,"c"],[3,1,"c"]]

newlist =[]
for iter1 in l1:
    for iter2 in iter1:
        newlist.append(iter2)
print(newlist)
for i in newlist:
    if newlist.count(i)>2:
        break
print(i)
