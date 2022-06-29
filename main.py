from scan_csv import scan_csv
from read_data import read_data
from watch_scores import get_wins
from write_csv import write_csv
from colorama import Fore, Back, Style
from time import sleep
from os import listdir

### TODO: 
# - Fix scheduler

### NOTES:
# - Implement into website

print('\n')
print(Fore.LIGHTBLACK_EX + '===== ' + Fore.LIGHTCYAN_EX + 'NFL ELIMINATOR Version 1.0.0' + Fore.LIGHTBLACK_EX + ' =====')
print('= ' + Fore.WHITE + 'Made by Conley Ratzlaff & Joseph Schiro' + Fore.LIGHTBLACK_EX + ' =')
print(Style.RESET_ALL + '\n')
sleep(5)

leagues = listdir('Leagues')

for league in leagues:
    leagues[leagues.index(league)] = str(league).replace('.csv', '')

for league in leagues:
    raw_data = scan_csv(str(league + '.csv'))

    print(Fore.LIGHTCYAN_EX + '\nScanning Data for League ' + Fore.LIGHTBLACK_EX + '= ' + Fore.WHITE + '{}'.format(league))
    print(Style.RESET_ALL)

    league_list = read_data(raw_data, league)
    league_name = ''
    for user in league_list:
        name = user.get_name()
        afc = user.get_afc()
        nfc = user.get_nfc()
        league_name = user.get_league()

        afc_wins = get_wins(afc, 'afc')
        nfc_wins = get_wins(nfc, 'nfc')

        user.set_afc_wins(afc_wins)
        user.set_nfc_wins(nfc_wins)

        # print('\nName = {}'.format(user.get_name()))
        # print('AFC = {}'.format(user.get_afc()))
        # print('NFC = {}'.format(user.get_nfc()))

    for user in league_list:
        user.print_data()

    print('\nWriting to CSV...')

    write_csv(league_name, league_list)