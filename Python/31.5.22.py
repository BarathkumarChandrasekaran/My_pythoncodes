# num = 1
# pdt = 1
# while(num<=10):
#     pdt = pdt * num
#     print(pdt)
#     num+=1
#     if pdt >=2679:
#         print(num)

# i=0
# pdt=0
# while(i<=300):
#     i += 1
#     j=0
#     while(j<=9):
#         j += 1
#         pdt = i*j
#         if pdt >= 2679:
#            break
#         print(i, j)

l1 =[["a","b","c"],[1,2,"c"],[3,1,"c"]]
# cnt=0
# for iter1 in l1:
#     for iter2 in iter1:
#         if iter2 == "c":
#             for i in iter2:
#                 cnt+=i.count("c")
# print(cnt)
newlist =[]
for iter1 in l1:
    for iter2 in iter1:
        newlist.append(iter2)
print(newlist)
for i in newlist:
    if newlist.count(i)>2:
        break
print(i)