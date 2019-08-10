#!/usr/bin/env python
# coding: utf-8

# In[36]:


import os
from xml.etree import ElementTree
import xlsxwriter


# In[41]:


workbook = xlsxwriter.Workbook('Golden_Standard.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'Patient ID',)
worksheet.write(0,1,'Disease_Concept',)
row = 1
files = []
for f in os.listdir():
    if '.xml' in f:
        files += [f]

for f in files:
    data = ElementTree.parse(f)
    entry = data.findall('stringSlotMention/stringSlotMentionValue')
    list_entry = [e.get('value') for e in entry]
    num_yes = list_entry.count('Yes')
    num_yes += list_entry.count('Type I')
    num_yes += list_entry.count('Type II')
    num_no = list_entry.count('No')
    if num_yes == 0 and num_no == 0:
        golden_standard = 'None'
    elif num_yes > num_no:
        golden_standard = 'Yes'
    elif num_yes < num_no:
        golden_standard = 'No'
    else:
        golden_standard = 'Unknown'
    patient_id = f.split('_')[0]
    worksheet.write(row,0,str(patient_id))
    worksheet.write(row,1,golden_standard)
    row += 1

workbook.close()

