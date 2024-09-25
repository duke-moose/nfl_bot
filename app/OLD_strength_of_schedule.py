import nflgame

def passing(teams, year, weeks, season_type):
    # Create Team Dictionaries for Offense and Defense Passing.
    team_off = {}
    team_def = {}
    season_length = len(weeks)

    for i in teams:
        team_off[i] = [0] * season_length
        team_def[i] = [0] * season_length

    for week in weeks:
        print('Passing Calc week ' + str(week) + ' of ' + str(season_length))
        games = nflgame.games(year=year, week=week, kind=season_type)

        # Assign Offense passing per week achieved and defensive passing yards allowed.
        for g in games:
            team_off[g.home][week-1] = g.stats_home.passing_yds
            team_off[g.away][week-1] = g.stats_away.passing_yds
            team_def[g.home][week-1] = g.stats_away.passing_yds
            team_def[g.away][week-1] = g.stats_home.passing_yds

    # Sum all of the passing yards.
    off = {}
    defen = {}
    for key in team_off:
        result_off = sum(team_off[key])
        result_defen = sum(team_def[key])
        off[key] = result_off
        defen[key] = result_defen

    return off, defen

def rushing(teams, year, weeks, season_type):
    # Create Team Dictionaries for Offense and Defense Passing.
    team_off = {}
    team_def = {}
    season_length = len(weeks)

    for i in teams:
        team_off[i] = [0] * season_length
        team_def[i] = [0] * season_length

    for week in weeks:
        print('Rushing Calc week ' + str(week) + ' of ' + str(season_length))
        games = nflgame.games(year=year, week=week, kind=season_type)

        # Assign Offense passing per week achieved and defensive passing yards allowed.
        for g in games:
            team_off[g.home][week-1] = g.stats_home.rushing_yds
            team_off[g.away][week-1] = g.stats_away.rushing_yds
            team_def[g.home][week-1] = g.stats_away.rushing_yds
            team_def[g.away][week-1] = g.stats_home.rushing_yds

    # Sum all of the passing yards.
    off = {}
    defen = {}
    for key in team_off:
        result_off = sum(team_off[key])
        result_defen = sum(team_def[key])
        off[key] = result_off
        defen[key] = result_defen

    return off, defen


# Builds a strength of schedule for the year specified.
# def strength_of_schedule(year, season_length, kind):
# def sos(teams, year, weeks, season_type):
def tot_pass_rush_def(teams):
    # Create empty dictionary of teams to fill.
    # sos_teams = dict(teams)

    # Builds dictionary with #1 offense playing the easiest defenses
    # from the previous year and #1 defense playing the easiest offenses.
    for team in teams:
        teams[team]['opp_pass_def'] = 0
        teams[team]['opp_rush_def'] = 0

        for opponent in teams[team]['sched']:
            if opponent != 'BYE':
                # Calculates total yards allowed by defenses in the previous year.
                teams[team]['opp_pass_def'] += teams[opponent]['tot_def_pass']
                teams[team]['opp_rush_def'] += teams[opponent]['tot_def_rush']

    # Build dictionary for passing and rushing rank.
    # 1 offense plays teams that allowed the most yards a
    # 1 defense played teams with the least offense.
def sos_rank(teams, key, reverse, rank_key):
    rank = {}
    for team in teams:
        rank[team] = teams[team][key]

    a = 0
    for key, value in sorted(rank.iteritems(), key=lambda (k, v): (v, k), reverse=reverse):
        a += 1
        teams[key][rank_key] = a