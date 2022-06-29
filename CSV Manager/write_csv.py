import csv

def write_csv(league_name, league):
    with open('Leagues/{}'.format(league_name + '.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter =',', quotechar='|')
        for user in league:
            writer.writerow(list(user.get_data()))