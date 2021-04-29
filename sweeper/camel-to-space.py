import csv
import re

filename = "../logs/spine-log.csv"

with open(filename) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    value = list(row.values())
    value_list = "".join(map(str, value))
    output = re.sub("([A-Z])", " \\1", f'{value_list}').strip()
    cap_output = output.title()
    print(cap_output)
