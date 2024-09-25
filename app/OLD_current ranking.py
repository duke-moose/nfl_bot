import nflgame
import tabulate
from collections import defaultdict

## Murkin Men Scoring
scoring = {
    # Passing
    'passing_yds': lambda x: x*0.04,
    'passing_tds': lambda x: x*6,
    'passing_twoptm': lambda x: x*2,
    # Rushing
    'rushing_yds': lambda x: x*.1,
    'rushing_tds': lambda x: x*6,
    'kickret_tds': lambda x: x*6,
    'puntret_tds': lambda x: x*6,
    # 'kickret_yds': lambda x: x*0.1,
    # 'puntret_yds': lambda x: x*0.1,
    'rushing_twoptm': lambda x: x*2,
    # Receiving
    'receiving_tds': lambda x: x*6,
    'receiving_yds': lambda x: x*.1,
    #'receiving_rec': lambda x: x*.5,
    'receiving_twoptm': lambda x: x*2,
    # Kicker
    'kicking_fgm_yds': lambda x: (5 if x >= 50 else (4 if x >= 40 else 3)),
    'kicking_xpmade': lambda x: 1,
    'kicking_xpmissed': lambda x: -1,
    'kicking_fgmissed': lambda x: -1,
    # Various
    'fumbles_lost': lambda x: x*-2,
    'passing_ints' : lambda x: x*-2,
}


def score_player(player):
    score = 0
    for stat in player._stats:
        if stat in scoring:
            score += scoring[stat](getattr(player, stat))
    return score


def std_deviation(scores):
    total = 0
    for i in scores:
        total += i
    avg = total / float(len(scores))
    variance = 0
    for score in scores:
        variance += (avg - score) ** 2
    std = (variance / len(scores)) ** 0.5
    return std


def PL_maker(PL, players, position_list, season_length, week):
    for p in players:
        if p.guess_position not in position_list:
            if PL.get(str(p.playerid), "empty") == "empty":
                PL[str(p.playerid)] = [0] * season_length
                points = score_player(p)
                # print p, p.team, points, position
                PL[str(p.playerid)][week - 1] = points
            elif PL.get(str(p.playerid), "empty") != "empty":
                points = score_player(p)
                # print p, p.team, points, position
                PL[str(p.playerid)][week - 1] = points
    return(PL)


def kicker_pts(year, week):
    games = nflgame.games(year, week)
    plays = nflgame.combine_plays(games)

    fgs_xps = defaultdict(list)
    for play in plays.filter(kicking_fga=True):
        for p in play.players:
            points = score_player(p)
            fgs_xps[str(p.playerid)].append(points)
            # print(str(p), p.kicking_fgm_yds, points)

    plays = nflgame.combine_plays(games)
    for play in plays.filter(kicking_xpa=True):
        for p in play.players:
            points = score_player(p)
            fgs_xps[str(p.playerid)].append(points)
            # print(str(p), p.kicking_xpmade, points)

    for kicker in fgs_xps:
        fgs_xps[kicker] = sum(fgs_xps[kicker])

    return fgs_xps


def player_ranks(year, pos, weeks):
    # Define the variables
    position = pos
    year = year
    PL = {} #Blank dictionary for Players

    if position in ('WR', 'RB'):
        Rank1 = 12 #Top X number of players (most often 12 for RB1 and WR1; 5 for QBs).
        Rank2 = 24 #Top X number of players (most often 24 for RB2 and WR2; 10 for QBs).
        Rank3 = 36 #Top X number of players (most often 36 for RB3 and WR3; 15 for QBs).
        Rank4 = 48 #Top X number of players (most often 48 for RB4 and WR4; 20 for QBs).
    elif position in ('QB', 'TE', 'K'):
        Rank1 = 5 #Top X number of players (most often 12 for RB1 and WR1; 5 for QBs).
        Rank2 = 10 #Top X number of players (most often 24 for RB2 and WR2; 10 for QBs).
        Rank3 = 15 #Top X number of players (most often 36 for RB3 and WR3; 15 for QBs).
        Rank4 = 20 #Top X number of players (most often 48 for RB4 and WR4; 20 for QBs).
    elif position == 'ALL':
        Rank1 = 20
        Rank2 = 40
        Rank3 = 60
        Rank4 = 80
        max_pl = 200

    #List of all players not in a specific position (i.e., QB has all players
    # in the list except QBs). RBs are sometimes blank.
    QB = ('', 'K', 'WR', 'TE', 'RB', 'DB', 'DEF', 'OLB', 'CB', 'DE', 'C',
          'P', 'SS', 'ILB', 'FS', 'OT', 'LS', 'LB', 'T', 'OG', 'FB', 'MLB',
          'DT', 'G', 'SAF', 'DL', 'NT', 'OL')
    WR = ('K', 'QB', 'TE', 'RB', 'DB', 'DEF', 'OLB', 'CB', 'DE', 'C', 'P',
          'SS', 'ILB', 'FS', 'OT', 'LS', 'LB', 'T', 'OG', 'FB', 'MLB', 'DT',
          'G', 'SAF', 'DL', 'NT', 'OL')
    RB = ('K', 'WR', 'TE', 'QB', 'DB', 'DEF', 'OLB', 'CB', 'DE', 'C', 'P',
          'SS', 'ILB', 'FS', 'OT', 'LS', 'LB', 'T', 'OG', 'MLB', 'DT', 'G',
          'SAF', 'DL', 'NT', 'OL')
    TE =  ('', 'K', 'WR', 'QB', 'RB', 'DB', 'DEF', 'OLB', 'CB', 'DE', 'C',
           'P', 'SS', 'ILB', 'FS', 'OT', 'LS', 'LB', 'T', 'OG', 'FB', 'MLB',
           'DT', 'G', 'SAF', 'DL', 'NT', 'OL')
    K =  ('QB', 'WR', 'TE', 'RB', 'DB', 'DEF', 'OLB', 'CB', 'DE', 'C',
          'P', 'SS', 'ILB', 'FS', 'OT', 'LS', 'LB', 'T', 'OG', 'FB', 'MLB',
          'DT', 'G', 'SAF', 'DL', 'NT', 'OL')
    ALL = ('DB', 'DEF', 'OLB', 'CB', 'DE', 'C', 'P', 'SS', 'ILB', 'FS', 'OT',
           'LS', 'LB', 'T', 'OG', 'MLB', 'DT', 'G', 'SAF', 'DL', 'NT', 'OL')

    season_length = len(weeks)

    #This for loop fills out the blank dictionary with points
    for w in weeks:
        week = w-min(weeks)+1
        games = nflgame.games(year=year, week=w)
        players = nflgame.combine_max_stats(games)

        print('Week ' + str(w))#Displays the week count so user can check where the code is.
        # Filter for player position and sort by most important attribute for points.
        if position == 'QB':
            position_list = QB
            PL = PL_maker(PL, players, position_list, season_length, week)
        elif position == 'WR':
            position_list = WR
            PL = PL_maker(PL, players, position_list, season_length, week)
        elif position == 'TE':
            position_list = TE
            PL = PL_maker(PL, players, position_list, season_length, week)
        elif position == 'RB':
            position_list = RB
            PL = PL_maker(PL, players, position_list, season_length, week)
        elif position == 'K':
            position_list = K
            PL = PL_maker(PL, players, position_list, season_length, week)
        elif position == 'ALL':
            position_list = ALL
            PL = PL_maker(PL, players, position_list, season_length, week)
        else:
            print("Check the position entry is correct.")
            break

    if position == 'K':
        for w in weeks:
            week = w - min(weeks) + 1
            kicker = kicker_pts(year, w) # need to output one number to replace the constructed PL dictionary
            # print(kicker)
            for player, points in kicker.iteritems():

                try:
                    PL[player][week-1] = points
                except KeyError:
                    pass
                    # troubleshoot.find_player(player)

    #Prints an organized table of the players points by week for an easy check.
    # print tabulate.tabulate(PL, headers = "keys")

    ###################################
    #This Section Ranks Players based on their percentage to achieve top playing ability
    ###################################
    Pt_rank = {} #Blank dictionary for Rank1, Rank2, Rank3, and Rank4
    PL_rank ={} #Blank dictionary for Player ranking.
    # for week in weeks:
    for w in weeks:
        week = w - min(weeks) + 1
    # for weeks in range(season_length):
        PL_score = []  # Make a blank list to store weekly scores
        # PL1, PL2, PL3, PL4 = 0, 0, 0, 0
        for key in PL:
            PL_score.append(PL[key][week-1])
            PL_rank[key] = {'Rank Score': [0] * 7}
        #Sort the scores and determine top Rank1, Rank2, Rank3, and Rank4 players.
        PL_score.sort(reverse=True)

        ##Error checker
        #print PL_score[Rank1-1], PL_score[Rank2-1], PL_score[Rank3-1], PL_score[Rank4-1]

        Pt_rank["Week "+str(week)]=[PL_score[Rank1-1], PL_score[Rank2-1], PL_score[Rank3-1], PL_score[Rank4-1]]

    pts_max = 0
    for key in PL:
        PL1_total, PL2_total, PL3_total, PL4_total = 0, 0, 0, 0

        for w in weeks:
            week = w - min(weeks)
            if PL[key][week] >= Pt_rank["Week " + str(week +1)][0]:
                PL1_total = PL1_total + 1
            elif PL[key][week] >= Pt_rank["Week " + str(week +1)][1]:
                PL2_total = PL2_total + 1
            elif PL[key][week] >= Pt_rank["Week " + str(week +1)][2]:
                PL3_total = PL3_total + 1
            elif PL[key][week] >= Pt_rank["Week " + str(week +1)][3]:
                PL4_total = PL4_total + 1
            else:
                0
        'Rank Score'
        PL_rank[key]['Rank Score'][1] = float(PL1_total) / season_length * 100.0
        PL_rank[key]['Rank Score'][2] = float(PL1_total + PL2_total) / season_length * 100.0
        PL_rank[key]['Rank Score'][3] = float(PL1_total + PL2_total + PL3_total) / season_length * 100.0
        PL_rank[key]['Rank Score'][4] = float(PL1_total + PL2_total + PL3_total + PL4_total) / season_length * 100.0
        PL_rank[key]['Rank Score'][5] = float(sum(PL[key]))
        PL_rank[key]['Rank Score'][6] = float(std_deviation(PL[key]))
        if int(sum(PL[key])) > pts_max:  # Finds the maximum points scored for a week.
            pts_max = int(sum(PL[key]))

    for key in PL_rank:
        # PL_rank[key][0] = (sum(PL_rank[key][1:5]) / 100 + 2 * PL_rank[key][5] / pts_max) / 6
        PL_rank[key]['Rank Score'][0] = (sum(PL_rank[key]['Rank Score'][1:5])/100 + \
                                         2*PL_rank[key]['Rank Score'][5]/pts_max)/6 #Determine player rank using the point percentages and 2 times the points b/c pts are most important.

    print(pts_max)

    #Re-assign PlayerID with Player Name
    games = nflgame.games(year, weeks)
    players = nflgame.combine_max_stats(games)
    for p in players:
        if p.playerid in PL.keys():
            player_label = str(p) + '-' + str(p.guess_position) + '-' + str(p.team)
            PL_rank[player_label] = PL_rank.pop(p.playerid)
            PL_rank[player_label]['pos'] = position
            PL_rank[player_label]['gsis_id'] = p.playerid
            PL[p] = PL.pop(p.playerid)

    return {'PL': PL, 'Pt_rank': Pt_rank, 'PL_rank': PL_rank}

    #Save Results as a Binary file in Pickle format
    # year = str(year)
    # f_name = position + '_stats' + year[2:4] + '.pckl'
    # with open(f_name, 'wb') as f:
    #     pickle.dump(PL, f)
    # f_name = position + '_rank' + year[2:4] + '.pckl'
    # with open(f_name, 'wb') as f:
    #     pickle.dump(PL_rank, f)


def nflgame_print(nfl_dict):
    """Takes a dictionary of players and points and prints it for readability."""
    print(tabulate.tabulate(nfl_dict['PL'], headers="keys"))
    print('')
    print("Weekly Points Ranking Criteria")
    print(tabulate.tabulate(nfl_dict['Pt_rank'], headers="keys"))
    a = 0
    print("Player Percent Rankings: P1, P2, P3, P4, total points, and std_dev (QB and TE top 5, RB and WR top 12)")
    print('')
    for key, value in sorted(nfl_dict['PL_rank'].iteritems(), key=lambda (k, v): (v, k), reverse=True):
        a = a + 1
        print("%s: %s: %s" % (a, key, value['Rank Score']))
        nfl_dict['PL_rank'][key]['Rank'] = a




if __name__ == "__main__":
    """
    Print Standard Player Ranking like all previous years

    1. Update nflgame
        cd venv/bin and run nflgame-update-players and run nflgame-update-schedule

    Points Ranking Script #########################################
    Steps
    1. Define position, player rankings, year and weeks of interest.
    2. Run through loop to calculate the points each player would attain based on 2017 Murkin Men Criteria
    3. Rank players by position based on their points achieved in comparisson to their peers.
    4. Save everything in a binary format (i.e., pickle) for quick access if there is not internet connection
        for NFL game.

    """
    year = 2019
    weeks = [1, 2]
    season_type = 'REG'
    #
    # # '''Rank Players'''
    qb_nflgame = player_ranks(year, 'QB', weeks)
    wr_nflgame = player_ranks(year, 'WR', weeks)
    rb_nflgame = player_ranks(year, 'RB', weeks)
    te_nflgame = player_ranks(year, 'TE', weeks)
    k_nflgame = player_ranks(year, 'K', weeks)

    nflgame_print(qb_nflgame)
    nflgame_print(wr_nflgame)
    nflgame_print(rb_nflgame)
    nflgame_print(te_nflgame)
    nflgame_print(k_nflgame)
