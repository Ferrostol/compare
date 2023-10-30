from pathlib import Path
import difflib
  
mypath = './'
file17c = Path(mypath, 'data1.txt')
file18c = Path(mypath, 'data2.txt')

with open(file17c) as file_1:
    file1 = file_1.readlines()
  
with open(file18c) as file_2:
    file2 = file_2.readlines()
  
for line in difflib.unified_diff(
         file1, file2, fromfile=str(file17c), tofile=str(file18c), lineterm=''):
    print(line)
