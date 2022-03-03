class rect:
    def __init__(self, l1, b1):
        self.l = l1
        self.b = b1

    def area(self):
        self.a = self.l * self.b

    def peri(self):
        self.p = 2 * (self.l + self.b)

    def disp(self):
        print("Area of rectangle \n", self.a)
        print("Perimeter of rectangle \n", self.p)

    def compare(self, obj):
        if self.a == obj.a:
            print("Areas are equal")
        elif self.a > obj.a:
            print("Area1 is greater than area2 ")
        elif self.a < obj.a:
            print("Area2 is greater than area1 ")


a = int(input("Enter length 1 "))
b = int(input("Enter breadth 1 "))
c = int(input("Enter length 2 "))
d = int(input("Enter breadth 2 "))

r1 = rect(a, b)
r2 = rect(c, d)

r1.area()
r1.peri()
r1.disp()

r2.area()
r2.peri()
r2.disp()

r1.compare(r2)
