#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
CSV/TSV TO TEXT FILE 
This script allows the user to create a text file for every patient based on a csv or a tsv file containing the data.
Author: Ahad Zai

"""
file_name = input("Enter File Name: ")
file_ext = file_name[-4:]
data = open(file_name,'r').readlines()
data = list(map(str.strip,data)) # Removes newline characters from the list
has_header = input("Does the file have an identifying header? Y or N: ")
if has_header.lower() == 'y':
    del(data[0]) # Deletes identifying columns
for i in range(len(data)):
    if file_ext == '.csv':
        patient_data = data[i].split(',')
    elif file_ext == '.tsv':
        patient_data = data[i].split('\t')
    patient_id = patient_data[0]
    date = patient_data[1]
    try:
        description = patient_data[2]
    except IndexError:
        description = ''
    output_file = open("%s_%s.txt" % (patient_id,date),'w')
    output_file.write(description)
    output_file.close()
print('completed')

