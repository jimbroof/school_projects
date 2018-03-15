# -*- coding: utf-8 -*-
"""
Created on Tue May  2 01:24:16 2017

@author: Lisa Denzer
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.plotly as py
import plotly.graph_objs as go

# Importing the dataset
dataset = pd.read_csv('C:/Users/Lisa Denzer/Google Drive/IT University of Copenhagen/3rd Sem 2017/Data Mining/Group Project/database_homocide.csv')
df = pd.DataFrame(dataset, columns = ['State', 'Year', 'CrimeType', 'VictimSex', 'VictimAge', 'VictimRace', 'VictimEthnicity', 'PerpetratorSex'])

dataset.describe()
dataset.count()

a = pd.Series(dataset.Year)
a.hist()

#change the type of the column
df.VictimSex = pd.Categorical(df.VictimSex)
df.CrimeType = pd.Categorical(df.CrimeType)
df.PerpetratorSex = pd.Categorical(df.PerpetratorSex)
        
#capture the category codes
df['VictimSexCode'] = df.VictimSex.cat.codes
df['CrimeTypeCode'] = df.CrimeType.cat.codes 
df['PerpetratorSexCode'] = df.PerpetratorSex.cat.codes


#Number of non-null observations
df.count()

#change the type of the column
df.Name = pd.Categorical(df.Name)
df.Platform = pd.Categorical(df.Platform)
df.Genre = pd.Categorical(df.Genre)
df.Publisher = pd.Categorical(df.Publisher)
        
#capture the category codes
df['NameCode'] = df.Name.cat.codes
df['PlatformCode'] = df.Platform.cat.codes 
df['GenreCode'] = df.Genre.cat.codes
df['PublisherCode'] = df.Publisher.cat.codes

s = pd.Series(df.Critic_Score)
#The value_counts() Series method computes a histogram of a 1D array of values. 
ScoreCount = s.value_counts()
#creates a visual histogram
s.hist()

t = pd.Series(df.Year_of_Release)
yearCount = t.value_counts()
t.hist(bins = 40 + 1)

u = pd.Series(df.PlatformCode)
PlatformCount = u.value_counts()
u.hist()

"""Found out how to name the histogram and its axes:"""
plt.title('Histogram of Education')
plt.xlabel('Education Level')
plt.ylabel('Frequency')
