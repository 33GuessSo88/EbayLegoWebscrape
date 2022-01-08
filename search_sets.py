"""Set List Generator

This script reads a csv file that contains set numbers
and creates a list called search_terms that is used in main
to iterate over. Also removes duplicates.
"""


def create_search_list():
    import csv

    search_terms = []
    search_file = 'All_sets_2021.csv'

    with open(search_file, newline='') as csvfile:
        for row in csv.reader(csvfile):
            search_terms.append(row[0])

    # Remove duplicates
    search_terms = list(dict.fromkeys(search_terms))
    return search_terms


# print(search_terms)

# TODO: this should probably be a function that returns search_terms[]
# TODO: Go to brickset.com every 3 months and grab a new set of set numbers.
