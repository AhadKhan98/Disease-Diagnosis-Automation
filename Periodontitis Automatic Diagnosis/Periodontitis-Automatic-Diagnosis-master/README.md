# Periodontitis Automatic Diagnosis Program
This directory contains all of the required scripts and instructions to automate the diagnosis of periodontitis using electronic dental records data.

## Instructions
1) Run the 'CSV-TSV To TXT Files' Script on the master sheet containing charting data for patients. This will create an individual text file for every patient in the file. Each text file will contain the charting data for that specific patient.
2) From the 'Disease Diagnosis Scripts' run the 'Diagnose Unknown Cases' script. This script will seperate the Unknown Cases from the text files. (Patients with incomplete or missing information)
2) From the 'Disease Diagnosis Scripts' run the 'Diagnose Severe Cases' script. This script will create two new folders (Severe_Cases, Others). The text files will be moved to the Severe_Cases folder if they are diagnosed with Severe Periodontitis whereas the remaining cases will be moved to the Others folder. 
3) From the 'Disease Diagnosis Scripts' run the 'Diagnose Moderate Cases' script in the 'Others' folder. This script will create two new folders (Moderate_Cases, Others). The text files will be moved to the Moderate_Cases folder if they are diagnosed with Moderate Periodontitis whereas the remaining cases will be moved to the Others folder. 
4) Similarly, run the 'Diagnose Mild Cases' script in the 'Others' folder. The output will be two folders 'Mild_Cases' and Others containing patients having mild periodontitis and no gingivitis respectively.
