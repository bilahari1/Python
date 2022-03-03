class bank:
    def __init__(self, a1, n1, t1, b1):
        self.a = a1
        self.n = n1
        self.t = t1
        self.b = b1

    def disp(self):
        print("Ac no:", self.a)
        print("Name:", self.n)
        print("Type:", self.t)
        print("Balance:", self.b)

    def depo(self, am1):
        self.b += am1
        print("Balance : ", self.b)

    def wi(self, am2):
        if self.b < am2:
            print("Invalid")
        else:
            self.b -= am2
            print("Balance : ", self.b)


a = int(input("Enter account number "))
n = input("Enter name ")
t = input("Enter the type of account ")
b = int(input("Enter balance "))
b1 = bank(a, n, t, b)
b1.disp()
a1 = int(input("Enter the amount to be deposited : "))
b1.depo(a1)
a2 = int(input("Enter the amount to be withdrawn : "))
b1.wi(a2)
