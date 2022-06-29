m1 = {1:[0,1,2,[0,3,2]],2:{0:[1,2],1:[2]}}
sum = 0
for key in m1:
    if type(m1[key]) == list:
        for j in m1[key]:
            if type(j) == list:
                for k in j:
                    sum = sum+k
            else:
                sum = sum+j

    if type(m1[key]) == list:
        for x in m1[key]:
            if type(x) == list:
                for y in x:
                   sum=sum+y
print(sum)

