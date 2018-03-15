should_recompute = True
use_clean_data = True
unique_games_only = False
should_remove_outliers = False

test_size = 0.3 #Size of the test
random_state = 42 #Random seed

#used to inititalise the nn
from keras.models import Sequential
#used to create the layers
from keras.layers import Dense, Dropout, Activation
from GameDataCleaning import GameDataCleaning
from sklearn.metrics import confusion_matrix
from keras import metrics
import numpy as np
import pandas as pd

'''NO TOUCHY FROM HERE!!!!'''
properties_to_use = ['Publisher_Type', 'Best_Sales_Region', 'Critic_Score_Bin', 'User_Score_Bin', 'Average_Score_Bin', 'Year_of_Release']
property_to_guess = ['Global_Sales_Bin']


# Importing the dataset
dataset = GameDataCleaning.get_data(should_recompute, use_clean_data, unique_games_only, should_remove_outliers)

dataset.isnull().sum()
dataset.info()
dataset = dataset[dataset['Publisher'].notnull()]

#year from float to int
X_start = dataset[properties_to_use]

X_start['Type_0'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 0 else False, axis=1)
X_start['Type_1'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 1 else False, axis=1)
X_start['Type_2'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 2 else False, axis=1)
X_start['Type_3'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 3 else False, axis=1)
X_start['Type_4'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 4 else False, axis=1)
X_start['Type_5'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 5 else False, axis=1)
X_start['Type_6'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 6 else False, axis=1)
X_start['Type_7'] = X_start.apply(lambda x : True if x['Publisher_Type'] == 7 else False, axis=1)

X_start['Best_Sales_0'] = X_start.apply(lambda x : True if x['Best_Sales_Region'] == 0 else False, axis=1)
X_start['Best_Sales_1'] = X_start.apply(lambda x : True if x['Best_Sales_Region'] == 1 else False, axis=1)
X_start['Best_Sales_2'] = X_start.apply(lambda x : True if x['Best_Sales_Region'] == 2 else False, axis=1)
X_start['Best_Sales_3'] = X_start.apply(lambda x : True if x['Best_Sales_Region'] == 3 else False, axis=1)

X_start['Critic_Score_0'] = X_start.apply(lambda x : True if x['Critic_Score_Bin'] == 0 else False, axis=1)
X_start['Critic_Score_1'] = X_start.apply(lambda x : True if x['Critic_Score_Bin'] == 1 else False, axis=1)
X_start['Critic_Score_2'] = X_start.apply(lambda x : True if x['Critic_Score_Bin'] == 2 else False, axis=1)
X_start['Critic_Score_3'] = X_start.apply(lambda x : True if x['Critic_Score_Bin'] == 3 else False, axis=1)
X_start['Critic_Score_4'] = X_start.apply(lambda x : True if x['Critic_Score_Bin'] == 4 else False, axis=1)

X_start['User_Score_0'] = X_start.apply(lambda x : True if x['User_Score_Bin'] == 0 else False, axis=1)
X_start['User_Score_1'] = X_start.apply(lambda x : True if x['User_Score_Bin'] == 1 else False, axis=1)
X_start['User_Score_2'] = X_start.apply(lambda x : True if x['User_Score_Bin'] == 2 else False, axis=1)
X_start['User_Score_3'] = X_start.apply(lambda x : True if x['User_Score_Bin'] == 3 else False, axis=1)
X_start['User_Score_4'] = X_start.apply(lambda x : True if x['User_Score_Bin'] == 4 else False, axis=1)

X_start['Average_Score_0'] = X_start.apply(lambda x : True if x['Average_Score_Bin'] == 0 else False, axis=1)
X_start['Average_Score_1'] = X_start.apply(lambda x : True if x['Average_Score_Bin'] == 1 else False, axis=1)
X_start['Average_Score_2'] = X_start.apply(lambda x : True if x['Average_Score_Bin'] == 2 else False, axis=1)
X_start['Average_Score_3'] = X_start.apply(lambda x : True if x['Average_Score_Bin'] == 3 else False, axis=1)
X_start['Average_Score_4'] = X_start.apply(lambda x : True if x['Average_Score_Bin'] == 4 else False, axis=1)

max = X_start['Year_of_Release'].max()
min = X_start['Year_of_Release'].min()
X_start['Year_of_Release'] = X_start.apply(lambda x : (x['Year_of_Release'] - min) / (max - min), axis=1)

X_start.pop('Publisher_Type')
X_start.pop('Best_Sales_Region')
X_start.pop('Average_Score_Bin')
X_start.pop('User_Score_Bin')
X_start.pop('Critic_Score_Bin')

Y_start = dataset[property_to_guess]
Y_start['Guess_0'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 0 else False, axis=1)
Y_start['Guess_1'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 1 else False, axis=1)
Y_start['Guess_2'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 2 else False, axis=1)
Y_start['Guess_3'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 3 else False, axis=1)
Y_start['Guess_4'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 4 else False, axis=1)
Y_start['Guess_5'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 5 else False, axis=1)
Y_start['Guess_6'] = Y_start.apply(lambda x : True if x['Global_Sales_Bin'] == 6 else False, axis=1)
Y_start.pop('Global_Sales_Bin')

X = X_start.values
y = Y_start.values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state)


#y_train = keras.utils.to_categorical(y_train, num_classes=7)
#y_test = keras.utils.to_categorical(y_test, num_classes=7)
'''NO TOUCHY ENDS HERE!!!!'''

# Part 2 - Now let's make the ANN!

# Initialising the ANN, defining as a sequence of layers
#creating an object, classifier
# first layer must have a defined input shape
model = Sequential()

# Adding the input layer and the first hidden layer
#Just your regular fully connected NN layer.
#output_dim = number of nodes in the hidden layer
#dense-function assigns a weight to each node
#relu = rectifier activation function
model.add(Dense(output_dim = 32, activation = 'relu', input_dim = len(X_start.columns)))

model.add(Activation('relu'))

model.add(Dropout(0.5))

# Adding the second hidden layer
#it knows what to expect, so we dont add the input-dim
model.add(Dense(output_dim = 16, activation = 'relu'))

model.add(Activation('relu'))


# Adding the output layer
#sigmoid function for output layer, probability for each observation
#output dimension 1 is only for binary outcomes 1/0 yes/no => what to do if we have several?
model.add(Dense(output_dim = 7, activation = 'sigmoid'))

# Compiling the ANN
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy', 'top_k_categorical_accuracy'])

# Fitting the ANN to the Training set
model.fit(X_train, y_train, batch_size = 32, nb_epoch = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = model.predict(X_test, batch_size=1)


prediction = pd.DataFrame(y_pred).idxmax(axis=1)
actual = pd.DataFrame(y_test).idxmax(axis=1)
# Making the Confusion Matrix
cm = confusion_matrix(prediction, actual)
print(cm)

# plot_model(model, to_file='model.png')