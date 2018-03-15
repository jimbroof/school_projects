should_recompute = False
use_clean_data = True
unique_games_only = True
should_remove_outliers = False

number_of_clusters = 7
init_type = 'k-means++' #k-means++ or random #those are the options
cluster_run_times = 20 #How many times to run the clustering
max_iterations = 300 #How many iterations each clustering run should do (max)
random_state = 42 #Random seed used to initialize the centers
algorithm_to_use = 'auto' #auto, full, elkan #those are the options
verbose = 1 #Verbosity mode

# MUST BE 3 AND NORMALIZED!
properties_to_cluster = ['Total_Publisher_Games', 'Average_Publisher_Sales_Log', 'Average_Publisher_Score_Normalized']
# MUST BE SAME 3 PROPERTIES, NOT NORMALIZED VERSIONS!
properties_to_show = ['Total_Publisher_Games', 'Average_Publisher_Sales_Log', 'Average_Publisher_Score']
# Must have the same size as the number of clusters

import matplotlib.pyplot as plt
import numpy as np
from GameDataCleaning import GameDataCleaning
import plotly.graph_objs as go
from plotly.offline import plot
from sklearn.cluster import KMeans
import sklearn.metrics as sm


# Get the cleaned data
dataset = GameDataCleaning.get_data(should_recompute, use_clean_data, unique_games_only, should_remove_outliers)

dataset = dataset.drop_duplicates('Publisher', keep='first').copy()
dataset['Total_Publisher_Games'] = dataset.apply(lambda x : np.log2(x['Total_Publisher_Games']), axis=1)
dataset['Average_Publisher_Sales_Log'] = dataset.apply(lambda x : (np.log2(x['Average_Publisher_Sales'])), axis=1)

# Get the attributes we want to use to cluster with
trim_dataframe = dataset[properties_to_cluster].copy()
min = trim_dataframe['Total_Publisher_Games'].min()
max = trim_dataframe['Total_Publisher_Games'].max()
trim_dataframe['Total_Publisher_Games'] = trim_dataframe.apply(lambda x : (x['Total_Publisher_Games'] - min) / (max - min), axis=1)
min_1 = trim_dataframe['Average_Publisher_Sales_Log'].min()
max_1 = trim_dataframe['Average_Publisher_Sales_Log'].max()
trim_dataframe['Average_Publisher_Sales_Log'] = trim_dataframe.apply(lambda x : (x['Average_Publisher_Sales_Log'] - min_1) / (max_1 - min_1), axis=1)


# Convert to a matrix
cluster_data = trim_dataframe.as_matrix()

# Run KMeans
kmeans = KMeans(n_clusters=number_of_clusters, init=init_type, n_init=cluster_run_times, max_iter=max_iterations, random_state=random_state, verbose=verbose, copy_x=True, algorithm=algorithm_to_use)
kmeans.fit(cluster_data)

# Initialize a figure
plt.figure(figsize=(10,10))

colors = ['green', '#6f6f6f', 'red', 'blue', 'purple', '#FF530D', 'yellow', 'teal', 'black']
colormap = np.array(colors)

# Make a figure of the publishers based on the attribute we generated
publisher_types = dataset['Publisher_Type']

trace = go.Scatter3d(
    x = dataset[properties_to_show[0]],
    y = dataset[properties_to_show[1]],
    z = dataset[properties_to_show[2]],
    #z = cluster_data[:, 2],
    mode = 'markers',
    marker = dict(
        color = colormap[publisher_types]
    ),
    text = dataset['Publisher']
)
plot([trace], filename='clusters.html')

# Make a figure of the publishers based on the clusters
predY = np.choose(kmeans.labels_, [0, 1, 2, 3, 4, 5, 6]).astype(np.int64)
trace = go.Scatter3d(
    x = dataset[properties_to_show[0]],
    y = dataset[properties_to_show[1]],
    z = dataset[properties_to_show[2]],
    mode = 'markers',
    marker = dict(
        color = colormap[predY]
    ),
    text = dataset['Publisher']
)
    
centroids = kmeans.cluster_centers_
for center in centroids:
    center[0] = (center[0] * (max - min)) + min # the x
    center[1] = (center[1] * (max_1 - min_1)) + min_1  #center[1] * dataset[properties_to_show[1]].max() # the y
    center[2] = center[2] * dataset[properties_to_show[2]].max() # the z
    
centroidTrace = go.Scatter3d(
    x = centroids[:, 0], 
    y = centroids[:, 1], 
    z = centroids[:, 2],
    marker = dict(
        size = 10,
        color = 'rgb(255, 255, 255)',
        symbol='x',
        line = dict(
            width = 2,
        )
    )
)

data = [trace, centroidTrace]
layout = go.Layout(showlegend=False)
fig = go.Figure(data=data, layout=layout)
# Create the graph and show it in a browser
plot(fig, filename='k-means-results.html')

print(sm.accuracy_score(publisher_types, predY))
print(sm.confusion_matrix(publisher_types, predY))


import matplotlib.pyplot as plt
import numpy as np
from GameDataCleaning import GameDataCleaning
import plotly.graph_objs as go
from plotly.offline import plot
from sklearn.cluster import KMeans
import sklearn.metrics as sm