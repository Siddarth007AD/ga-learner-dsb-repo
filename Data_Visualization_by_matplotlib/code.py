# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path) 

loan_status = data['Loan_Status'].value_counts()
print(loan_status)

plt.figure(figsize=[10,15])
plt.xlabel('loan Status')
plt.ylabel('Number of amount')
plt.title('counting of loan status')
loan_status.plot(kind='bar')
#Code starts here


# --------------
#Code starts here

# group the data frame by property area and loan status 
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
# print(property_and_loan)

property_and_loan.plot(kind='bar')

# label of ploted graph 
plt.xticks(rotation=45, horizontalalignment="center")
plt.title(" Distributaion of property and loan")
plt.xlabel("Property Area")
plt.ylabel('Loan status')

# show graph
plt.show()


# --------------
#Code starts here



# group by education and loan status 
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
# print(education_and_loan)

education_and_loan.plot(kind='bar')

plt.xlabel('Education Status')
plt.ylabel("Loan Status")
plt.xticks(rotation=45)

plt.show()


# --------------
#Code starts here

# create a dataframe as graduate 

graduate = data[data['Education']=='Graduate']
# print(graduate)
not_graduate = data[data['Education']=='Not Graduate']
# print(not_graduate)

graduate['LoanAmount'].plot(kind='density',label='Graduate')

not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set(title='Applicant Income')


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_2.set(title='Coapplicant Income')


#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome']+ data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_3.set(title='Total Income')


#Code ends here


