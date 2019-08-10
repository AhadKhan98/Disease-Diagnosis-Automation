#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os,re

unknown_files = []
known_files = []
known_pids = []

#Stores Unknown Files
for file in os.listdir():
    if re.search('.txt',file):
        unknown_files += [file]
        
#Stores Known Files
for file in os.listdir('Knowns'):
    if re.search('.txt',file):
        known_files += [file]
        
for file in known_files:
    known_pids += [file.split('_')[0]]


# In[7]:


def write_to_file(file_name,content):
    file = open(file_name,'w')
    for line in content:
        file_name.write(str(line))
    file.close()

def check_and_copy(file_content):
    to_copy = []
    line = 0
    for f in file:
        if 'ATTACH' in f:
            to_copy += [file[line:line+6]]
            line += 6
    return to_copy


# In[8]:



for i in range(len(unknown_files)):
    pid = unknown_files[i].split('_')[0]
    if pid in known_pids:
        indexat = known_pids.index(pid)
        known_file_content = open("Knowns/"+known_files[indexat],'r').readlines()
        copy = []
        count = 0
        for line in known_file_content:
            if 'ATTACH' in line:
                copy += known_file_content[count:count+6]
                count += 6
        
        unknown_file_content = open(unknown_files[i],'a')
        for item in copy:
            unknown_file_content.write(str(item))
        unknown_file_content.close()
        
    
    
        

