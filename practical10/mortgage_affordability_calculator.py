#write a function which determines whether an individual can buy a specific house. 
#two parameters: 
#(1) the total value of the house = value
#(2) the purchaser’s annual salary = salary
# value <= 5*salary
class calculatorclass:
    def __init__(self,value,salary):#define the attributes
        self.value=value
        self.salary=salary
    def print_details(self): #to define the print of attributes
        print(f'value={self.value}, salary={self.salary}')
    def mortgage_affordability_calculator(self):
        '''determines whether an individual can buy a specific house, i.e. the value of the house <= 5*salary'''
        if isinstance(self.value, (int, float)) and isinstance(self.salary, (int, float)): #to determine if x ans y are numbers
            if self.value <= 5*self.salary : #if it is true, can buy
                return 'can buy the house'
            else : #if it is not true, can not buy
                return 'can not buy the house'
        else:
            print("Error: value and salary must be numbers.")

#example
a=calculatorclass(18000,35000)
a.print_details()
a.mortgage_affordability_calculator()



