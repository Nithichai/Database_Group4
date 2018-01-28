import os

f = []
# mypath = 'C:\'
for (dirpath, dirnames, filenames) in os.walk('.'):
    f.extend(filenames)
    break

csv_file_list = [file for file in f if file.endswith('.csv')]
    
print(f)
print(csv_file_list)
