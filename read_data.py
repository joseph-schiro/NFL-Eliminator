from colorama import Fore, Back, Style

def read_data(raw_data, league):
    class User:
        def __init__ (self, owner, AFC, AFC_wins, NFC, NFC_wins, League):
            self.owner = owner
            self.AFC = AFC
            self.AFC_wins = AFC_wins
            self.NFC = NFC
            self.NFC_wins = NFC_wins
            self.League = League
        def get_data(self):
            return self.owner, self.AFC, self.AFC_wins, self.NFC, self.NFC_wins
        
        def get_name(self):
            return self.owner

        def get_league(self):
            return self.League
        
        def print_data(self):
            print(Fore.LIGHTYELLOW_EX + '\nOwner ' + Fore.LIGHTBLACK_EX + '= ' + Fore.WHITE + self.owner)
            print(Fore.LIGHTRED_EX + 'AFC ' + Fore.LIGHTBLACK_EX + '= ' + Fore.WHITE + self.AFC)
            print(Fore.LIGHTRED_EX + 'AFC Wins ' + Fore.LIGHTBLACK_EX + '= ' + Fore.WHITE + str(self.AFC_wins))
            print(Fore.LIGHTBLUE_EX + 'NFC ' + Fore.LIGHTBLACK_EX + '= ' + Fore.WHITE + self.NFC)
            print(Fore.LIGHTBLUE_EX + 'NFC Wins ' + Fore.LIGHTBLACK_EX + '= ' + Fore.WHITE + str(self.NFC_wins))
            print(Style.RESET_ALL)
        
        def get_afc(self):
            return self.AFC

        def get_nfc(self):
            return self.NFC

        def set_afc_wins(self, wins):
            self.AFC_wins = wins
        
        def set_nfc_wins(self, wins):
            self.NFC_wins = wins

    user_data = []

    for row in raw_data:
        row = ','.join(row).split(',')
        print(Fore.LIGHTCYAN_EX + '\nCreating User Data for {}'.format(row[0]) + '...')
        print(Style.RESET_ALL)
        user_data.append(User(row[0], row[1], row[2], row[3], row[4], league))
    
    return user_data