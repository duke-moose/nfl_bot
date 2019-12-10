##################All QB Passing Yards in Fantasy Season #########################################
import nflgame


games = nflgame.games(year=[2016], week=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) #2012, 2013, 2014, 2015, 2016
players = nflgame.combine(games, plays=True)

# #### Quarterback Filter #######
# print 'Quarterbacks'
# for p in players.sort('passing_tds').limit(20):
#     points = (p.passing_tds + p.rushing_tds + p.receiving_tds + p.kickret_tds + p.puntret_tds + p.fumbles_rec_tds) * 6 \
#              + p.passing_yds / 25 \
#              + (p.receiving_yds + p.rushing_yds) / 10 \
#              + (p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) * 2 \
#              + (p.passing_int + p.fumbles_lost) * (-2)
#     print '%s, %d touchdowns and %d passing yards for %d points.' \
#     % (p, p.passing_tds, p.passing_yds, points)
#
# print '-'*25

#### Runningback Filter #######
print 'Runningbacks'
for p in players.sort('rushing_yds').limit(50):
    points = (p.passing_tds + p.rushing_tds + p.receiving_tds + p.kickret_tds + p.puntret_tds + p.fumbles_rec_tds) * 6 \
             + p.passing_yds / 25 \
             + (p.receiving_yds + p.rushing_yds) / 10 \
             + (p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) * 2 \
             + (p.passing_int + p.fumbles_lost) * (-2)
    print '%s, %d rushing touchdowns %d recieving_tds and %d rushing yards for %d points at position %s, %s.' \
          % (p, p.rushing_tds, p.receiving_tds, p.rushing_yds, points, p.guess_position, p.player.position)

    
print '-'*25


# print 'Wide Receivers'
# #### Wide Receiver Filter #######
# for p in players.sort('receiving_yds').limit(20):
#     points = (p.passing_tds + p.rushing_tds + p.receiving_tds + p.kickret_tds + p.puntret_tds + p.fumbles_rec_tds) * 6 \
#              + p.passing_yds / 25 \
#              + (p.receiving_yds + p.rushing_yds) / 10 \
#              + (p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) * 2 \
#              + (p.passing_int + p.fumbles_lost) * (-2)
#     print '%s, %d touchdowns and %d passing yards for %d points.' \
#           % (p, p.passing_tds, p.passing_yds, points)
#
# print '-'*25
#
#
# print 'Tight Ends'
# for pos in ['TE']:
#     for p in filter(lambda z: z.guess_position==pos, players.sort('receiving_yds').limit(20)):
#         points = (
#                  p.passing_tds + p.rushing_tds + p.receiving_tds + p.kickret_tds + p.puntret_tds + p.fumbles_rec_tds) * 6 \
#                  + p.passing_yds / 25 \
#                  + (p.receiving_yds + p.rushing_yds) / 10 \
#                  + (p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) * 2 \
#                  + (p.passing_int + p.fumbles_lost) * (-2)
#         print '%s, %d touchdowns and %d passing yards for %d points.' \
#               % (p, p.passing_tds, p.passing_yds, points)
