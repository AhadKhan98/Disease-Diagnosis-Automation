#!/usr/bin/env python
# coding: utf-8

# In[11]:


from fuzzywuzzy import fuzz
import os 
import xlsxwriter as xl



diabetes_keywords_pos = ['recently diagnosed with','recently diagnosed','reports history of diabetes','diagnosed','Yes','took insulin','diagnoses','Diabetic','diabetic episode','diabetic','diagnnosed',
                        'insulin dependent','Dx w Diabetes','medicated for diabetes','diabetes','hx of DM','diagnosis of','diagnosis',
                        'Insulin Dependent Diabetes','Insulin dependent','diabetes mellitus','diagnosed with diabetes','medication for diabetes',
                        'type I diabetes','Type 1 diabetes','diabetes type I','DM T1','Type I Diabetes','Type 1 Diabetes','history of type I',
                        'type I','Diabetes Type 2','Type II diabetic','type II diabetes','Type Two','diabetes type 2','type II diabetics',
                        'DM2','diabetes mellitus type 2','type 2 diabetes','type II DM','DM Type II',
                        'Type II Diabetes Mellitus','type II','Diabetes Type II','type 2 diabetic','Type 2','T2DM','type two diabetes',
                        'Type 2 diabetes mellitus','Type II Diabetic','type 2 diabtetes','type II diabetes mellitus','DMII',
                        'Type2 diabetes','type 2','Stage two diabetes','Type two diabetes','Diabetes type II']
diabetes_keywords_neg = ['No.','no diagnosis of',"doesn t have diabetes",'not actual diabetes','not diagnosed with','not diagnosed with any type of diabetes',
                        'not diagnosed','does not have diabetes','no longer diabetic','never actually diagnosed','mother had','family hx','father had', 'grandmother', 'grandfather']
diabetes_keywords_neg += ['Prediabetic','borderline type 2 diabetes','borderline','borderline diabetic type II','borderline type 2 diabetic',
                        'Borderline diabetic','temporary diabetes','pre diabetic','mild diabetes mellitus','mild diabetes',
                        'beginnings of diabetes','Pre-diabetes','boarderline diabetic','is pre-diabetic','pre-diabetic']


# In[35]:


def similar(a,b):
    if type(a) == str:
        a = a.lower()
    if type(b) == str:
        b = b.lower()
    return fuzz.partial_ratio(a,b)

def get_top_five(scores):
    top_scores = []
    for item in range(5):
        top_scores += [max(scores)]
        scores.remove(max(scores))
    return top_scores

def find_diabetes(description,file):
    if len(description) == 0:
        return 'Unknown'
    
    positive_scores = []
    negative_scores = []
    
    for keyword in diabetes_keywords_pos:
        positive_scores += [similar(keyword,description)]
    for keyword in diabetes_keywords_neg:
        negative_scores += [similar(keyword,description)]
    
    final_positive_score = sum(get_top_five(positive_scores))
    final_negative_score = sum(get_top_five(negative_scores))
    
    if final_positive_score > final_negative_score:
        return 'Diabetic'
    elif final_positive_score < final_negative_score:
        return 'Not Diabetic'
    else:
        return 'Unknown'
    


# In[36]:


files = []
for f in os.listdir():
    if '.txt' in f:
        files += [f]

        
excel_file = xl.Workbook('diabetes_diagnosis_output.xlsx')
worksheet = excel_file.add_worksheet()
row = 0
col = 0
worksheet.write(0,0,'Patient ID')
worksheet.write(0,1,'Date')
worksheet.write(0,2,'Program Diagnosis')
worksheet.write(0,3,'Clinical Documentation')
row += 1
for file in files:
    patient_id = file.split('_')[0]
    date = file.split('_')[1].replace('.txt','')
    description = open(file,'r').read()
    diagnosis = find_diabetes(description,file)
    worksheet.write(row,col,patient_id)
    worksheet.write(row,col+1,date)
    worksheet.write(row,col+2,diagnosis)
    worksheet.write(row,col+3,description)
    row += 1
    
excel_file.close()
    
    

