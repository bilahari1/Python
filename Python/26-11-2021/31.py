n = int(input("Enter the limit "))
lst1 = []
print("Enter the values ")
for i in range(0, n):
    e = int(input())
    lst1.append(e)
print(lst1)
lst2 = []
for i in lst1:
    if i % 2 != 0:
        lst2.append(i)

print(lst2)
