# for k in range(0,50):
#     if (k%3==0) and (k%6==0) and (k%7==0):
#         print(k)
#
a=[]
k=0
while(k<=50):
    k += 1
    if (k%3==0) and (k%6==0) and (k%7==0):
        print(k)
        for i in str(k):
            a.append(i)
        print(a)
        print(int(a[0])+int(a[1]))