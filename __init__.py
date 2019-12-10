import nflgame
import fixes
import pythagorean_wins as pw
import schedule
import strength_of_schedule
import player_ranks

# year = 2018
# weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
year = 2019
weeks = [1,2,3]

season_type = 'REG'

'''Build Dictionary of Teams'''
draft_team  = fixes.build_dict(nflgame.teams)

'''Add Pythagorean Wins to Dictionary'''
pw.pythagorean_calculated_wins(draft_team, year, weeks, season_type)

'''Build 2019 Schedule'''
schedule.schedule(draft_team, year)# http://www.espn.com/nfl/schedulegrid

'''Add Total Offense to Dictionary'''
'''Add Total Defense to Dictionary'''
off_pass, def_pass = strength_of_schedule.passing(draft_team, year, weeks, season_type)
off_rush, def_rush = strength_of_schedule.rushing(draft_team, year, weeks, season_type)
for team in draft_team:
    draft_team[team]['tot_off_pass'] = off_pass[team]
    draft_team[team]['tot_def_pass'] = def_pass[team]
    draft_team[team]['tot_off_rush'] = off_rush[team]
    draft_team[team]['tot_def_rush'] = def_rush[team]

strength_of_schedule.tot_pass_rush_def(draft_team)

'''Add Strength of Schedule to Dictionary'''
strength_of_schedule.sos_rank(draft_team, 'tot_off_pass', True, 'off_pass_rank')
strength_of_schedule.sos_rank(draft_team, 'tot_off_rush', True, 'off_rush_rank')
strength_of_schedule.sos_rank(draft_team, 'opp_pass_def', False, 'opp_pass_def_rank')
strength_of_schedule.sos_rank(draft_team, 'opp_rush_def', False, 'opp_rush_def_rank')

a=0
for key, value in sorted(draft_team.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    a = a + 1
    print("%s: %s: %s" % (a, key, value))
#
# '''Build Dictionary of Players'''
# players = {}
# player.off_player_dict(players, year, weeks, season_type)
#
# '''Add Total Previous Year Stats to Players Dictionary'''
# player.off_player_pts(players, year, weeks, season_type)
# print(players)

'''Rank Players'''
# qb = player_ranks.player_ranks(year, 'QB', weeks)
# wr = player_ranks.player_ranks(year, 'WR', weeks)
# rb = player_ranks.player_ranks(year, 'RB', weeks)
# te = player_ranks.player_ranks(year, 'TE', weeks)
# k = player_ranks.player_ranks(year, 'K', weeks)
# print(len(weeks))

'''Previous Year Injuries to Player'''


# pyth_wins 5%
# pts_scored 5%
# tot_off 5%
# prv_player_stats 5%
# projected_player_stats 80%
# injury -5%