#pesudocode:
####### 1.import the dataset:
# import python libraries
# change working directory
# download the full_data.csv
# import the csv: read the content of csv file into a dataframe object

##### 2. working with dataframes
# see the beginning of the dataframe
# see the type of the data points, column numbers, and row numbers in covid_data
# describe the mean, standard deviation, range
# to see only specific value in the dataframe: iloc and loc

###### 3. examining the situation on 31 march
# date: 2023-03-31
# columns: location, new_cases, new_deaths
# save as separate objects
# numpy to compute the mean new cases and new deaths on 2023-03-31
# calculate the proportion
# draw the boxplot
# compare new cases and new deaths across the world



####### 1.import the dataset:

# import python libraries
import os # allow us to work with files and directories
import pandas as pd # to work with dataframes 
import matplotlib.pyplot as plt
import numpy as np

#  change the working directory with os.chdir
os.chdir('/Users/elaine/IBI/IBI1_2022-24/practical7')

# import the csv: read the content of csv file into a dataframe object
covid_data = pd.read_csv('full_data.csv')


##### 2. working with dataframes

# see the beginning of the dataframe
covid_data.head(5)
covid_data.head(10)

# see the type of the data points, column numbers, and row numbers in covid_data
covid_data.info()

# describe the mean, standard deviation, range
print(covid_data.describe ())

# to see only specific value in the dataframe: iloc and loc
# iloc use [] to pick the x,y: column index to locate names
covid_data.iloc[0,1]
covid_data.iloc[2,0:5]
covid_data.iloc[0:2,:]
covid_data.iloc[0:10:2,0:5]
covid_data.iloc[0:3,[0,1,3]]
# Booleans with same length as the number of columns in the dataframe
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]
# the “True” columns are showed
# loc use column names. but rows don’t have name, so still use numbers
covid_data.loc[2:4,'date']

# to find all total cases in ‘afghanistan’
# know 0-81 rows are afghanistan
covid_data.loc[0:81,'total_cases']
# want to find the afghanistan 
covid_data.loc[covid_data.loc[:,'location'] == 'Afghanistan','total_cases']


###### 3. examining the situation on 31 march
# date: 2023-03-31
# columns: location, new_cases, new_deaths
# save as separate objects
wanted_columns = [False, True, True, True, False, False]
new_data = covid_data.loc[covid_data.loc[:,'date']=='2020-03-31',wanted_columns]
print(new_data)

cases_deaths=new_data.iloc[:,1:3]

# numpy to compute the mean new cases and new deaths on 2023-03-31
# numpy instructions:  https://blog.csdn.net/u013250861/article/details/123965146?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_utm_term~default-0-123965146-blog-122905081.235^v27^pc_relevant_3mothn_strategy_recovery&spm=1001.2101.3001.4242.1&utm_relevant_index=2
np.mean(cases_deaths,axis=0)
###result:
###new_cases     640.461538
###new_deaths     37.928205
###dtype: float64
# different. 
# new cases are more than new deaths

# calculate the proportion
deaths_mean=np.mean(cases_deaths,axis=0)[1]
cases_mean=np.mean(cases_deaths,axis=0)[0]
proportion=deaths_mean/cases_mean
print(proportion)
###result: 0.05922011370005605

#draw the boxplot of new cases 
new_data.info()
cases=new_data.iloc[:,1]
plt.boxplot(cases)
plt.show()
## the box is at the place near zero. there are also points higher than that. the highest is more than 60000
## the orange line, 50% quantile, is between 5 and 7.5

#draw the boxplot of new deaths
new_deaths=new_data.iloc[:,2]
plt.boxplot(new_deaths)
plt.show()
## 50% quantile is 0
## highest is over 3500

# plot the data for the whole world over time
world_dates=covid_data.loc[covid_data.loc[:,'location'] == 'World','date']
world_new_cases=covid_data.loc[covid_data.loc[:,'location'] == 'World','new_cases']
plt.plot(world_dates, world_new_cases,'b+') #b+ means use blue and + sign to mark the points

# compare new cases and new deaths across the world
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90) #0:len(world_dates):4 uses slicing to select elements from the world_dates variable. In this case, the slice indicates starting from index 0 and going up to the last element of world_dates, with a step size of 4. This means that every 4th element is selected as a tick position for the x-axis labels.
# rotation=-90：Rotate the x-axis tick labels counterclockwise by 90 degrees.
plt.show()


##### new question: Are there places in the World where there have been more than 10,000 total infections (as of 31 March)? If so, where are they?
#find the rows that have more than 10000 deaths on March 31
places = new_data.loc[new_data['new_cases'] > 10000, 'location']
##result:
##7717    United States
##7971            World
##Name: location, dtype: object

