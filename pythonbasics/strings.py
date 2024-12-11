mystr="python is Programming Language"
print(mystr)
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())
print(mystr.endswith("a"))
print(mystr.endswith("Language"))
print(mystr.endswith("e"))
print(mystr.startswith("python"))
print(mystr.count('o'))
print(mystr.count(' '))
print(mystr.find('p'))
print(len(mystr))


'''
"python is Programming Language"
p-0
y-1
t-2
h-3
'''

print(mystr[0])
print(mystr[1])
print(mystr[2])
print(mystr[3])
print(mystr[4])
print(mystr[5])
# print(mystr[30])

print(mystr.casefold())
print(mystr.isalnum())
mystr=mystr.replace("python","java")
print(mystr)