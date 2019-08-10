#!/usr/bin/env python
# coding: utf-8

# In[129]:



data = open("PerioCharting ATTACH_POCKET.csv",'r').readlines()
data = list(map(str.strip,data))
del(data[0])
data
patient_ids = []
sites_affected = []
perconds_affected = []
count = 0
line = 0
for i in range(len(data)):
    try:
        cur_sitename = data[line].split(',')[5]
        next_sitename = data[line+1].split(',')[5]
    except IndexError:
        break
        
    if cur_sitename == next_sitename:
        line += 2
        continue
    else:
        patient_id = data[line].split(',')[1].replace('"','') 
        site_affected = data[line].split(',')[5].replace('"','')
        percond_affected = data[line].split(',')[4].replace('"','')
        if patient_id not in patient_ids:
            count += 1
        patient_ids += [patient_id]
        sites_affected += [site_affected]
        perconds_affected += [percond_affected]
        line+=1


for pid in patient_ids:
    copy_to_xl_file = open("copy_to_xl.txt",'w')
    copy_to_xl_file.write(pid+'\n')
    copy_to_xl_file.close()

log_file = open("log.txt",'w')
log_file.write('Unique Unstructured Patients: %s\n\nUnstructured Patients by PatientIDs: \n' % count)

for pid in range(len(patient_ids)):
    log_file.write('PatientID: ' + patient_ids[pid] + '  |   PerCond: '+perconds_affected[pid]+'  |  SiteName: '+ sites_affected[pid] + '\n')
log_file.close()


# In[ ]:




