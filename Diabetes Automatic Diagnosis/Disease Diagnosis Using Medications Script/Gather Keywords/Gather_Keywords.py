#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os


# In[10]:


df = pd.read_excel('keywords.xlsx')
txt_file = open('keywords.txt','w')
for item in df['Keywords']:
    txt_file.write(item + '\n')
txt_file.close()

