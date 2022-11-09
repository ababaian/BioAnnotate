import pandas as pd
import csv

f = pd.read_csv("/Users/user/Documents/COURSES 2022-23/Rotations/2-Babaian lab/values_search_results.csv", header=None)
values = f[0].tolist()
print("Input read.")


def replace_all(v):
    v = v.lower()
    dictionary = {' ': '_',
                  '-': '_',
                  '—': '_',
                  "'": '',
                  '/': '',
                  ',': '',
                  '"': ''}
    for key, value in dictionary.items():
        v = v.replace(key, value)
    return v

d = set()

for i in values:
    v = str(i)
    if not v.isnumeric():
        v_fixed = replace_all(v)
        d.add(v_fixed)

print("Making list.")
d_list = sorted(list(d))
values_after_dictionary = [[i] for i in d_list]

with open("/Users/user/Documents/COURSES 2022-23/Rotations/2-Babaian lab/values_after_dictionary.csv", "w") as o:  # append or write mode
    output = csv.writer(o)
    output.writerows(values_after_dictionary)  # writerows for one column, no s for one row

print("Output written to csv file.")
