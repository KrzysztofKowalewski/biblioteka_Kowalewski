import csv
 
def reading():
    with open('biblio/book.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return csv_reader     