#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re


# In[3]:


files = []
try:
    os.mkdir("Unknown_Cases")
except FileExistsError:
    pass
for file in os.listdir():
    if re.search('.txt',file):
        files += [file]


# In[ ]:


for i in range(len(files)):
    data = open(files[i],"r").readlines()
    data = list(map(str.strip,data))
   
    attach_sites = 0
    pocket_sites = 0
    
    for line in range(len(data)):
        if 'ATTACH' in data[line]:
            attach_sites += 1
        if 'POCKET' in data[line]:
            pocket_sites += 1
    
    if attach_sites == 0 or pocket_sites == 0:
        os.rename(files[i],"Unknown_Cases/"+files[i])

