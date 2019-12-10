import nflgame
import csv

# nflgame.combine(nflgame.games(2019)).csv('season2019.csv')

# games = nflgame.games(year=2019, week=6, kind='REG')
# plays = nflgame.combine_plays(games).csv('plays2019.csv')
#
# for play in plays:
#     # print play
#     for player in play.players:
#         print '\t', player, player.formatted_stats()


games = nflgame.games(2019)
plays = nflgame.combine_plays(games)

with open('plays2019.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerow(['playid', 'down', 'time', 'home', 'team', 'players', 'touchdown', 'yards_togo', 'total_yds', 'turnovers', 'rushing_yds', 'passing_yds', 'kicking_xpa', 'kicking_xpmade', 'kicking_fga', 'kicking_fgm'])

    def turnovers(p):
        return p.passing_int or p.fumbles_lost
    def total_yards(p):
        return p.rushing_yds + p.passing_yds

    for play in plays:
        # print(dir(play))
        data = []
        data.append(play.playid)
        data.append(play.down)
        data.append(play.time)
        data.append(play.home)
        data.append(play.team)
        data.append(play.players)
        data.append(play.touchdown)
        data.append(play.yards_togo)
        data.append(total_yards(play))
        data.append(turnovers(play))
        data.append(play.rushing_yds)
        data.append(play.passing_yds)
        data.append(play.kicking_xpa)
        data.append(play.kicking_xpmade)
        data.append(play.kicking_fga)
        data.append(play.kicking_fgm)
        w.writerow(data)
