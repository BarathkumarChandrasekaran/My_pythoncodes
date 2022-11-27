import re
txt = "The rain in spain"
# i = input("Enter the string:")
o = re.findall("ai",txt)
print(o)
print(len(o))

o = re.findall("z",txt)
print(o)

print("--------------------------------------------------------")
str1 = "xyz abc xyz abc"
o1 = re.search("a",str1)
print(o1)

o1 = re.search("n",str1)
print(o1)

print("--------------------------------------------------------")

o = re.split("\s",str1)
print(o)

o = re.split("\s",str1,2)
print(o)

print("--------------------------------------------------------")

o=re.sub("\s","#",str1)
print(o)


str1 = "20012344"
for i in range(len(str1)):
    l = len(str1)
    for j in range(1,l+1):
        res = str1[l-j]
        print(res)
    break
