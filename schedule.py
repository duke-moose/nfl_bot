import json
import os
import fixes
"""Builds Current Season Schedule"""

def schedule(teams, year):

    print('Generating Schedule')

    # 1. Complete scrape of season with Scrapy Script.
    # 2. Load JSON file and parse into dictionary.
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'scrapy_nfl/' + str(year) + '_nfl_schedule.json')

    season_schedule = {}

    with open(filename) as f:
        d = json.load(f)
        for item in d:
            team = item['team'].encode('utf-8')
            team = fixes.team_fix(team)
            opponents = []
            for o in item['opponents']:
                o = o.replace("@","") #Remove "@" symbol because it's not currently needed.
                o = fixes.team_fix(o)
                opponents.append(o.encode('utf-8'))
            # season_schedule[team] = opponents
            teams[team]['sched'] = opponents
    # return season_schedule