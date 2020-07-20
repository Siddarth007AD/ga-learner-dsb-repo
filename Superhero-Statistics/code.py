# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

# replace '-' by 'Agender' by using replace funcation in gender colom
data['Gender'].replace('-','Agender', inplace=True)

# count the value of gender
gender_count = data['Gender'].value_counts()
plt.bar(gender_count.index, gender_count)
print(gender_count)
plt.xlabel("Gender")
plt.ylabel("Count of People")
plt.title("Count of People by Gender");
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
plt.bar(alignment.index,alignment)
plt.title("Character Alignment")
plt.show()


# --------------
#Code starts here

#Subsetting the data with columns ['Strength', 'Combat']
sc_df = data[['Strength','Combat']].copy()

#Finding covariance between 'Strength' and 'Combat'
sc_covariance = sc_df.cov().iloc[0,1]

#Finding the standard deviation of 'Strength'
sc_strength = sc_df['Strength'].std()

#Finding the standard deviation of 'Combat'
sc_combat = sc_df['Combat'].std()

#Calculating the Pearson's correlation between 'Strength' and 'Combat'
sc_pearson = sc_covariance/(sc_combat*sc_strength)

print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)


#Subsetting the data with columns ['Intelligence', 'Combat']
ic_df = data[['Intelligence','Combat']].copy()

#Finding covariance between 'Intelligence' and 'Combat'
ic_covariance = ic_df.cov().iloc[0,1]

#Finding the standard deviation of 'Intelligence'
ic_intelligence = ic_df['Intelligence'].std()

#Finding the standard deviation of 'Combat'
ic_combat = ic_df['Combat'].std()

#Calculating the Pearson's correlation between 'Intelligence' and 'Combat'
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)

#Code ends here


# --------------
#Code starts here

# fine the quantile=0.99 value of 'total' column
total_high = data['Total'].quantile(q=0.99)
print(total_high)

# Subsetting the dataframe based on "total_hight"
super_best = data[data['Total']>total_high]
print(super_best)
# Creating a list of 'Name' associated with the "super_best"
super_best_names = list(super_best['Name'])

# printing the names
print(super_best_names)

# code ends here 


# --------------
#Code starts here

# Create subplots 
# fig, ax_1, ax_2, ax_3 
fig, ax_1 = plt.subplots()
ax_1.boxplot(super_best['Intelligence'])
plt.title('Intelligence')
plt.show()

fig, ax_2 = plt.subplots()
ax_2.boxplot(super_best['Speed'])
plt.title('Speed')
plt.show()

fig, ax_3 = plt.subplots()
ax_3.boxplot(super_best['Power'])
plt.title('Power')
plt.show()


