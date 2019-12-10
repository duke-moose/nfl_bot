'''Fix Jacksonville, LA Rams, & LA Chargers'''
def team_fix(team):
    if team in ['JAC']:
        team_new = 'JAX'
    elif team in ['STL', 'LAR']:
        team_new = 'LA'
    elif team in ['SD']:
        team_new = 'LAC'
    elif team in ['WSH']:
        team_new = 'WAS'
    else:
        team_new = team
    return team_new

def build_dict(list):
    d = dict()
    '''Build Dictionary of Teams'''
    for item in list:
        '''
        nflgame.teams = ['NO', 'New Orleans', 'Saints', 'New Orleans Saints', 'N.O.', 'NOR']
        '''
        team_name = team_fix(item[0])
        d[team_name] = {}
    return d

