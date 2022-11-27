import re

txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


txt = "The rain in Spain"
x = re.search("\s", txt) ##\s --> space

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt,1)
print(x)


txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

import re

txt = "The Sain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())


txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)


txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)


txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)



txt = "The hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
print(x)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")



txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")




txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)



txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)



txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")




txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt) #\A starts with

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")




txt = "ain't The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt) #\b -> beginning

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")





txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")




txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")




txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



txt = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")




txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")




txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
