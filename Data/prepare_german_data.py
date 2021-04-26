import pandas as pd

german_data_colnames = [
    "chk_acct", "duration", "credit_his", "purpose", "amount", "saving_acct",
    "present_emp", "installment_rate", "sex", "other_debtor", "present_resid",
    "property", "age", "other_install", "housing", "n_credits", "job",
    "n_people", "telephone", "foreign", "response"
]

df = pd.read_csv('..\\data_original\\german.data', header=None, delimiter=r"\s+", names=german_data_colnames)
df['GOOD'] = 2 - df['response']
df = df.drop(['response'], axis=1)
df.csv('..\\data_preprocessed\\german_data.csv', index=False)
