from summary import Summary


class GetTeamLists():
    def __init__(self, team_list=[]):
        self.summary = Summary(team_list)
        self.matches = self.summary.matches

    def run(self):
        for match in self.matches:
            if not hasattr(match, 'team_1'):
                continue
            print('Series: {}, {} vs. {}'.format(match.match_title,
                                                 match.team_1_abbreviation,
                                                 match.team_2_abbreviation))
            self.printPlayerList(match)

    def printPlayerList(self, match):
        print('{}:'.format(match.match_title))

        def extractPlayerNames(playerList):
            for player in playerList:
                print('{}'.format(player['card_long']))
            print()

        # Team 1
        print('{}:'.format(match.team_1_abbreviation))
        extractPlayerNames(match.team_1_players)
        # Team 2
        print('{}:'.format(match.team_2_abbreviation))
        extractPlayerNames(match.team_2_players)


# Will fail for cases where a team isn't found at the moment
teamLists1 = GetTeamLists([])
teamLists1.run()

teamLists2 = GetTeamLists(["India"])
teamLists2.run()
