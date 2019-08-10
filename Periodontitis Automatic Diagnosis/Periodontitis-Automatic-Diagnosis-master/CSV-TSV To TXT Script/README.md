# CSV/TSV To TXT File Script
### Author: Ahad Zai
## Functionality
This script is created for the periodontitis project. The script reads through a .csv or a .tsv file and using the first two columns (Patient ID and Date) it creates a text file for every unique patient. The content that goes in the file is the rest of the values stored in the file for that particular patient.
## Instructions
1) Add .csv or .tsv file to the working directory
2) **IMPORTANT:** Make sure to remove special characters from the file otherwise program might malfunction.
2) Download the python script and run it
2) Enter the name of the csv file including the file extention (eg: example.csv)
3) Enter 0 if the file does not contain an identifying header or 1 if it does contain a header.
4) Once 'Completed!' is displayed, check your existing directory to locate the newly created text files. 