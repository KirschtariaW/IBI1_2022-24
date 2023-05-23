#  store the records for their members’ times in local triathlon competitions
# a new Python class that can be used to contain 
# information about individual athletes 
# and their recorded times for each of the three disciplines (swim, cycle, run).

# Create a class called ‘triathlon’ contains
# person’s first name,
# and last name, 
# the location at which the competition took place, 
# the person’s time for each of the three disciplines  (swim, cycle, run),
# and the person’s total time over the triathlon. 

class triathlon:
    def __init__(self,first_name, last_name, location, swim_time, cycle_time, run_time):# initialize the attributes
        # just the attributes that need to be put initially need to be in the ()
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        #if don't need to be put in initially, can get from other attributes, it don't need and cannot put into the ()
        self.total = swim_time + cycle_time + run_time
    #print the details
    def print_details(self):
        # the unit of time: min
        print(f"the athlete's name is {self.first_name} {self.last_name}, location is {self.location}, swim time is {self.swim_time}min, cycle time is {self.cycle_time}min, run time is {self.run_time}min, total time is {self.total}min")



#example
example=triathlon('J','D','F',2,4,5)
example.print_details()
example.first_name