import requests
from bs4 import BeautifulSoup
from match import Match
import re


class Summary(object):
    def __init__(self, team_list=[]):
        self.url = "http://static.cricinfo.com/rss/livescores.xml"
        self.xml = self.get_xml()
        self.match_ids = self._match_ids()
        self.match_names = self._match_names()
        if not team_list:
            self.matches = self._build_matches()
        else:
            self.matches = []
            # FIXME - this is yucky and there's no error checking for cases where a team name isn't found
            # maybe implement fuzzy matching later
            for team_name in team_list:
                for index, match_name in enumerate(self.match_names):
                    if team_name.lower() in match_name.lower():
                        self.matches.append(
                            self._build_match(self.match_ids[index]))

    def get_xml(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            return BeautifulSoup(r.text, 'xml')
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def _match_names(self):
        return [re.findall('\>(.*)\<', str(x.description))[0]
                for x in self.xml.findAll('item')]

    def _match_ids(self):
        return [x.link.text.split(".html")[0].split(
            '/')[6] for x in self.xml.findAll('item')]

    def _build_match(self, match_id):
        return Match(match_id)

    def _build_matches(self):
        return [self._build_match(m) for m in self.match_ids]
