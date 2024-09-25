import os

import pandas as pd

class PBP(object):
    def __init__(self, fp):
        self.play_by_play = self.open_csv_gz(fp)

    def open_csv_gz(self, file):
        if os.path.isfile(file):
            data = pd.read_csv(file, compression= 'gzip', low_memory= False)
            return data
        else:
            raise FileNotFoundError(f'{fp} was not found or is a directory.')

    def make_player(self):
        data = self.play_by_play.copy()

        # Get rushing yards and touchdowns
        rush = data.groupby('rusher_player_name')[[
            'lateral_rushing_yards', 'rushing_yards', 'rush_touchdown',
            'rush_attempt', 'fumble', 'fumble_lost', 'posteam'
            ]].sum().reset_index()
        print(rush)

        # Get receiving yards and pass touchdowns
        receive = data.groupby('receiver_player_name')[[
            'lateral_receiving_yards', 'receiving_yards', 'pass_touchdown',
            'pass_attempt', 'fumble', 'fumble_lost', 'posteam'
            ]].sum().reset_index()
        print(receive)

        # Get passing yards
        passing = data.groupby('name')[[
            'passing_yards', 'pass_touchdown', 'interception', 'fumble',
            'fumble_lost', 'posteam'
            ]].sum().reset_index()
        print(passing)

1. Add kick
2. Add player position
3. Combine all dataframes into a single dataframe then dictionary.


if __name__ == '__main__':
    file_path = '../data/play_by_play_2024.csv.gz'
    pbp = PBP(file_path)
    # print(pbp.play_by_play.head())
    # print(pbp.play_by_play.columns.tolist())
    pbp.make_player()
