from GameDataCleaning import *
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout

init_notebook_mode(connected= True)

data = GameDataCleaning.get_data()


# linear regression plot
def critic_vs_user_score():

    g = sns.jointplot(
        x = 'Critic_Score',
        y = 'User_Score',
        data = data,
        kind = 'hex',
        cmap= 'hot',
        label = 'correlation line',
        size=6)
    sns.regplot(data.Critic_Score, data.User_Score, ax=g.ax_joint, scatter=False, color='white')
    sns.plt.show()

# high correlation, you may wanna have similar ranges on the values
def critic_count_by_critic_score_corr():

    g = sns.jointplot(
        x = 'Critic_Count',
        y = 'Critic_Score',
        data = data,
        kind = 'hex',
        cmap= 'hot',
        size=6)
    sns.regplot(data.Critic_Count, data.Critic_Score, ax=g.ax_joint, scatter=False, color='white')
    sns.plt.show()

def generation_by_criticscore_corr():

    g = sns.jointplot(
        x = 'Generation',
        y = 'Critic_Score',
        data = data,
        kind = 'hex',
        cmap= 'hot',
        size=6)
    sns.regplot(data.Generation, data.Critic_Score, ax=g.ax_joint, scatter=False, color='white')
    sns.plt.show()

def number_of_games_by_year(data):
    name_count = data.groupby('Year_of_Release', axis=0).count().reset_index()[['Name','Year_of_Release']].sort_values(by='Name',ascending=True)

    layout = go.Layout(
        title='Releases by year',
        yaxis=dict(
            title='Years'),
        xaxis=dict(
            title='Count'),
        height=600, width=600
    )

    trace = go.Bar(
        x=name_count.Name,
        y=name_count.Year_of_Release,
        orientation='h'
    )

    figure = go.Figure(data=[trace], layout=layout)
    plot(figure)

def release_by_platform(data):
    platform_count = data.groupby('Platform', axis=0).count().reset_index()[['Platform', 'Name']].sort_values(by='Name',
                                                                                                            ascending=True)
    layout = go.Layout(
        title='Release by Platform',
        yaxis=dict(
            title='Platform'),
        xaxis=dict(
            title='Count'),
        height=600, width=600
    )

    trace = go.Bar(
        x=platform_count.Name,
        y=platform_count.Platform,
        orientation='h'
    )

    figure = go.Figure(data=[trace], layout=layout)
    plot(figure)

def critic_score_by_global_sales_corr(data):

    g = sns.jointplot(
        x = 'Critic_Score',
        y = 'Global_Sales',
        data = data,
        kind = 'hex',
        cmap= 'hot',
        size=6)
    sns.regplot(data.Critic_Score, data.Global_Sales, ax=g.ax_joint, scatter=False, color='white')
    sns.plt.show()

number_of_games_by_year(data)
