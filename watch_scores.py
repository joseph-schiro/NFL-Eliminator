from colorama import Fore, Back, Style
from sportsipy.nfl.teams import Teams
from time import sleep

def get_wins(team, conference):
    if conference == 'afc':
        color = Fore.LIGHTRED_EX
    else:
        color = Fore.LIGHTBLUE_EX
    print('\n\nGetting Wins for ' + color + '{}'.format(team) + '...')
    print(Style.RESET_ALL)
    abbr = {
        'Dallas Cowboys': 'DAL',
        'Tampa Bay Buccaneers': 'TAM',
        'Buffalo Bills': 'BUF',
        'Kansas City Chiefs': 'KAN',
        'Los Angeles Chargers': 'SDG',
        'New England Patriots': 'NWE',
        'Cincinnati Bengals': 'CIN',
        'Los Angeles Rams': 'RAM',
        'Indianapolis Colts': 'CLT',
        'Green Bay Packers': 'GNB',
        'Arizona Cardinals': 'CRD',
        'Philadelphia Eagles': 'PHI',
        'San Francisco 49ers': 'SFO',
        'Minnesota Vikings': 'MIN',
        'Tennessee Titans': 'OTI',
        'Seattle Seahawks': 'SEA',
        'Baltimore Ravens': 'RAV',
        'Las Vegas Raiders': 'RAI',
        'New Orleans Saints': 'NOR',
        'Cleveland Browns': 'CLE',
        'Pittsburgh Steelers': 'PIT',
        'Miami Dolphins': 'MIA',
        'Denver Broncos': 'DEN',
        'Washington Commanders': 'WAS',
        'Detroit Lions': 'DET',
        'Atlanta Falcons': 'ATL',
        'Chicago Bears': 'CHI',
        'New York Jets': 'NYJ',
        'Carolina Panthers': 'CAR',
        'Houston Texans': 'HTX',
        'New York Giants': 'NYG',
        'Jacksonville Jaguars': 'JAX',
    }

    teams = Teams()
    error = False
    
    try:
        team = teams(abbr[team])
    except:
        print('[!] No data for {}.'.format(team))
        sleep(3)
        error = True

    if not error:
        wins = team.wins
        print(Fore.LIGHTGREEN_EX + 'Wins = {}'.format(wins))
        print(Style.RESET_ALL)
        return wins
    else:
        return 0
