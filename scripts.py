import json
import os

import nfl_bot

"""Create Draft Team and Player Ranks"""
year = 2019
draft_loc = os.path.join('nfl_bot' , 'merkin_men_2019')

"""Draft Team Dictionary"""
dt_file = 'draft_team.json'
if os.path.isfile(os.path.join(draft_loc, dt_file)):
    with open(os.path.join(draft_loc, dt_file), 'r') as fp:
        dt = json.load(fp)
else:
    dt = nfl_bot.draft_team(year=2019, weeks=range(1, 18), season_type='REG')
    with open(os.path.join(draft_loc, dt_file), 'w') as fp:
        json.dump(dt, fp)

"""Draft Player Dictionary"""
dp_file = 'draft_player.json'
# if os.path.isfile(os.path.join(draft_loc, dp_file)):
#     with open(os.path.join(draft_loc, dp_file), 'r') as fp:
#         dt = json.load(fp)
# else:
#     dt = nfl_bot.draft_player(year=2019, weeks=range(1, 18), season_type='REG')
#     with open(os.path.join(draft_loc, dp_file), 'w') as fp:
#         json.dump(dt, fp)


