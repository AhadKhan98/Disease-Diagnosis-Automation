#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Remove Duplicates Script: This script takes a csv file as an input and then finds the duplicates in the file and removes them.
The csv file must be sorted so that the duplicates appear in a line by line manner. The program then keeps track of the 
patient ids and the site names that had duplicates and outputs them in a separate file 'duplicates.txt'. It also generates a new
csv file containing cleaned data of the entered file.

Author: Ahad Zai

"""

file_name = input("Enter File Name: ")
data = open(file_name,'r').readlines()

has_header = input("Does file have identifying header? Y or N: ")
if has_header.lower() == 'y':
    del[data[0]]
    

deleted = 0
line = 0
duplicate_ids = []

while line != len(data)-1:
    current_line = data[line]
    next_line = data[line+1]
    if current_line == next_line:
        temp = str(data[line])
        temp = temp.split(',')
        to_add = "PtID: " + str(temp[1]) + " SiteName: " + str(temp[5])
        if not to_add in duplicate_ids:
            duplicate_ids += [to_add]
        del[data[line+1]]
        deleted += 1
    else:
        line+=1
print("%s duplicates removed | %s entries in output file" % (deleted,len(data)))

output_file_duplicates = open("duplicates.txt",'w')
for item in duplicate_ids:
    output_file_duplicates.write(item+"\n")
output_file_duplicates.close()

output_file = open(file_name+"_output.csv","w")
for item in data:
    output_file.write(str(item))
output_file.close()

