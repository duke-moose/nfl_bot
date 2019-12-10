import player_ranks
from merkin_men import SleeperBuild, SleeperPlayersTaken
import tabulate


def nflgame_print(nfl_dict):
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

#cd venv/bin and run nflgame-update-players and run nflgame-update-schedule

year = 2019
# weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
weeks = [11, 12, 13]
season_type = 'REG'
#
# # '''Rank Players'''
qb_nflgame = player_ranks.player_ranks(year, 'QB', weeks)
wr_nflgame = player_ranks.player_ranks(year, 'WR', weeks)
rb_nflgame = player_ranks.player_ranks(year, 'RB', weeks)
te_nflgame = player_ranks.player_ranks(year, 'TE', weeks)
k_nflgame = player_ranks.player_ranks(year, 'K', weeks)

nflgame_print(qb_nflgame)
print(qb_nflgame)

mm = SleeperBuild(year=2019, league_name='merkin_men', league_num=393807404686458880)
mm_dict = SleeperPlayersTaken(me='DeepMooseKnuckle', sleeper_build=mm)
# print(mm_dict.sleeper_dict)
print(mm_dict.taken_list)

'''Correlate nflgame playerid and sleeper_id'''