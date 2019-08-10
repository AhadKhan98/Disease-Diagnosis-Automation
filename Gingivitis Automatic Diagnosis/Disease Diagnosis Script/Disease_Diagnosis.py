#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os,re


# In[30]:


def calculate_total_sites(file_content):
    
    """
    This function return the total sites which is determined by the total teeth * 6
    """
    total_sites = 0
    sites_used = []
    for i in range(len(file_content)):
        if 'SiteName:' in file_content[i]:
            current_site = file_content[i][10:]
            if not current_site in sites_used:
                sites_used += [current_site]
                total_sites += 1
    return total_sites * 6

def calculate_bop(file_content):
    """
    This function reads the file and checks for the number of sites that were bleeding and then returns it.
    """
    bop_sites = 0
    for i in range(len(file_content)):
        if 'PerCond: BLEED' in file_content[i]:
            values = [file_content[i+3][8:],file_content[i+4][8:],file_content[i+5][8:]]
            for item in values:
                if item == '1' or item == 'B' or item == 'b':
                    bop_sites += 1
            
    return bop_sites

def calculate_attach_sites(file_content):
    """
    This function reads the file and checks for the number of attach sites and returns it
    """
    attach_sites = 0
    for i in range(len(file_content)):
        if 'PerCond: ATTACH' in file_content[i]:
            attach_sites += 1
    return attach_sites
            

def diagnose(total_sites, bop_sites,file):
    """
    This function calculates the percentage of the number of sites that bled and uses the given criteria to move the file into
    its determined diagnosis.
    """
    if total_sites == 0: # Accounts for other cases
        os.rename(file,'Unknown/'+file)
        return "Unknown"

    elif round((bop_sites / total_sites) * 100) < 10:
        os.rename(file,'No_Gingivitis/'+file)
        return "No Gingivitis"
    elif round((bop_sites / total_sites) * 100) >= 10 and round((bop_sites / total_sites) * 100) <= 30:
        os.rename(file,'Localized_Gingivitis/'+file)
        return "Localized Gingivitis"
    elif round((bop_sites / total_sites) * 100) > 30:
        os.rename(file,'Generalized_Gingivitis/'+file)
        return "Generalized Gingivitis"
    


# In[35]:


def main():
    files = []
    try:
        os.mkdir('No_Gingivitis')
        os.mkdir('Localized_Gingivitis')
        os.mkdir('Generalized_Gingivitis')
        os.mkdir('Unknown')
    except FileExistsError:
        pass

    for f in os.listdir():
        if re.search('.txt',f):
            files += [f]

    log_file_content = ""
    for file in files:
        data = open(file,'r').readlines()
        data = list(map(str.strip,data))
        patient_id = file.split('_')[0]
        patient_date = file.split('_')[1].replace('.txt','')
        total_sites = calculate_total_sites(data)
        total_teeth = round(total_sites / 6)
        bop_sites = calculate_bop(data)
        attach_sites = calculate_attach_sites(data)
        if attach_sites == 0:
            log_file_content += ("Patient ID: " + str(patient_id) + "\n" + "Date: " + str(patient_date) + "\n" + "Total Teeth: ATTACH MISSING" + "\n" + "Total Sites: ATTACH MISSING" + "\n" + "BOP Sites: ATTACH MISSING" + "\n" + "Affected: ATTACH MISSING"+ "\n" + "Diagnosis: UNKNOWN" + "\n\n\n")
            os.rename(file,'Unknown/'+file)
            continue
        diagnosis = diagnose(total_sites,bop_sites,file)

        log_file_content += ("Patient ID: " + str(patient_id) + "\n" + "Date: " + str(patient_date) + "\n" + "Total Teeth: " + str(total_teeth) +"\n" + "Total Sites: " + str(total_sites) + "\n" + "BOP Sites: " + str(bop_sites) + "\n" + "Affected: " + str(round((bop_sites / total_sites) * 100)) +"%"+ "\n" + "Diagnosis: " + diagnosis + "\n\n\n") 
    log_file = open("log.txt",'w')
    log_file.write(log_file_content)
    log_file.close()

if __name__=="__main__":
    main()


# In[ ]:




