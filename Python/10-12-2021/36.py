n = int(input("Enter a number:"))


def factor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


print("Factors are: ")
factor(n)
