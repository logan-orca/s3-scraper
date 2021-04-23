import re

import csv

with open('../logs/knee-log.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row)

def camel_case_split(str):
      
    start_idx = [i for i, e in enumerate(str)
                 if e.isupper()] + [len(str)]
  
    start_idx = [0] + start_idx
    return [str[x: y] for x, y in zip(start_idx, start_idx[1:])] 
      
      
# # Driver code
# str = "GeeksForGeeks"
# print(camel_case_split(str))


# Import array from logs:
