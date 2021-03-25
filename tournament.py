import pandas as pd
from tabulate import tabulate
from os.path import isfile


class Tournament:
    def __init__(self, players):
        self.players = players
        if isfile('matchlist.csv'):
            self.matchlist = pd.read_csv('matchlist.csv')
        else:
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
        ranking = dict(sorted(ranking.items(), key=lambda item: item[1][0], reverse=True))
        headers = ['Player', 'Points', 'Games']
        pretty_ranking = tabulate([[k, v[0], v[1]] for k, v in ranking.items()], headers=headers, tablefmt='psql')
        return pretty_ranking

    def prettyMatchlist(self):
        return tabulate(self.matchlist[['White', 'Black', 'Result']], tablefmt='psql', headers='keys')

    def prettyResults(self):
        ranking = self.getRanking()
        ranking = dict(sorted(ranking.items(), key=lambda item: item[1][0], reverse=True))
        players_sorted = ranking.keys()
        cols = ['Player']
        cols.extend(players_sorted)
        cols.extend(['Points', 'Games'])
        results = pd.DataFrame(columns=cols)
        for player, points_and_games in ranking.items():
            row = {'Player': player, 'Points': points_and_games[0], 'Games': points_and_games[1]}
            for opponent in players_sorted:
                if opponent == player:
                    row[opponent] = '-'
                else:
                    row[opponent] = ' '
            results = results.append(row, ignore_index=True)
        results = results.set_index('Player')
        results = results.astype({player: float for player in players_sorted}, errors='ignore')
        for index, match in self.matchlist.iterrows():
            results.loc[match['White'], match['Black']] = match['pWhite'] \
                if results.loc[match['White'], match['Black']] == ' ' \
                else results.loc[match['White'], match['Black']] + match['pWhite']
            results.loc[match['Black'], match['White']] = match['pBlack'] \
                if results.loc[match['Black'], match['White']] == ' ' \
                else results.loc[match['Black'], match['White']] + match['pBlack']
        return tabulate(results, tablefmt='psql', headers='keys')