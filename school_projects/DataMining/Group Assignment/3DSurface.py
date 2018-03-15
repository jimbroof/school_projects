import plotly.graph_objs as go
from GameDataCleaning import GameDataCleaning
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected= False)

alldata = GameDataCleaning.get_data
newdata = alldata[['EU_Sales','NA_Sales','JP_Sales','Critic_Score','Critic_Count']]

data = [
    go.Surface(
        z=newdata.as_matrix(),
        hoverinfo = 'all'
    )
]
layout = go.Layout(
    title='Test surface',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
plot(fig, filename='3d surface test')
