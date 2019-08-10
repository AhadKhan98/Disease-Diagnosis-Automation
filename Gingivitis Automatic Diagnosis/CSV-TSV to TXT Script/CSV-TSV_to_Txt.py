#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
CSV/TSV TO TEXT FILE 

This script allows the user to create a text file for every patient based on a tsv or a csv file containing the data.

Author: Ahad Zai

"""
file_name = input("Enter File Name: ")
file_ext = file_name[-4:]
data = open(file_name,'r').readlines()
data = list(map(str.strip,data))
data = list(map(lambda item: item.replace('"',''),data)) # Replaces all of the double quote characters from the 'data' variable
has_header = input("Does the file have an identifying header? Y or N: ")
if has_header.lower() == 'y':
    del(data[0])
for i in range(len(data)):
    if file_ext.lower() == '.csv':
        patient_data = data[i].split(',') # Converts each line into a list separated by ','
    elif file_ext.lower() == '.tsv':
        patient_data = data[i].split('\t') # Converts each line into a list separated by 'TAB'
    patient_id = patient_data[1]
    date = patient_data[3]
    percond = patient_data[4]
    sitename = patient_data[5]
    section = patient_data[6]
    v1 = patient_data[7]
    v2 = patient_data[8]
    v3 = patient_data[9]
    file_name = ('%s_%s.txt' % (str(patient_id),str(date)))
    output_file = open(file_name,'a')
    output_file.write('PerCond: %s\nSiteName: %s\nSection: %s\nValue1: %s\nValue2: %s\nValue3: %s\n' % (percond,sitename,section,v1,v2,v3))
    output_file.close()
print("Completed!")

