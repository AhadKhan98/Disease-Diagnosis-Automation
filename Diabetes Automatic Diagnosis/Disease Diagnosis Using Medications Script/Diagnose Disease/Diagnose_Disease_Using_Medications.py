#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import xlsxwriter
from fuzzywuzzy import fuzz


def get_id_date(file):
    patient_id = file.split('_')[0]
    date = file.split('_')[1].replace('.txt','')
    return (patient_id,date)

def add_to_log(pid,date,matched_keywords):
    log_file = open('log.txt','a')
    log_file.write('Patient ID: %s | Date: %s | Matched Keywords: %s \n' % (pid,date,matched_keywords))
    log_file.close()

def main():
    workbook = xlsxwriter.Workbook('Results.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0,'Patient ID')
    worksheet.write(0,1,'Date')
    worksheet.write(0,2,'Medications')
    worksheet.write(0,3,'Diagnosis')
    row = 1
    col = 0
    keywords_file = open('keywords.txt','r')
    keywords = keywords_file.readlines()
    keywords = [item.strip() for item in keywords]
    files = []
    for f in os.listdir('patient_files'):
        if '.txt' in f:
            files += [f]
	
	

    for f in files:
        keywords_scores = []
        patient_description = open('patient_files/' + f,'r').read()
        for k in keywords:
            keywords_scores += [fuzz.partial_ratio(k.lower(),patient_description.lower())]

        keywords_matched = []
        for k in keywords_scores:
            if k > 80:
                if keywords[keywords_scores.index(k)] not in keywords_matched:
                    keywords_matched += [keywords[keywords_scores.index(k)]]
        pid = get_id_date(f)[0]
        date = get_id_date(f)[1]
        if len(patient_description) <= 2:
            worksheet.write(row,col,pid)
            col += 1
            worksheet.write(row,col,date)
            col += 1
            worksheet.write(row,col,patient_description)
            col += 1
            worksheet.write(row,col,'UNKNOWN')
            col = 0
            row += 1
            continue
        if len(keywords_matched) > 0:
            worksheet.write(row,col,pid)
            col += 1
            worksheet.write(row,col,date)
            col += 1
            worksheet.write(row,col,patient_description)
            col += 1
            worksheet.write(row,col,'YES')
            col = 0
            row += 1
            add_to_log(pid,date,keywords_matched)
        else:
            worksheet.write(row,col,pid)
            col += 1
            worksheet.write(row,col,date)
            col += 1
            worksheet.write(row,col,patient_description)
            col += 1
            worksheet.write(row,col,'NO')
            col = 0
            row += 1
        
        
    workbook.close()

if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:




