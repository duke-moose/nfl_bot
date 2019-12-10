import nflgame

# Utility function to print out some basic info about a drive
# def print_drive_info(drive):
# 	print "Drive {0} - Team {1} - First Downs {2} - Result {3} - Total Yds {4} - Penalty Yds {5} - Play Count {6} - Possession Time {7} ({8} seconds) - From {9} Until {10}".format(drive.drive_num, drive.team, drive.first_downs, drive.result, drive.total_yds, drive.penalty_yds, drive.play_cnt, drive.pos_time, drive.pos_time.total_seconds(), drive.field_start, drive.field_end)
#
# g = nflgame.one(2013, 1, "BUF", "NE")
#
# print "\nFilter & Print Drives with 3 or more First Downs"
# for drive in g.drives.filter(first_downs__ge=3):
# 	print_drive_info(drive)
#
# print "\nFilter & Print Drives with 5 or more Plays"
# for drive in g.drives.filter(play_cnt__ge=5):
# 	print_drive_info(drive)
#
# print "\nFilter & Print Drives Resulting in a Punt"
# for drive in g.drives.filter(result="Punt"):
# 	print_drive_info(drive)
#
# print "\nFilter & Print Drives with 20 or less Yards"
# for drive in g.drives.filter(total_yds__le=20):
# 	print_drive_info(drive)
#
# print "\nFilter & Print Drives where the Defense has more Penalty Yards than the Offense"
# for drive in g.drives.filter(penalty_yds__gt=0):
# 	print_drive_info(drive)
#
# print "\nFilter & Print Drives where the Offense has more Penalty Yards than the Defense"
# for drive in g.drives.filter(penalty_yds__lt=0):
# 	print_drive_info(drive)

# Finds aggregate team stats for single games, will be good to build the total defense yds allowed module.
# #Find our game
g = nflgame.one(2013, 1, "BUF", "NE")

print g.stats_home
print g.stats_away

# Finds and list specific player states aggregated by entire an entire game.
# games = nflgame.games(year=2017, week=9, kind='REG')
# for game in games:
#     for pp in game.players:
#         print pp, pp.team, pp.stats

# Finds and list specific plays made by players aggregated by week.
# games = nflgame.games(2017, week=9)
# plays = nflgame.combine_plays(games)
# for p in plays:
#     print p.players
#     print p.team, p.time, p.total_yards
#     print p.data

    # if p.note == None:
    #     down = p.down
    #     ydstogo = p.ydstogo
    # print p.note, p.down, p.ydstogo
    # print p.data

# games = nflgame.games(2017, week=10)
# players = nflgame.combine_max_stats(games)
# for p in players:
#     print p.playerid
#     print p.stats

# games = nflgame.games(2017, week=9)
# plays = nflgame.combine_plays(games)
# for g in games:
#     print g.home, g.away
#     for drive in g.drives:
#         for play in drive.plays:
#             print play.player
#             print drive
#             # print drive.team, drive.time, drive.total_yards
#             # print drive.data