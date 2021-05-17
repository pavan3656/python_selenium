class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("getting")


    def getData(self):
        print("i am getting pavankumar")
    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())
