import nflgame
from math import log

'''pyth_wins: Theoretical wins a team should have achieved based on point differential'''
def pyth_calc(pf, pa):
    '''
    EXP = 1.5 * LOG((PF + PA) / 16)
    PYTH = ((PF ^ EXP) / (PF ^ EXP + PA ^ EXP)) * 16
    '''
    exp = 1.5 * log((pf + pa)/16)
    pyth = ((pf ** exp) / (pf ** exp + pa ** exp)) * 16
    return pyth

#####################################################################################
# year = 2018
# week = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def pythagorean_calculated_wins(teams, year, weeks, season_type):

    print('Pythagorean Wins Calculator')
    cat_name = 'pyth_wins'

    '''Add Pyth Results Key to Teams Dictionary'''
    for team in teams:
        teams[team][cat_name] = [0] * 5

    games = nflgame.games(year=year, week=weeks, kind=season_type)
    for game in games:
        '''Calculate Total Number of Wins'''
        if game.score_home > game.score_away:
            teams[game.home][cat_name][2] += 1
        elif game.score_home < game.score_away:
            teams[game.away][cat_name][2] += 1

        '''Summation of points scored'''
        teams[game.home][cat_name][3] += game.score_home
        teams[game.away][cat_name][3] += game.score_away
        teams[game.home][cat_name][4] += game.score_away
        teams[game.away][cat_name][4] += game.score_home

    for team in teams:
        pf = teams[team][cat_name][3]
        pa = teams[team][cat_name][4]
        pyth_wins = pyth_calc(pf, pa)
        teams[team][cat_name][1] = pyth_wins

        actual_wins = teams[team][cat_name][2]
        adj_wins = pyth_wins - actual_wins
        teams[team][cat_name][0] = adj_wins

    # print 'Pythagorean Analysis of '+str(year)+' teams'
    # print 'Results show Pyth#, Adj_wins, actual_wins, Score_for, Score_against, '
    # a = 0
    # for key, value in sorted(teams.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    #     a = a + 1
    #     print "%s: %s: %s" % (a, key, value)
    return teams