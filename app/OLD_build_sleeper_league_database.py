# File to access Sleeper API to build player dictionary and check players on other teams.
import json
import requests
import os
import sys
from datetime import datetime
import glob


def save_json_from_api(api_url, f_path_and_name):
    json_data = requests.get(api_url).content
    json_data = json.loads(json_data)
    outfile = os.path.join(f_path_and_name)
    with open(outfile, 'w') as f:
        json.dump(json_data, f, indent=4)


class SleeperBuild:
    """
    Builds Merkin Men User Roster, All Players, and Players on each User Roster
    """
    def __init__(self, year, league_name, league_num):
        self.year = year
        self.directory = league_name + '_' + str(year)
        self.leagueId = league_num
        self.url = 'https://api.sleeper.app/v1/league/' + str(self.leagueId)
        self.users = os.path.join(self.directory, league_name + '_users_' + str(year) + '.json')
        self.usersPlayerRoster = os.path.join(self.directory, league_name + '_user_player_roster_' +
                                              str(year) + '.json')
        self.nflPlayerUrl = 'https://api.sleeper.app/v1/players/nfl'
        self.mmUserUrl = self.url + '/users'
        self.today = datetime.today()
        self.nflPlayers = os.path.join(self.directory, 'NFL_players_' + self.today.strftime('%m%d%y') + '.json')
        self.mmRosterUrl = self.url + '/rosters'
        self.run()

    def make_dir(self):
        if not os.path.isdir(self.directory):
            print('Making directory %s' % self.directory)
            os.mkdir(self.directory)
        else:
            print('Directory: %s exists' % self.directory)

    def make_user_roster(self):
        if not os.path.isfile(self.users):
            print('Making roster')
            try:
                save_json_from_api(self.mmUserUrl, self.users)
            except:
                print(sys.exc_info())
        else:
            print('Roster: %s exists' % self.users)

    def make_nfl_players(self):
        f = [f for f in glob.glob(os.path.join('*' + self.directory, 'NFL_players*.json'))]
        if f:
            date = f[0].split('.')[0][-6:]
            date = datetime.strptime(date, '%m%d%y')
        else:
            date = datetime(1900, 1, 1)

        if (self.today - date).days > 7:

            save_json_from_api(self.nflPlayerUrl, self.nflPlayers)
            for f_remove in f[:-1]:
                os.remove(f_remove)
            print('NFL_players is up to date - updated')
        else:
            print('NFL_players is up to date - not updated')

    def make_user_player_roster(self):
        save_json_from_api(self.mmRosterUrl, self.usersPlayerRoster)

    def run(self):
        print('Checking directory')
        self.make_dir()

        print('Checking user roster')
        self.make_user_roster()

        print('Checking for roster of NFL players')
        self.make_nfl_players()

        print('Updating users player rosters')
        self.make_user_player_roster()


class SleeperPlayersTaken:
    """
    Builds dictionary of players taken from rosters except specified user
    """
    def __init__(self, me, sleeper_build):
        self.moose = me
        self.sleeper_build = sleeper_build
        self.sleeper_dict = self.user_id_and_name()
        self.user_players()
        self.taken_list = self.players_taken()

    def user_id_and_name(self):
        sleeper_dict = {}
        with open(self.sleeper_build.users, 'r') as infile:
            mm_users = json.load(infile)
            users = [(i['display_name'], i['user_id']) for i in mm_users]
            for u in users:
                sleeper_dict[u[1]] = {
                    'display_name': u[0],
                    'user_id': u[1]
                }
        return sleeper_dict

    def user_players(self):
        # self.sleeper_dict
        with open(self.sleeper_build.usersPlayerRoster, 'r') as infile:
            mm_player_roster = json.load(infile)
            players = [(i['owner_id'], i['players']) for i in mm_player_roster]
            for p in players:
                self.sleeper_dict[p[0]].update({
                    'players': p[1]
                })

    def players_taken(self):
        taken = []
        for key, value in self.sleeper_dict.iteritems():
            if value['display_name'] != self.moose:
                taken += value['players']
        return taken


if __name__ == '__main__':
    mm = SleeperBuild(year=2019,
                      league_name='merkin_men',
                      league_num=393807404686458880)
    mm_dict = SleeperPlayersTaken(me='DeepMooseKnuckle',
                                  sleeper_build=mm)
    print(mm_dict.sleeper_dict)
    print(mm_dict.taken_list)




#
# # 2. Convert Player Numbers to names
# sleeper_players = os.path.join(directory, sleeper_players_roster_file)
# with open(sleeper_players, 'r') as read_file:
#     sleeper_file = json.load(read_file)
#     # print(sleeper_file)
#     for key, value in sleeper_file.iteritems():
#         if key in players_taken:
#             try:
#                 players_taken.append(value['full_name'])
#                 players_taken.remove(key)
#             except KeyError:
#                 if value['position'] == 'DEF':
#                     pass
#                 else:
#                     print('No full_name key or Defense in ', value)
# print(players_taken)
#
# for player in players_taken:
#     player = player.split(' ')
#     if len(player) > 1: #Filter out defense
#         print(str(player[0])[0] + '.' + player[1])
