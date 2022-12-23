import json
import requests
from bs4 import BeautifulSoup


class Match(object):

    def __init__(self, match_id):
        self.match_id = match_id
        self.match_url = "https://www.espncricinfo.com/matches/engine/match/{0}.html".format(
            str(match_id))
        self.json_url = "https://www.espncricinfo.com/matches/engine/match/{0}.json".format(
            str(match_id))
        self.json = self.get_json()
        self.unusable_match_data = False
        if self.json:
            self.status = self._status()
            self.series = self._series()
            self.series_name = self._series_name()
            self.series_id = self._series_id()
            self.match_title = self._match_title()
            self.result = self._result()
            self.ground_id = self._ground_id()
            self.ground_name = self._ground_name()
            self.innings_list = self._innings_list()
            self.innings = self._innings()
            self.latest_batting = self._latest_batting()
            self.latest_bowling = self._latest_bowling()
            self.latest_innings = self._latest_innings()
            self.latest_innings_fow = self._latest_innings_fow()
            self.team_1 = self._team_1()
            self.team_1_id = self._team_1_id()
            self.team_1_abbreviation = self._team_1_abbreviation()
            self.team_1_players = self._team_1_players()
            self.team_1_innings = self._team_1_innings()
            self.team_1_run_rate = self._team_1_run_rate()
            self.team_1_overs_batted = self._team_1_overs_batted()
            self.team_1_batting_result = self._team_1_batting_result()
            self.team_2 = self._team_2()
            self.team_2_id = self._team_2_id()
            self.team_2_abbreviation = self._team_2_abbreviation()
            self.team_2_players = self._team_2_players()
            self.team_2_innings = self._team_2_innings()
            self.team_2_run_rate = self._team_2_run_rate()
            self.team_2_overs_batted = self._team_2_overs_batted()
            self.team_2_batting_result = self._team_2_batting_result()

    def get_json(self):
        r = requests.get(self.json_url)
        if r.status_code == 404:
            pass
        elif 'Scorecard not yet available' in r.text:
            pass
        else:
            return r.json()

    def match_json(self):
        return self.json['match']

    def _status(self):
        return self.match_json()['match_status']

    def _match_class(self):
        if self.match_json()['international_class_card'] != "":
            return self.match_json()['international_class_card']
        else:
            return self.match_json()['general_class_card']

    def _series(self):
        if not self.json.get('series'):
            print('Unusable match data for {}'.format(self.json_url))
            self.unusable_match_data = True
        return self.json.get('series')

    def _series_name(self):
        try:
            return self.json['series'][-1]['series_name']
        except:
            return None

    def _series_id(self):
        if self.json.get('series'):
            return self.json['series'][-1]['core_recreation_id']

    def _match_title(self):
        return self.match_json()['cms_match_title']

    def _result(self):
        return self.json['live']['status']

    def _ground_id(self):
        return self.match_json()['ground_id']

    def _ground_name(self):
        return self.match_json()['ground_name']

    def _innings_list(self):
        try:
            return self.json['centre']['common']['innings_list']
        except:
            return None

    def _innings(self):
        return self.json['innings']

    def _latest_batting(self):
        try:
            return self.json['centre']['common']['batting']
        except:
            return None

    def _latest_bowling(self):
        try:
            return self.json['centre']['common']['bowling']
        except:
            return None

    def _latest_innings(self):
        try:
            return self.json['centre']['common']['innings']
        except:
            return None

    def _latest_innings_fow(self):
        return self.json['centre'].get('fow')

    def _team_1(self):
        return self.json['team'][0]

    def _team_1_id(self):
        return self._team_1()['team_id']

    def _team_1_abbreviation(self):
        return self._team_1()['team_abbreviation']

    def _team_1_players(self):
        return self._team_1().get('player', [])

    def _team_1_innings(self):
        try:
            return [inn for inn in self.json['innings'] if inn['batting_team_id'] == self._team_1_id()][0]
        except:
            return None

    def _team_1_run_rate(self):
        try:
            return float(self._team_1_innings()['run_rate'])
        except:
            return None

    def _team_1_overs_batted(self):
        try:
            return float(self._team_1_innings()['overs'])
        except:
            return None

    def _team_1_batting_result(self):
        try:
            return self._team_1_innings()['event_name']
        except:
            return None

    def _team_2(self):
        return self.json['team'][1]

    def _team_2_id(self):
        return self._team_2()['team_id']

    def _team_2_abbreviation(self):
        return self._team_2()['team_abbreviation']

    def _team_2_players(self):
        return self._team_2().get('player', [])

    def _team_2_innings(self):
        try:
            return [inn for inn in self.json['innings'] if inn['batting_team_id'] == self._team_2_id()][0]
        except:
            return None

    def _team_2_run_rate(self):
        try:
            return float(self._team_2_innings()['run_rate'])
        except:
            return None

    def _team_2_overs_batted(self):
        try:
            return float(self._team_2_innings()['overs'])
        except:
            return None

    def _team_2_batting_result(self):
        try:
            return self._team_2_innings()['event_name']
        except:
            return None
