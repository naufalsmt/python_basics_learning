class School:
    stds = 100

    def students(self):
        print('There are hundred students in the class')

    def __init__(self, a, b):
        print('Iam calling automatically in this class')
        self.firstNumber = a
        self.secondNumber = b

    def summation(self):
        return self.firstNumber + self.secondNumber


    def summationVariable(self):
        return self.firstNumber + self.secondNumber + School.stds

obj1 = School(2, 3) # declare the object of the class
obj1.students() # call function within the object (class)
print(obj1.stds) # call and print the variable within the object (class)

summation1 = obj1.summation()
print(summation1)
summation2 = obj1.summationVariable()
print(summation2)

obj2 = School(4, 5)
summation3 = obj2.summation()
print(summation3)
summation4 = obj2.summationVariable()
print(summation4)