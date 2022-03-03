lst = []
lst1 = []
n = int(input("Enter the number of words "))
for i in range(0, n):
    str = input("Enter the data ")
    lst.append(str)
print("List is: ", lst)


def long(l):
    for i in l:
        str1 = len(i)
        lst1.append(str1)

    print("Length:", lst1)

    for i in lst1:
        a = max(lst1)
    return a


b = long(lst)
print("Length of longest word", b)