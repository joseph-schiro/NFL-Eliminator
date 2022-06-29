import csv
    
def scan_csv(league):

    raw_data = []
    
    with open('Leagues/{}'.format(league)) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            raw_data.append(row)
    csvfile.close()

    return raw_data