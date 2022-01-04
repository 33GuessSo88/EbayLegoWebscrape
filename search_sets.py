"""Set List Generator

This script reads a csv file that contains set numbers
and creates a list called search_terms that is used in main
to iterate over.
"""

import csv

search_terms = []
search_file = 'set_test.csv'

with open(search_file, newline='') as csvfile:
    for row in csv.reader(csvfile):
        search_terms.append(row[0])

print(search_terms)

# TODO: this should probably be a function that returns search_terms[]
