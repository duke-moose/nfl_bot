import matplotlib.pyplot as plt
import fantasy_draft_old.Unpickle

# pickle_path = '/home/sogood/nfl_stats/foosbawl_bot/fantasy_draft/pickle/'
file = '2017_116_Off_pts.pckl'
# Off_rank = Unpickle.unpickle('2016_116_Off_rank.pckl')
Off_pts = fantasy_draft_old.Unpickle.unpickle(file)
# Def_rank = Unpickle.unpickle('2016_116_Def_rank.pckl')
offense_position_dict = ['QB', 'WR', 'RB', 'TE', 'K']
plot_positions = dict.fromkeys(offense_position_dict, None)
for player in Off_pts:
    player_position = Off_pts[player][1]
    weekly_points_dict = 3
    print player_position
    if plot_positions[player_position] is None:
        plot_positions[player_position] = Off_pts[player][weekly_points_dict]
    else:
        plot_positions[player_position] = plot_positions[player_position] + Off_pts[player][weekly_points_dict]

print plot_positions
for position in plot_positions:
    print "%s: %d" % (position, max(plot_positions[position]))

QB = plot_positions['QB']
RB = plot_positions['RB']
WR = plot_positions['WR']
TE = plot_positions['TE']
K = plot_positions['K']

plt.figure(1)


n_bins = 20
points_range = [0, 26]

plt.subplot(511)
plt.hist(QB, n_bins, range=points_range, normed=1, histtype='bar', color='red', label='QB')
# ax0.legend(prop={'size': 20})
# ax0.set_title('QB')

plt.subplot(512)
plt.hist(RB, range=points_range, normed=1, histtype='bar')
# ax1.set_title('RB')

plt.subplot(513)
plt.hist(WR, range=points_range, histtype='step', stacked=True, fill=False)
# ax2.set_title('WR')

plt.subplot(514)
plt.hist(TE, range=points_range, histtype='bar')
# ax3.set_title('TE')

plt.subplot(515)
plt.hist(K, range=points_range, histtype='bar')
# ax4.set_title('K')

plt.tight_layout()
plt.show()