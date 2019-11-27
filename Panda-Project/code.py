# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

bank =pd.pandas.read_csv(path, sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
categorical_var=bank.select_dtypes(include = 'object')
print('categorical_var')

numerical_var = bank.select_dtypes(include = 'number')
print('numerical_var')


# code starts here






# code ends here


# --------------
# code starts here
bank.drop(['Loan_ID'],axis=1,inplace=True)
banks =bank.copy()

print(banks.isnull().sum())
bank_mode = bank.mode()
banks = banks.fillna(bank_mode.T.squeeze())
banks.head()
print(banks)
#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(
                 values = 'LoanAmount',
                 index = ['Gender','Married','Self_Employed'],
                 aggfunc=np.mean)

print(avg_loan_amount)



# code ends here



# --------------
# code starts here
"""
loan_approved_se = banks['Self_Employed' == Yes and Loan_Status == Yes].valuecounts()
print(loan_approved_se)
loan_approved_nse= banks[Self_Employed == No and Loan_Status == Yes].counts()
print(loan_approved_nse)
#loan_approval = df['Loan_Status'].value_counts()['Y']
#print(loan_approval)

#percentage_se = (loan_approved * 100 / 614)
print(percentage_se)

#percentage_nse = (loan_approved * 100 / 200)
print(percentage_nse)
# code ends here
"""
SelfE_df= banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_se=SelfE_df['Self_Employed'].count()
print(loan_approved_se)

SelfNE_df= banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse=SelfNE_df['Self_Employed'].count()
print(loan_approved_nse)

percentage_se=(loan_approved_se/614)*100;
percentage_nse=(loan_approved_nse/614)*100;

print(percentage_nse);
print(percentage_se)



# --------------
# code starts here
import calendar


loan_term=(banks['Loan_Amount_Term']).apply(lambda x:(x/12));
print(loan_term)
big_loan_term=loan_term[loan_term>=25].count()
print(big_loan_term)



#big_loan_term = df['Loan_Amount_Term'].apply(lambda x: if (x, loan_term >= 25 ) else None)
#print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)
print(loan_groupby)



# code ends here


