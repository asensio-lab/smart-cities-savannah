import numpy as np
import pandas as pd
import os

names = os.listdir('assessed_values')

df_assessed = pd.DataFrame()
df_appraised = pd.DataFrame()
df_tax = pd.DataFrame()
df_sales = pd.DataFrame()

def merge_parts(df, directory, id_):
    df_part = pd.read_csv(directory)
    if ('tax' in directory):
        df_part = df_part.iloc[:-1]
    df_part['PARID'] = id_[:-4]
    df = df.append(df_part)
    return df
    
for id_ in names:
    df_assessed = merge_parts(df_assessed, ('assessed_values\\' + id_), id_)
    df_appraised = merge_parts(df_appraised, ('appraised_values\\' + id_), id_)
    df_tax = merge_parts(df_tax, ('tax\\' + id_), id_)
    df_sales = merge_parts(df_sales, ('sales\\' + id_), id_)   
    
df_assessed.to_csv('df_assessed.csv', index=False)
df_appraised.to_csv('df_appraised.csv', index=False)
df_tax.to_csv('df_tax.csv', index=False)
df_sales.to_csv('df_sales.csv', index=False)