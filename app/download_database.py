import os

import wget

def download_file(url):
    '''
    Download nflverse saved database file as byte compressed file.

    Example:
        download_file()
    '''
    # Save file to data directory
    os.chdir('../data')
    wget.download(url)

if __name__ == '__main__':
    # for i in range(1999, 2025):
    #     print(i)
    nfl_url = 'https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2024.csv.gz'
    download_file(nfl_url)
