#!/usr/bin/env python
# coding: utf-8

# In[13]:


"""
CSV/TSV TO TEXT FILE 
This script allows the user to create a text file for every patient based on a csv or a tsv file containing the data.
Author: Ahad Zai

"""
file_name = input("Enter File Name: ")
file_ext = file_name[-4:]
data = open(file_name,'r').readlines()
data = list(map(str.strip, data)) # Removes the newline characters from the data
data = list(map(lambda item: item.replace('"',''),data)) # Replaces all of the double quote characters from the 'data' variable
has_header = input("Does the file have an identifying header? Y or N: ")
if has_header.lower() == 'y':
    del(data[0]) # Deletes the header of the file
    
line = 0 # Used to iterate through the lines in the data
for i in data:
    if file_ext == '.csv':
        entry = data[line].split(',') # Converts the string into a list
    elif file_ext == '.tsv':
        entry = data[line].split('\t')
    date_filename = entry[3].replace("/","")
    output_file = open(entry[1] + '_' + date_filename + ".txt",'a')
    output_file.write("PerCond: " + entry[4] + "\n")
    output_file.write("SiteName: " + entry[5] + "\n")
    output_file.write("Section: " + entry[6] + "\n")
    output_file.write("Value1: " + entry[7] + "\n")
    output_file.write("Value2: " + entry[8] + "\n")
    output_file.write("Value3: " + entry[9] + "\n")
    output_file.close()
    line += 1

