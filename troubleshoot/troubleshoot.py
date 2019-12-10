import nflgame

year = 2019
weeks = [1, 2]


def find_player(player_number):
    games = nflgame.games(year, weeks)
    players = nflgame.combine_max_stats(games)
    for p in players:
        if p.playerid == player_number:
            print(str(p), p.playerid, p.guess_position)


def player_dir(player_number, year, week):
    games = nflgame.games(year, week)
    players = nflgame.combine_max_stats(games)
    for p in players:
        if p.playerid == player_number:
            print(str(p), p.guess_position, dir(p))

def plays_in_game(year, week, team):
    games = nflgame.games(year, week, home=team, away=team)
    plays = nflgame.combine_plays(games)
    for p in plays:
        print(p)


if __name__ == "__main__":
    # find_player('00-0031203')
    # player_dir('00-0031203', 2019, 1)
    player_dir('00-0030063', 2019, 7)
    # plays_in_game(2019, 4, 'TB')
