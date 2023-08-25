import csv

id = "412090644"

with open('idToUrl.csv', mode ='r', encoding="utf8")as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for row in csvFile:
        rRow = row[0].split(' ')
        idrow = rRow[0]
        if idrow == id:
            print([rRow[1],rRow[2]])