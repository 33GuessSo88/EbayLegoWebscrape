import csv

search_terms = []
with open('set_test.csv', newline='') as csvfile:
    for row in csv.reader(csvfile):
        search_terms.append(row[0])

print(search_terms)