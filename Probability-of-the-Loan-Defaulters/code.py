# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)

total = len(df['fico'])
# print(total)

# Number of fico which is less than 700
length = len(df.loc[df['fico'] >= 700])
# print(length)

p_a = length/total
# p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print("probablity of event that fico is > than 700 : ", p_a)

# length of purpose 
total = len(df['purpose'])
print(total)

# probability of purpose == debt_consolidation
p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print("probability of purpose == debt_consolidation", p_b)


# Create new dataframe for condition ['purpose']== 'debt_consolidation' 
df1 = df[df['purpose'] == 'debt_consolidation']
print(df1)

# Calculate the P(A|B)
p_a_b = df1[df["fico"].astype(float) > 700].shape[0]/df1.shape[0]
print(p_a_b)

# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
# code starts here
#  probability p(A) for the event that paid.back.loan == Yes
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
print(prob_lp)

#  probability p(B) for the event that credit.policy == Yes
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
print(prob_cs)

new_df =  df[df['paid.back.loan'] == 'Yes']
# print(new_df)

prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)

bayes =  (prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# create bar plot for purpose
df.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution of Purpose")
plt.ylabel("Probability")
plt.xlabel("Number of Purpose")
plt.show()

#create new dataframe for paid.back.loan == 'No'
df1= df[df['paid.back.loan'] == 'No']

# plot the bar plot for 'purpose' where paid.back.loan == No 
df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution of Purpose")
plt.ylabel("Probability")
plt.xlabel("Number of Purpose")
plt.show()


# --------------
# code starts here

inst_median = df['installment'].median()
print(inst_median)
inst_mean = df['installment'].mean()
print(inst_mean)

df['installment'].hist(normed = True, bins=50)
df['log.annual.inc'].hist(normed = True, bins=50)
# code ends here


