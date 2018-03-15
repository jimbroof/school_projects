""" Generates clusters from a given .csv Uses 3 dimensional representation of attributes """
import plotly.plotly as plt
from GameDataCleaning import GameDataCleaning
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=False)

data = GameDataCleaning.get_data()

scatter = dict(
    mode = 'markers',
    name = 'Scatter',
    type = 'scatter3d',
    x = data['Publisher'],
    y = data['Year_of_Release'],
    z = data['Global_Sales'],
    marker = dict(
        size = 2,
        color = 'blue',
        colorscale='Portland'
    )
    # Pre-defined color scales -
    # 'pairs' | 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' |
    # 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
)

clusters = dict(
    delaunayaxis="y",

    name = 'Cluster',
    opacity = 0.5,
    type = 'mesh3d',
    x = data['Publisher'],
    y = data['Year_of_Release'],
    z = data['Global_Sales'],
)

layout = dict(
    title = 'Missing sales values',
    scene = dict(
        xaxis = dict(zeroline = False),
        yaxis = dict(zeroline = False),
        zaxis = dict(zeroline = False),
    )
)

fig = dict(
    data=[scatter],
    layout = layout)

plot(fig, filename='3d_cluster.html')
