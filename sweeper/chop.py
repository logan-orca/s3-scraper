import csv

filename = "../logs/knee-log.csv"

with open(filename) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    value = list(row.values())
    value_list = "".join(map(str, value))
    value_string = str(value_list).strip("[']")

    original = value_string
    size = len(original)

    strip = original[:size - 14]
    string_split = strip.split('_')
    list_to_string = str(string_split).strip("[']")
    string_cap = [string_split.capitalize() for string_split in string_split]
    final_value = " ".join(string_cap)

    print(final_value)



