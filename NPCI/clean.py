import csv

filename = 'NPCI/dataNPCI.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    ids=[]
    for row in datareader:
        id = row[0]
        if id in ids:
            print(id)
        else:
            ids.append(id)
    print(ids)