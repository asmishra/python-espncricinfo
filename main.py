from summary import Summary


class GetTeamLists():

    def setup(self):
        self.summary = Summary()
        self.matches = self.summary.matches

    def run(self):
        self.setup()

        # Match list
        specificMatches = self.getSpecificMatches('IND', self.matches)
        if specificMatches == []:
            specificMatches = self.matches

        for match in specificMatches:
            print('Series: {}, {} vs. {}'.format(match.match_title,
                                                 match.team_1_abbreviation,
                                                 match.team_2_abbreviation))
            self.printPlayerList(match.team_1_abbreviation,
                                 match.team_1_players)
            self.printPlayerList(match.team_2_abbreviation,
                                 match.team_2_players)

    def getSpecificMatches(self, teamName, matchList):
        specificMatchList = []
        for match in matchList:
            if match.team_1_abbreviation == teamName or match.team_2_abbreviation == teamName:
                specificMatchList.append(match)
        return specificMatchList

    def printPlayerList(self, team, playerList):
        print('{}:'.format(team))
        for player in playerList:
            print('{}'.format(player['card_long']))
        print('')


getTeamLists = GetTeamLists()
getTeamLists.run()
