from oops_demo import School

class Building(School): # inherit other file class Shool in this class Building
    digit = 120

    def __init__(self):
        School.__init__(self, 10, 20) # declare the variable a & b from class School of another file


    def corporation(self):
        return self.digit + self.stds + self.summationVariable() # variable in this class Building + variable in other
                                                                 # file class School + call function from class School


obj5 = Building() # create object for this class
print(obj5.corporation())