#!/usr/bin/env python
# coding: utf-8

# In[27]:


import os


# In[31]:


files = [] # Stores a list of all text files in the current directory
for f in os.listdir():
    if '.txt' in f:
        files += [f]
try:
	files.remove('log_file.txt') # Removes log file from array if it exists
	files.remove('master_file.txt') # Removes master file from array if it exists
except ValueError:
	pass

log_file = open('log_file.txt','w') 
master_file = open('master_file.txt','w')
master_file.write('NDBPRN_ID\tcounter_id\tpatient_id\tdate_created\tdate_modified\tmodified_by\tphysicians_care_YN\tphysicians_care_notes\thospitalized_YN	hospitalized_notes\tserious_injury_YN\tserious_injury_notes\tmedications_YN\tmedications_notes\tphen_fen_YN\ttobacco_YN\tdiet_YN\tsubstances_YN\tother_illness_YN\tother_illness_notes\tdiseases\tallergies_notes\tcomments\tfosamax_yn\n')

total_entries = 0 # Keeps count of the number of lines that were copied from all text files excluding header rows

for f in files: # Runs the following code for all text files
    data = open(f,'r').readlines()
    del(data[0]) # Removes the header from the data
    for line in data: # Reads each line in the file
        master_file.write(line) # Writes the line to the master file
    total_entries += len(data) # Adds the total lines in the files excluding the header row to the total_entries variable
    log_file.write('Successfully copied %s entries from file: %s\n' % (len(data),f)) # Ouputs to the log file
log_file.write('Total Entries Copied: %s' % total_entries)
master_file.close()
log_file.close()

