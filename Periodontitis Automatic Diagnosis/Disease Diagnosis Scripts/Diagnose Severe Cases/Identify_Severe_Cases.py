#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os 
import re


# In[27]:


files = []
try:
    os.mkdir("Severe_Cases")
    os.mkdir("Others")
except FileExistsError:
    pass
for file in os.listdir():
    if re.search('.txt',file):
        files += [file]


# In[28]:


for i in range(len(files)):
    data = open(files[i],"r").readlines()
    data = list(map(str.strip,data))
    sites_affected_attach = 0
    sites_affected_pocket = 0

    for line in range(len(data)):
        if 'ATTACH' in data[line]:
            current_sitename = data[line+1][10:]
            try:
                next_sitename = data[line+7][10:]
            except IndexError:
                break

            if current_sitename == next_sitename:
                all_values = []
                try:
                    all_values += [int(data[line+3][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+4][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+5][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+9][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+10][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+11][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                if max(all_values) >= 6:
                    sites_affected_attach += 1
                all_values = []
            else:
                continue


    for line in range(len(data)):
        if 'POCKET' in data[line]:
            current_sitename = data[line+1][10:]
            try:
                next_sitename = data[line+7][10:]
            except IndexError:
                break

            if current_sitename == next_sitename:
                all_values = []
                try:
                    all_values += [int(data[line+3][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+4][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+5][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+9][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+10][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                try:
                    all_values += [int(data[line+11][8:])] # Adds value1
                except ValueError:
                    all_values += [0]
                if max(all_values) >= 5:
                    sites_affected_pocket += 1
                all_values = []
            else:
                continue


    if sites_affected_attach >= 2 and sites_affected_pocket >= 1:
        os.rename(str(files[i]),"Severe_Cases/"+str(files[i]))
    else:
        os.rename(str(files[i]),"Others/"+str(files[i]))

