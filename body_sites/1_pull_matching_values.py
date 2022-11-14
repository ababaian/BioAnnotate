import csv
from lxml import etree
import glob

with open("bodysite_tags.csv", "r") as search_file:
    sf = list(csv.reader(search_file))

    l = sf[2]
    lookup_list = list(filter(None, l))  # lookup list now includes copies of tags with spaces

print("Cross-ref lists ready.")


def pull_matching_values():
    for event, elem in big_file:
        if event == "end" and elem.tag == "Attribute":
            biosample_tag = elem.attrib["attribute_name"]
            for i in lookup_list:
                if str(i) in biosample_tag:
                    biosample_value = str(elem.text)
                    raw.add(biosample_value)

raw = set()

for f in glob.glob("/Users/user/Downloads/ncbi_split/biosample_set*"):
    big_file = etree.iterparse(f, events=("start", "end"))
    pull_matching_values()

    raw_list = list(raw)
    values = [[i] for i in raw_list]

    with open("values_search_results.csv", "a") as o:  # append mode
        output = csv.writer(o)
        output.writerows(values)  # writerows for one column
    print(f)

print("Output written to csv file.")
