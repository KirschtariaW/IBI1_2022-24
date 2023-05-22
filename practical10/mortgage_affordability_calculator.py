#write a function which determines whether an individual can buy a specific house. 
#two parameters: 
#(1) the total value of the house = value
#(2) the purchaser’s annual salary = salary
# value <= 5*salary

def mortgage_affordability_calculator(value, salary):
    '''determines whether an individual can buy a specific house, i.e. the value of the house <= 5*salary'''
    if value <= 5*salary : #if it is true, can buy
        return 'can buy the house'
    else : #if it is not true, can not buy
        return 'can not buy the house'

