from oopsdemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator. __init__(self, 2, 20)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = ChildImpl()
print(obj.getCompleteData())
