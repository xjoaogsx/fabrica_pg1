import pandas as pd
import numpy as np

df_prod = pd.read_excel('files/master.xlsx', engine='openpyxl')
df_branch = pd.read_excel('files/master.xlsx', engine='openpyxl')

compare_values = df_prod.values == df_branch.values

print(compare_values)

rows, cols = np.where(compare_values == False)

for item in zip(rows, cols):
    df_prod.iloc[item[0], item[1]] = '{} --> {}' .format(df_prod.iloc[item[0], item[1], df_branch.iloc[item[0], item[1]]])

df_prod.to_excel('files/output.xls', index=False, header=True)