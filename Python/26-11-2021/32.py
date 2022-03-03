n = int(input("Enter the limit "))
l = []
print("Enter the values ")
for i in range(0, n):
    e = int(input())
    l.append(e)
print(l)
s = 0
for i in l:
    s = s + i
print("Sum = ", s)
