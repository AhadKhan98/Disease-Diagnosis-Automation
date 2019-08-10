#!/usr/bin/env python
# coding: utf-8

# In[43]:


import os
from xml.etree import ElementTree # Used to parse XML files

files = []
for file in os.listdir('XMLs'):
    if '.xml' in file:
        files += [file]

keywords_type_concept = []
keywords_disease_concept = []

for f in files: # Iterates through all the files contained in the XMLs folder
    data = ElementTree.parse('XMLs/'+f)
    entry = data.findall('classMention/mentionClass') # Finds all elements containing the keyword that was highlighted in eHost
    for e in entry:
        if e.get('id') == 'Diabetes_Type_Concept': # Checks the concept for the element
            if e.text not in keywords_type_concept: 
                keywords_type_concept += [e.text]
                continue
        elif e.get('id') == 'Diabetes_Disease_Concept':
            if e.text not in keywords_disease_concept:
                keywords_disease_concept += [e.text]
                continue

            
output_file = open('keywords.txt','a')
output_file.write('Keywords for Disease Concept: ')
for item in keywords_disease_concept:
    output_file.write(item+', ')
output_file.write('\n\nKeywords for Disease Type Concept: ')
for item in keywords_type_concept:
    output_file.write(item+', ')
output_file.close()

