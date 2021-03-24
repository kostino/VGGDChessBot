import pandas as pd
from tabulate import tabulate


class Tournament:
    def __init__(self, players):
        self.players = players
        self.matchlist = pd.DataFrame(columns=['White', 'Black', 'Result', 'pWhite', 'pBlack'])

    def addMatch(self, white, black, result):
        new_match = {}
        if result == '1-0':
            new_match['pBlack'] = 0
            new_match['pWhite'] = 1
        elif result == '0-1':
            new_match['pBlack'] = 1
            new_match['pWhite'] = 0
        elif result == 'draw':
            new_match['pBlack'] = 0.5
            new_match['pWhite'] = 0.5
        else:
            print('Invalid result')
            return
        new_match['White'] = white
        new_match['Black'] = black
        new_match['Result'] = result
        self.matchlist = self.matchlist.append(new_match, ignore_index=True)

    def saveMatches(self):
        self.matchlist.to_csv('matchlist.csv', index=False)

    def getRanking(self):
        points = {player: [0, 0] for player in self.players}
        for index, match in self.matchlist.iterrows():
            points[match['White']][0] += match['pWhite']
            points[match['Black']][0] += match['pBlack']
            points[match['White']][1] += 1
            points[match['Black']][1] += 1
        return points

    def prettyRanking(self):
        ranking = self.getRanking()
        ranking = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))
        headers = ['Player', 'Points', 'Games']
        pretty_ranking = tabulate([[k, v[0], v[1]] for k, v in ranking.items()], headers=headers, tablefmt='psql')
        return pretty_ranking

    def prettyMatchlist(self):
        return tabulate(self.matchlist[['White', 'Black', 'Result']], tablefmt='psql', headers='keys')

