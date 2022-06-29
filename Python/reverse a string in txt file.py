f= open("D:/new.txt","r+")
str1 = ""
for i in f.readline():
    str1+=i
reversestr = str1[::-1]
str1=open("D:/new1.txt","w")
str1.write(reversestr)


