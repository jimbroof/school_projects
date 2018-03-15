# Options
should_recompute = False
use_clean_data = True
unique_games_only = False
should_remove_outliers = False

properties_to_use = ['Critic_Score', 'User_Score', 'Year_of_Release']
property_to_predict = 'Has_Great_Sales'
test_size = 0.33
k_nearest_neighbors = 5

random_state = 42 # Random seed for generating the test size

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from GameDataCleaning import GameDataCleaning

dataset = GameDataCleaning.get_data(should_recompute, use_clean_data, unique_games_only, should_remove_outliers)

# create design matrix X and target vector y
X = np.array(dataset[properties_to_use].copy())
y = np.array(dataset[property_to_predict].copy())
print(len(X))
print(len(y))

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,random_state=random_state)

knn = KNeighborsClassifier(n_neighbors=k_nearest_neighbors)

# fitting the model
knn.fit(X_train, y_train)

# predict the response
pred = knn.predict(X_test)

# evaluate accuracy
print (accuracy_score(y_test, pred))