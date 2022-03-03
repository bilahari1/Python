a = 0
b = 1
s = 0
c = int(input("Enter the limit "))
print("Fibonacci series")
print(a)
print(b)
for i in range(1, c):
    s = a + b
    print(s)
    a = b
    b = s
    c = c + 1
