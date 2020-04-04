import nflgame
import fixes
import pythagorean_wins as pw
import schedule
import strength_of_schedule


def draft_team(year, weeks, season_type):
    """Build Draft Dictionary of Teams adding all of their stats to one draft_team object."""
    '''Build Dictionary of Teams
    fixes team names to correct from old locations to new.
    TODO: Coordinate Las Vegas and Oakland'''
    teams_list = fixes.build_dict(nflgame.teams)

    '''Add Pythagorean Wins to Dictionary'''
    pw.pythagorean_calculated_wins(teams_list, year-1, weeks, season_type)

    '''Build 2019 Schedule'''
    schedule.schedule(teams_list, year)# http://www.espn.com/nfl/schedulegrid

    '''Add Total Offense to Dictionary'''
    '''Add Total Defense to Dictionary'''
    off_pass, def_pass = strength_of_schedule.passing(teams_list, year-1, weeks, season_type)
    off_rush, def_rush = strength_of_schedule.rushing(teams_list, year-1, weeks, season_type)
    for team in teams_list:
        teams_list[team]['tot_off_pass'] = off_pass[team]
        teams_list[team]['tot_def_pass'] = def_pass[team]
        teams_list[team]['tot_off_rush'] = off_rush[team]
        teams_list[team]['tot_def_rush'] = def_rush[team]

    strength_of_schedule.tot_pass_rush_def(teams_list)

    '''Add Strength of Schedule to Dictionary'''
    strength_of_schedule.sos_rank(teams_list, 'tot_off_pass', True, 'off_pass_rank')
    strength_of_schedule.sos_rank(teams_list, 'tot_off_rush', True, 'off_rush_rank')
    strength_of_schedule.sos_rank(teams_list, 'opp_pass_def', False, 'opp_pass_def_rank')
    strength_of_schedule.sos_rank(teams_list, 'opp_rush_def', False, 'opp_rush_def_rank')

    a=0
    for key, value in sorted(teams_list.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        a = a + 1
        print("%s: %s: %s" % (a, key, value))

    return teams_list


def draft_player(year, weeks, season_type):
    """Build Dictionary of Players"""
    players = {}
    player.off_player_dict(players, year, weeks, season_type)


def off_player(play_dict, year, weeks, season_type):
    pass

    # '''Add Total Previous Year Stats to Players Dictionary'''
    # player.off_player_pts(players, year, weeks, season_type)

'''Previous Year Injuries to Player'''
# pyth_wins 5%
# pts_scored 5%
# tot_off 5%
# prv_player_stats 5%
# projected_player_stats 80%
# injury -5%


games = nflgame.games(year=2019, week=1)
players = nflgame.combine_max_stats(games)
for p in players:
    # print(dir(p))
    print(str(p), p.playerid, p.guess_position)
