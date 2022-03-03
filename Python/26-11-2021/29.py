str1 = input("Enter a string ")
str2 = str1.split(" ")
print(str2)
a = str2[0]
b = str2[-1]
a1 = a[0]
b1 = b[0]
a2 = a[1:]
b2 = b[1:]
o1 = b1 + a2
o2 = a1 + b2
lst1 = [o1, o2]
print(lst1)
