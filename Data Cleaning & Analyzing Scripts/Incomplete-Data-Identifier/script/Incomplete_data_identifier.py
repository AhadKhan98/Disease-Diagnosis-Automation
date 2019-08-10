#!/usr/bin/env python
# coding: utf-8

# In[38]:


import os

def write_missing(patient_id,missing):
    log_file = open("log.txt",'a')
    log_file.write('Patient ID: %s | Missing: %s\n' % (patient_id,missing))
    log_file.close()

files = []
for file in os.listdir():
    if '.txt' in file:
        files += [file]

patient_ids = []
for f in files:
    patient_id = f.split('_')[0]
    data = open(f,'r').readlines()
    data = list(map(str.strip,data))

    for line in range(len(data)):
        if 'ATTACH' in data[line]:
            try:
                sitename = int(data[line+1][10:])
            except ValueError:
                if patient_id not in patient_ids:
                    patient_ids += [patient_id]
                sitename = 'SITENAME'
                write_missing(patient_id,sitename)

            try:
                section = int(data[line+2][9:])
            except ValueError:
                if patient_id not in patient_ids:
                    patient_ids += [patient_id]
                section = 'SECTION'
                write_missing(patient_id,section)
            try:
                value1 = int(data[line+3][8:])
            except ValueError:
                if patient_id not in patient_ids:
                    patient_ids += [patient_id]
                value1 = 'VALUE1'
                write_missing(patient_id,value1)
            try:
                value2 = int(data[line+4][8:])
            except ValueError:
                if patient_id not in patient_ids:
                    patient_ids += [patient_id]
                value2 = 'VALUE2'
                write_missing(patient_id,value2)
            try:    
                value3 = int(data[line+5][8:])
            except ValueError:
                if patient_id not in patient_ids:
                    patient_ids += [patient_id]
                value3 = 'VALUE3'
                write_missing(patient_id,value3)

                
for pid in patient_ids:
    copy_to_xl_file = open("copy_to_xl.txt",'w')
    copy_to_xl_file.write(pid+'\n')
    copy_to_xl_file.close()

log_file = open("log.txt",'a')
log_file.write('\n\n\n Unique Patients Missing Information: %s' % len(patient_ids))
log_file.close()

