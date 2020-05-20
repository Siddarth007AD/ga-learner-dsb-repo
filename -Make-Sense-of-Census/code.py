# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data, new_record), axis=0)
print(census)



# --------------
#Code starts here
age = census[:,0]
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]
print(race_list)
#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))
print(minority_race)
#Code ends here


# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here
# calculate the high paid employee
high = census[census[:,1]>10]
print(high)

# calculate the low paid employee
low = census[census[:,1]<=10]
print(low)

# find the mean of high paid sallary
avg_pay_high = high.mean(axis=0)[7]
print(avg_pay_high)

# find the mean of high paid sallary
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_high)

# check ad compare both the values for education leads to better pay
if(avg_pay_high == avg_pay_low):
    print("True")
    print("yes it is truth in better education leads to better pay")




