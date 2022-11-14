import pandas as pd
import csv

f = pd.read_csv("bto_labels.csv", header=None)
bto = f[0].tolist()


def replace_all_bto(label):
    label = label.lower()
    dictionary = {' ': '_',
                  '-': '_',
                  '—': '_',
                  '&apos;': ''}
    for key, value in dictionary.items():
        label = label.replace(key, value)
    return label

bto_labels = list()

for i in bto:
    if not "culture" in str(i):
        label = str(i)
        label_fixed = replace_all_bto(label)
        bto_labels.append(label_fixed)

bto_labels_final = [[i] for i in bto_labels]

with open("bto_labels_final.csv", "w") as o:  # append or write mode
    output = csv.writer(o)
    output.writerows(bto_labels_final)  # writerows for one column, no s for one row

print("Output written to csv file.")
