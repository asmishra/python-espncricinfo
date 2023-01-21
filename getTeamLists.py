from summary import Summary


class GetTeamLists():
    def __init__(self, team_list=[]):
        self.summary = Summary(team_list)
        self.matches = self.summary.matches

    def chunkstring(self, s, length):
        return (s[0 + i: length + i] for i in range(0, len(s), length))

    def run(self):
        result = ''
        for match in self.matches:
            if not hasattr(match, 'team_1'):
                continue

            result += self.printPlayerList(match)
        return 'uh-oh, maybe they\'re not playing? (or try full name)' if result == '' else result

    def getCurrentMatches(self):
        retStr = ''
        for match in self.matches:
            retStr += '**Series: {}, {} vs. {}**'.format(match.match_title,
                                                         match.team_1['team_name'],
                                                         match.team_2['team_name']) + '\n'
        return self.chunkstring(retStr, 4096)

    def printPlayerList(self, match):
        retStr = ''
        retStr += '**Series: {}, {} vs. {}**'.format(match.match_title,
                                                     match.team_1['team_name'],
                                                     match.team_2['team_name']) + '\n'

        def extractPlayerNames(playerList):
            s = ''
            for player in playerList:
                s += '{}'.format(player['card_long']) + '\n'
            return s

        # Team 1
        retStr += '**{}**:'.format(match.team_1['team_name'],) + '\n'
        retStr += extractPlayerNames(match.team_1_players)
        retStr += '\n'
        # Team 2
        retStr += '**{}**:'.format(match.team_2['team_name'],) + '\n'
        retStr += extractPlayerNames(match.team_2_players)
        retStr += '\n'
        return retStr
