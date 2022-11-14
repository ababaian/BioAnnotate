import csv
import pandas as pd

with open("bodysite_tags.csv", "r") as search_file:
    sf = list(csv.reader(search_file))

    t = sf[0]
    terms_list = list(filter(None, t))  # filter out blanks

print("Cross-ref list ready.")

f = pd.read_csv("/Users/user/Documents/COURSES 2022-23/Rotations/2-Babaian lab/values_after_dictionary.csv", header=None)
values_after_dictionary = f[0].tolist()

print(values_after_dictionary[0:5])

level_1_term = list()
value_output = list()

for e in terms_list:
    term = str(e)
    for i in values_after_dictionary:
        value = str(i)
        if term in value:
            level_1_term.append(term)
            value_output.append(value)

df = pd.DataFrame(list(zip(level_1_term, value_output)),
                  columns=["LEVEL 1 TERM", "VALUE"])

df.to_csv("crossref_results.csv", index=False)

print("Table written to csv file.")
