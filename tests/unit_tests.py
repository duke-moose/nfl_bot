# test previous year wins, losses, yardage
# http://www.espn.com/nfl/statistics/team/_/stat/rushing

import unittest
import requests
import os

class TestMerkinMen(unittest.TestCase):
    directory = '../merkin_men_2019'
    sleeper_url = 'https://api.sleeper.app/v1/league/'
    merkin_men_league_id = 393807404686458880

    def test_sleeper_url(self):
        api_url = os.path.join(self.sleeper_url + str(self.merkin_men_league_id))
        response = requests.get(api_url)
        self.assertEqual(response.status_code, 200, 'url to sleeper is incorrect, check url and league id')

    def test_directory(self):
        path = os.path.isdir(self.directory)
        self.assertTrue(path, 'No directory: %s' % self.directory)

    def test_users(self):
        users_file = 'merkin_men_users_2019.json'
        file_path = os.path.join(self.directory, users_file)
        self.assertTrue(os.path.isfile(file_path), 'file: %s not in %s' % (users_file, self.directory))


if __name__ == '__main__':
    unittest.main()
# suite = unittest.TestLoader().loadTestsFromTestCase(TestMerkinMen)
# unittest.TextTestRunner(verbosity=2).run(suite)