#!/usr/bin/env python
# coding: utf-8

# In[7]:


file_name = input("Enter file name: ")
data = open(file_name,'r').readlines()
data = list(map(str.strip,data))
del(data[0])


# In[36]:


line = 0
complete_pid = []
complete_date = []
complete_diagnosis = []
duplicate_ids = []
for i in range(len(data)):
    patient_id = data[line].split(',')[0]
    date = data[line].split(',')[1]
    diagnosis = data[line].split(',')[2]
    try:
        if patient_id == data[line+1].split(',')[0]:
            if patient_id not in duplicate_ids:
                duplicate_ids += patient_id
            line += 1
            continue
        else:
            if diagnosis == 'Unknown':
                temp_diagnosis = diagnosis
                temp_pid = patient_id
                temp_date = date
                temp_line = line
                while temp_diagnosis == 'Unknown' and temp_pid == patient_id:
                    temp_line -= 1
                    temp_pid = data[temp_line].split(',')[0]
                    if temp_pid != patient_id:
                        break
                    temp_diagnosis = data[temp_line].split(',')[2]
                    temp_date = data[temp_line].split(',')[1]
                complete_pid += [temp_pid]
                complete_date += [temp_date]
                complete_diagnosis += [temp_diagnosis]
                line += 1
                continue
            else:
                complete_pid += [patient_id]
                complete_date += [date]
                complete_diagnosis += [diagnosis]
                line += 1
                continue
    except IndexError:
        complete_pid += [patient_id]
        complete_date += [date]
        complete_diagnosis += [diagnosis]
        break

output_file = open(file_name + '_complete_data.csv','w')
output_file.write("Patient ID,Date,Diagnosis\n")
for i in range(len(complete_pid)):
    output_file.write("%s,%s,%s\n" % (complete_pid[i],complete_date[i],complete_diagnosis[i]))
output_file.close()

