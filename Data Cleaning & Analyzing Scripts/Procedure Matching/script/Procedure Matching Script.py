#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


df_diabetes = pd.read_excel('ALL_Cases.xlsx',sheet_name=0)
df_procedures = pd.read_excel('Procedures.xlsx',sheet_name=0)
df_procedures['Offset Date'] = df_procedures['ModifiedDateTime'].apply(lambda x: x-pd.DateOffset(years=1))


# In[ ]:


def get_index(patient_id):
    return df_procedures.index[df_procedures['IRB_ID'] == patient_id].tolist()


# In[ ]:


for i in range(len(df_diabetes)):
    found = False
    patient_id = df_diabetes['Patient ID'][i]
    date = df_diabetes['Date'][i]
    pos_in_procedures = get_index(patient_id)
    
    for position in pos_in_procedures:
        offset_date = df_procedures['Offset Date'][position]
        if (('D0150' in df_procedures['Procedure'][position]) and (date >= offset_date and date <= df_procedures['ModifiedDateTime'][position])):
            found = True
            df_diabetes['Procedure Code Date'][i] = df_procedures['ModifiedDateTime'][position]
            df_diabetes['Found'][i] = 'TRUE'
            break
        else:
            found = False
            continue
    if found == False:
        df_diabetes['Found'][i] = 'FALSE'


# In[ ]:


df_diabetes.to_excel('new.xlsx',sheet_name='Sheet1')

