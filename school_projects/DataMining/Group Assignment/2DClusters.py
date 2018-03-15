""" Generates clusters from a given .csv Uses 3 dimensional representation of attributes """
import plotly.plotly as plt
from GameDataCleaning import GameDataCleaning
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import pandas as pd

init_notebook_mode(connected= False)

# Load te CSV file and clean it
data = GameDataCleaning.get_data()

# Calculate the "total sales" of a game, no matter how many platforms it was released on
# Ex. GTA V will have 56.6 written on every platform
data['Series_Sales'] = data.groupby(['Name', 'Publisher'])['Global_Sales'].transform('sum')

# Remove duplicate entries of games
# Ex. GTA V will not appear only once
newData = data.drop_duplicates('Name', keep='first')

# Group by publisher and count the number of games a publisher has released
newData['Count'] = newData.groupby('Publisher')['Name'].transform('count')

# Group by publisher and calculate the mean sales of all of their games
newData['Mean'] = newData.groupby('Publisher')['Series_Sales'].transform('mean')

# Create a scatter plot that has the mean sales on the X axis and the number of games on the Y axis
trace = go.Scatter(
    x = newData['Mean'],
    y = newData['Count'],
    mode = 'markers',
    text = newData['Publisher']
)

# Create the graph and show it in a browser
plot([trace], filename='basic-scatter')
