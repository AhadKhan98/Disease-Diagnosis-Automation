# Gingivitis Automatic Diagnosis Program
This directory contains all of the required scripts and instructions to automate the diagnosis of gingivitis using electronic dental records data.

## Instructions
1) Run the 'CSV-TSV To TXT Files' Script on the master sheet containing charting data for patients. This will create an individual text file for every patient in the file. Each text file will contain the charting data for that specific patient.
2) Run the 'Disease Diagnosis Script' on the created text files. Make sure that the script is in the same folder as the text files. This script will create four new folders (Generalized_Gingivitis,Localized Gingivitis,No_Gingivitis,Unknown) and move all of the text files into their respective folders.
3) Some of the unknown cases might have their 'ATTACH' data reported in the periodontitis text files. Therefore, to reduce the number of unknown cases, run the 'Unknowns Reducer Script' and place ALL text files from the periodontitis program into the Knowns/ directory and place the unknown cases where the script it located. After running the script, some of the unknown cases with missing 'ATTACH' information will be updated.
4) Run the 'Disease Diagnosis Script' on these unknown cases to get the final output.
