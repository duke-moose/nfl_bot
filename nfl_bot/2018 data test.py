'''Python 3'''


import nflgame

year = 2018
week = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


'''Check that all 2018 stats are loaded - Confirmed July 2019'''
# 2018 season
# team = "NO"
# player = "D.Brees"
# tds = 32

# team = "KC"
# player = "P.Mahomes"
# tds = 50

# team = "ATL"
# player = "M.Ryan"
# tds = 35
#
#     '''Check for stat for entire season'''
# games = nflgame.games(year=year, week=week)
# players = nflgame.combine(games, plays=True)
# for p in players.sort('passing_tds').limit(10):
#     print '%s, %s, %d touchdowns.' \
#           % (p, p.team, p.passing_tds)
#
#     '''Check game stats for single player by week'''
# games = nflgame.games(year=year, home=team, away=team)
# for i, game in enumerate(games):
#     # if game.players.name(this_player.gsis_name):
#     if game.players.name(player):
#         stats = game.players.name(player).passing_tds
#         print 'Game {:2}, Week {:2} - {:4}'.format(
# 			i+1, game.schedule['week'], stats)

'''Check that team names are correct for the schedule'''
nfl_teams = {}

'''Fix Jacksonville, LA Rams, & LA Chargers'''
def team_fix(team):
    t = team
    if team is 'JAC':
        t = 'JAX'
    elif team is 'STL':
        t = 'LA'
    elif team is 'SD':
        t = 'LAC'
    return t

# for team in nflgame.teams:
#     '''
#     nflgame.teams = ['NO', 'New Orleans', 'Saints', 'New Orleans Saints', 'N.O.', 'NOR']
#     '''
#     team_name = team_fix(team[0])
#     nfl_teams[team_name] = [0] * 5

# '''Check that JAC is JAX in all 2018'''
# team = 'JAX'
# week = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17]
# for week in week:
#     games = nflgame.games(year=year, week=week, home=team, away=team)
#     for game in games:
#         print(week, game.home, game.away)


