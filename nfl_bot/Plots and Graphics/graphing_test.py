# Plotting Tutorial
# http://wseaton.com/pulling-data-with-nflgame.html

# script might require Tkinter (sudo apt-get install python-tk)
import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

games = nflgame.games(year=2019, week=1)
players = nflgame.combine_game_stats(games)

# First Figure
fig = plt.figure(figsize=(12, 8))

ax1 = fig.add_subplot(211)
ax1.set_title('age vs. rushing yds', fontsize=14, color='black')
fig.subplots_adjust(top=0.85)

ax1.set_ylabel('age (years)')
ax1.set_xlabel('rushing_yds')

plt.style.use('ggplot')

for p in players.rushing():
    if p.player is not None:
        years_old = float((datetime.datetime.today() - datetime.datetime.strptime(p.player.birthdate, '%m/%d/%Y')).days) / 365
        plt.scatter(p.rushing_yds, years_old)

# Figure 2
runs = pd.Series([p.rushing_yds for p in players.rushing()])
# fig = plt.figure(figsize=(12, 8))
ax2 = fig.add_subplot(212)
ax2.set_title('rushing yards 2019 season', fontsize=14, color='black')

ax2.set_ylabel('frequency')
ax2.set_xlabel('bins')

plt.style.use('ggplot')
plt.hist(runs, color='purple')
plt.tight_layout()

# Figure 3
fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111)
ax.set_title('height and weight of 2018 NFL RBs and FBs', fontsize=14, color='black')

fig.subplots_adjust(top=0.85)

ax.set_ylabel('height')
ax.set_xlabel('weight')

plt.style.use('ggplot')

for p in players.rushing():
    if p.player.position in ['RB', 'FB']:
        plt.scatter(p.player.weight, p.player.height, c='green')

        if p.player.name in ['Josh Jacobs', 'Mark Ingram']:
            plt.annotate(
                p.player.name + ', ' + p.player.team, color='black',
                xy = (p.player.weight, p.player.height), xytext = (p.player.weight, p.player.height-1.5), alpha = 0.9,
                xycoords='data',
                textcoords='data',
                arrowprops=dict(arrowstyle="-|>", color='black',
                                connectionstyle="arc3"))

plt.show()

# ###############################################################
# # Basketball Court
# # http://wseaton.com/animating-nba-shot-charts-with-matplotlib.html
# from matplotlib.patches import Circle, Rectangle, Arc
# def draw_court(ax=None, color='black', lw=2, outer_lines=False):
#     # If an axes object isn't provided to plot onto, just get current one
#     if ax is None:
#         ax = plt.gca()
#
#     # Create the various parts of an NBA basketball court
#
#     # Create the basketball hoop
#     # Diameter of a hoop is 18" so it has a radius of 9", which is a value
#     # 7.5 in our coordinate system
#     hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
#
#     # Create backboard
#     backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
#
#     # The paint
#     # Create the outer box 0f the paint, width=16ft, height=19ft
#     outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
#                           fill=False)
#     # Create the inner box of the paint, widt=12ft, height=19ft
#     inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
#                           fill=False)
#
#     # Create free throw top arc
#     top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
#                          linewidth=lw, color=color, fill=False)
#     # Create free throw bottom arc
#     bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
#                             linewidth=lw, color=color, linestyle='dashed')
#     # Restricted Zone, it is an arc with 4ft radius from center of the hoop
#     restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
#                      color=color)
#
#     # Three point line
#     # Create the side 3pt lines, they are 14ft long before they begin to arc
#     corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
#                                color=color)
#     corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
#     # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
#     # I just played around with the theta values until they lined up with the
#     # threes
#     three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
#                     color=color)
#
#     # Center Court
#     center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
#                            linewidth=lw, color=color)
#     center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
#                            linewidth=lw, color=color)
#
#     # List of the court elements to be plotted onto the axes
#     court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
#                       bottom_free_throw, restricted, corner_three_a,
#                       corner_three_b, three_arc, center_outer_arc,
#                       center_inner_arc]
#
#     if outer_lines:
#         # Draw the half court line, baseline and side out bound lines
#         outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
#                                 color=color, fill=False)
#         court_elements.append(outer_lines)
#
#     # Add the court elements onto the axes
#     for element in court_elements:
#         ax.add_patch(element)
#
#     return ax
#
# plt.figure(figsize=(12,11))
# # plt.scatter(shot_df.LOC_X, shot_df.LOC_Y, c='r')
# plt.title('Basketball Court')
# plt.grid(False)
# draw_court()
#
# plt.xlim(-250,250)
# plt.ylim(422.5, -47.5)
#
# plt.tick_params(labelbottom=False, labelleft=False)
# plt.show()
