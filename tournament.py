import numpy as np
import pandas as pd


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
        points = {player: 0 for player in self.players}
        for index, match in self.matchlist.iterrows():
            points[match['White']] += match['pWhite']
            points[match['Black']] += match['pBlack']
        return points


