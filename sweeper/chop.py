import csv

filename = "../logs/knee-log.csv"

with open(filename) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    value = list(row.values())
    value_string = "".join(map(str, value))
    value_strip = str(value_string).strip("[']")
    original = value_strip
    size = len(original)

    strip = original[:size - 14]
    string_split = strip.split('_')

    list_to_string = str(string_split).strip("[']")
    string_cap = [string_split.capitalize() for string_split in string_split]
    y = " ".join(string_cap)

    print(y)



