"""
Created on Tue May  2 01:24:16 2017

@author: Lisa Denzer
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from GameDataCleaning import GameDataCleaning

great_game_requirement = 80

def greatest(NA, EU, JP):
    if NA > EU and NA > JP:
        theGreatest = 1
    elif EU > NA and EU > JP:
        theGreatest = 2
    else:
        theGreatest = 3
    return theGreatest


def criticScoreRound(creditscore):
    if creditscore >= 80: creditscore = 1
    elif creditscore >= 60: creditscore = 2
    else: creditscore = 3
    return creditscore

def userScoreRounded(userScore):
    if userScore >= 8: userScore = 1
    elif userScore >= 6: userScore = 2
    else: userScore = 3
    return userScore



if __name__ == '__main__':
    dataset = GameDataCleaning.get_data()

    dataset = dataset.dropna(axis=0, how='any')
    dataset = dataset[dataset.RatingCode != -1]

    dataset['continent_greatest_sales'] = dataset.apply(lambda x:greatest(x['NA_Sales'],x['EU_Sales'],x['JP_Sales']),axis=1)

    dataset.to_csv("theGames",sep=",",encoding='utf-8',index= False)

    print("This is the end")