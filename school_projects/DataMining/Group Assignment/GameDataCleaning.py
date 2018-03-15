#File location
#Lisa
#Joachim
#file_loc = 'C:/DataGroupMining/DataMining/Group Assignment/theGames.csv'
#Vlad
#file_loc = 'C:/Users/Vlad/Documents/Repositories/DataMining/data/CSVs GroupAssignment/Games.csv'
#Ivan
file_loc = 'C:/Users/ivanm/Documents/GitHub/DataMining/data/CSVs GroupAssignment/Games.csv'

# Properties
great_game_requirement = 80 # Used for boolean
great_sales_requirement = 1.5
big_company_num_games = 100
big_company_average_sales = 1.5
big_company_average_score = 60
# Bins
sales_bins = [0, 0.05, 0.1, 0.2, 0.4, 0.7, 1.25, 100]
sales_labels = [0, 1, 2, 3, 4, 5, 6]
score_bins = [0, 35, 50, 65, 85, 100]
score_labels = [0, 1, 2, 3, 4]

import pandas as pd
import numpy as np
import seaborn as sns
import os.path
from scipy import stats

""" The file loads data from a CSV file, cleans it,
    normalizes it, and creates new properties.
    The data is then passed to the algorithm calling the
    get_data function
"""
class GameDataCleaning:        
    def get_data(should_recompute, should_clean, should_cut, should_remove_outliers):
        """ Executes everything required to load and clean the data """
        
        if (not should_recompute and should_clean):
            if (should_cut and os.path.isfile('cleaned_data_cut.csv')):
                dataset = pd.read_csv('cleaned_data_cut.csv')
                dataset = GameDataCleaning.generate_categories(dataset)
                if (should_remove_outliers):
                    dataset = GameDataCleaning.remove_outliers(dataset)
                dataset['Best_Sales_Region'] = dataset['Best_Sales_Region'].astype('category')
                dataset['Best_Sales_Region_Code'] = dataset.Name.cat.codes
                return dataset
            elif (os.path.isfile('cleaned_data_uncut.csv')):
                dataset = pd.read_csv('cleaned_data_uncut.csv')
                dataset = GameDataCleaning.generate_categories(dataset)
                if (should_remove_outliers):
                    dataset = GameDataCleaning.remove_outliers(dataset)
                dataset['Best_Sales_Region'] = dataset['Best_Sales_Region'].astype('category')
                dataset['Best_Sales_Region_Code'] = dataset.Name.cat.codes
                return dataset
        elif(not should_recompute):
            if (should_cut and os.path.isfile('uncleaned_data_cut.csv')):
                dataset = pd.read_csv('uncleaned_data_cut.csv')
                dataset = GameDataCleaning.generate_categories(dataset)
                if (should_remove_outliers):
                    dataset = GameDataCleaning.remove_outliers(dataset)
                dataset['Best_Sales_Region'] = dataset['Best_Sales_Region'].astype('category')
                dataset['Best_Sales_Region_Code'] = dataset.Name.cat.codes
                return dataset
            elif (os.path.isfile('uncleaned_data_uncut.csv')):
                dataset = pd.read_csv('uncleaned_data_uncut.csv')
                dataset = GameDataCleaning.generate_categories(dataset)
                if (should_remove_outliers):
                    dataset = GameDataCleaning.remove_outliers(dataset)
                dataset['Best_Sales_Region'] = dataset['Best_Sales_Region'].astype('category')
                dataset['Best_Sales_Region_Code'] = dataset.Name.cat.codes

                return dataset

        # Read the CSV file
        dataset = pd.read_csv(file_loc)
		
        # Print stats
        print('Stats before cleaning:')
        GameDataCleaning.print_stats(dataset)
        GameDataCleaning.print_correlation(dataset)
        
        if (should_remove_outliers):
            dataset = GameDataCleaning.remove_outliers(dataset)
        
        # Generate categorical attributes
        #dataset = GameDataCleaning.generate_categories(dataset)
        
        # Normalize the data
        dataset = GameDataCleaning.normalize_data_start(dataset)
        
        # Create new properties out of the available data
        dataset = GameDataCleaning.create_new_properties_start(dataset)
        
        # Clean the data
        if (should_clean):
            dataset = GameDataCleaning.clean_data(dataset)
        
        # Remove nulls
        dataset = GameDataCleaning.remove_nulls(dataset)
        
        dataset = GameDataCleaning.create_new_properties_end(dataset, should_cut)
        
        dataset = GameDataCleaning.normalize_data_end(dataset)
        
        # Re-categorize
        dataset = GameDataCleaning.generate_categories(dataset)
        dataset['Best_Sales_Region'] = dataset['Best_Sales_Region'].astype('category')
        dataset['Best_Sales_Region_Code'] = dataset.Name.cat.codes

        # Print stats
        print('Stats post cleaning:')
        GameDataCleaning.print_stats(dataset)
        GameDataCleaning.print_correlation(dataset)
        
        if (should_clean):
            if (should_cut):
                dataset.to_csv("cleaned_data_cut.csv",sep=",",encoding='utf-8',index= False)
            else:
                dataset.to_csv("cleaned_data_uncut.csv",sep=",",encoding='utf-8',index= False)
        else:
            if (should_cut):
                dataset.to_csv("uncleaned_data_cut.csv",sep=",",encoding='utf-8',index= False)
            else:
                dataset.to_csv("uncleaned_data_uncut.csv",sep=",",encoding='utf-8',index= False)
            
        return dataset
    
    def remove_outliers(dataset):
        dataset = dataset[(np.abs(stats.zscore(dataset['Global_Sales'])) < 3)]
        dataset = dataset[(np.abs(stats.zscore(dataset['NA_Sales'])) < 3)]
        dataset = dataset[(np.abs(stats.zscore(dataset['EU_Sales'])) < 3)]
        dataset = dataset[(np.abs(stats.zscore(dataset['JP_Sales'])) < 3)]
        dataset = dataset[(np.abs(stats.zscore(dataset['Other_Sales'])) < 3)]

        return dataset
    

    """ Cleans the data from missing values and inconsistencies """
    def clean_data(dataset):        
        # Fill in the null values in year of release with the median of the specific game's generation
        dataset['Year_of_Release'] = dataset[['Year_of_Release']].fillna(dataset.groupby('Platform').transform('median'))
        
        dataset = dataset[dataset.Year_of_Release >= 2006]
        
        # Fill in developer code with the median developer in regards to generation, game name, and publisher        
        #dataset['Developer_Code'] = dataset['Developer_Code'].replace('-1', np.nan)
        #dataset['Developer_Code'] = dataset[['Developer_Code']].fillna(dataset.groupby(['Platform', 'Name'])['Developer_Code'].transform('median'))
        #dataset['Developer_Code'] = dataset[['Developer_Code']].fillna(dataset.groupby(['Platform', 'Publisher_Code'])['Developer_Code'].transform('median'))
        #dataset['Developer_Code'] = dataset[['Developer_Code']].fillna(dataset.groupby('Platform')['Developer_Code'].transform('median'))        
        
        # Fill in the developer attribute by reflecting the categorical representation (and convert back from float to int)
        #dataset['Developer_Code'] = dataset['Developer_Code'].replace(np.nan, -1)
        #dataset['Developer_Code'] = dataset['Developer_Code'].astype('int')
        #dataset = dataset.assign(Developer = dataset.Developer_Code.apply(lambda x : dataset.Developer.cat.categories[x] if x > -1 else None))
        
        # Fill in rest with publisher
        #dataset['Developer'] = dataset['Developer'].astype('str')
        #dataset['Publisher'] = dataset['Publisher'].astype('str')
        #dataset['Developer'] = dataset.apply(lambda x : x['Developer'].replace('nan', x['Publisher']), axis=1)

        # Fill in missing scores based on the developer's track record in the same time period
        dataset['Critic_Score'] = dataset[['Critic_Score']].fillna(dataset.groupby(['Genre', 'Publisher']).transform('mean'))
        dataset['Critic_Score'] = dataset[['Critic_Score']].fillna(dataset.groupby(['Platform', 'Publisher']).transform('mean'))
        dataset['Critic_Score'] = dataset[['Critic_Score']].fillna(dataset.groupby('Genre').transform('mean'))
        dataset['Critic_Score'] = dataset[['Critic_Score']].fillna(dataset.groupby('Platform').transform('mean'))
        dataset['Critic_Count'] = dataset[['Critic_Count']].fillna(dataset.groupby(['Genre', 'Publisher']).transform('mean'))
        dataset['Critic_Count'] = dataset[['Critic_Count']].fillna(dataset.groupby(['Platform', 'Publisher']).transform('mean'))
        dataset['Critic_Count'] = dataset[['Critic_Count']].fillna(dataset.groupby('Genre').transform('mean'))
        dataset['Critic_Count'] = dataset[['Critic_Count']].fillna(dataset.groupby('Platform').transform('mean'))
        dataset['User_Score'] = dataset[['User_Score']].fillna(dataset.groupby(['Genre', 'Publisher']).transform('mean'))
        dataset['User_Score'] = dataset[['User_Score']].fillna(dataset.groupby(['Platform', 'Publisher']).transform('mean'))
        dataset['User_Score'] = dataset[['User_Score']].fillna(dataset.groupby('Genre').transform('mean'))
        dataset['User_Score'] = dataset[['User_Score']].fillna(dataset.groupby('Platform').transform('mean'))
        dataset['User_Count'] = dataset[['User_Count']].fillna(dataset.groupby(['Genre', 'Publisher']).transform('mean'))
        dataset['User_Count'] = dataset[['User_Count']].fillna(dataset.groupby(['Platform', 'Publisher']).transform('mean'))
        dataset['User_Count'] = dataset[['User_Count']].fillna(dataset.groupby('Genre').transform('mean'))
        dataset['User_Count'] = dataset[['User_Count']].fillna(dataset.groupby('Platform').transform('mean'))
        
        #dataset['Rating_Code'] = dataset['Rating_Code'].replace('-1', np.nan)
        #dataset['Rating_Code'] = dataset[['Rating_Code']].fillna(dataset.groupby('Genre')['Rating_Code'].transform('median'))
        #dataset['Rating_Code'] = dataset[['Rating_Code']].fillna(dataset.groupby('Platform')['Rating_Code'].transform('median'))
        #dataset['Rating_Code'] = dataset[['Rating_Code']].fillna(dataset.groupby('Developer')['Rating_Code'].transform('median'))
        #dataset['Rating_Code'] = dataset[['Rating_Code']].fillna(dataset.groupby('Publisher')['Rating_Code'].transform('median'))
        #dataset['Rating_Code'] = dataset[['Rating_Code']].fillna(dataset['Rating_Code'].median())
        #dataset['Rating_Code'] = dataset['Rating_Code'].replace(np.nan, '-1')
        
        #dataset['Rating_Code'] = dataset['Rating_Code'].astype('int')
        #dataset = dataset.assign(Rating = dataset.Rating_Code.apply(lambda x : dataset.Rating.cat.categories[x] if x > -1 else None))
		
        return dataset

        
    """ Normalize the data """
    def normalize_data_start(dataset):
        # normalizing should go here
        
        # Remove all "TBD" entries in the user score column with a 0
        dataset['User_Score'] = dataset['User_Score'].replace(to_replace=['tbd'], value=np.nan)
        
        # Convert the User_Score column to a float from a string, errors are replaced with a NaN (because of coerce)
        dataset['User_Score'] = dataset['User_Score'].astype('float')
        
        # Multiply every user score by 10 so it's between 0 and 100 (to unify with the critic score column)
        dataset = dataset.assign(User_Score = dataset.User_Score.apply(lambda x : x * 10))
        
        return dataset
        
    def normalize_data_end(dataset):
        
        # Convert some of the attributes to an integer
        dataset['Year_of_Release'] = dataset['Year_of_Release'].astype('int')
        
        #dataset['Critic_Score'] = dataset['Critic_Score'].astype('int')
        #dataset['User_Score'] = dataset['User_Score'].astype('int')
        #dataset['Critic_Count'] = dataset['Critic_Count'].astype('int')
        #dataset['User_Count'] = dataset['User_Count'].astype('int')
        
        # Create a normalized version of each nominal attribute
        dataset['Year_of_Release_Normalized'] = dataset.apply(lambda x : (x['Year_of_Release'] / dataset['Year_of_Release'].max()), axis=1)
        #dataset['NA_Sales_Normalized'] = dataset.apply(lambda x : (x['NA_Sales'] / dataset['NA_Sales'].max()), axis=1)
        #dataset['EU_Sales_Normalized'] = dataset.apply(lambda x : (x['EU_Sales'] / dataset['EU_Sales'].max()), axis=1)
        #dataset['JP_Sales_Normalized'] = dataset.apply(lambda x : (x['JP_Sales'] / dataset['JP_Sales'].max()), axis=1)
        #dataset['Other_Sales_Normalized'] = dataset.apply(lambda x : (x['Other_Sales'] / dataset['Other_Sales'].max()), axis=1)
        #dataset['Global_Sales_Normalized'] = dataset.apply(lambda x : (x['Global_Sales'] / dataset['Global_Sales'].max()), axis=1)
        #dataset['Critic_Score_Normalized'] = dataset.apply(lambda x : (x['Critic_Score'] / dataset['Critic_Score'].max()), axis=1)
        #dataset['Critic_Count_Normalized'] = dataset.apply(lambda x : (x['Critic_Count'] / dataset['Critic_Count'].max()), axis=1)
        #dataset['User_Score_Normalized'] = dataset.apply(lambda x : (x['User_Score'] / dataset['User_Score'].max()), axis=1)
        #dataset['User_Count_Normalized'] = dataset.apply(lambda x : (x['User_Count'] / dataset['User_Count'].max()), axis=1)
        #dataset['Generation_Normalized'] = dataset.apply(lambda x : (x['Generation'] / dataset['Generation'].max()), axis=1)
        dataset['Total_Publisher_Games_Normalized'] = dataset.apply(lambda x : (x['Total_Publisher_Games'] / dataset['Total_Publisher_Games'].max()), axis=1)
        dataset['Average_Publisher_Sales_Normalized'] = dataset.apply(lambda x : (x['Average_Publisher_Sales'] / dataset['Average_Publisher_Sales'].max()), axis=1)
        #dataset['Total_Publisher_Sales_Normalized'] = dataset.apply(lambda x : (x['Total_Publisher_Sales'] / dataset['Total_Publisher_Sales'].max()), axis=1)
        dataset['Average_Score_Normalized'] = dataset.apply(lambda x : (x['Average_Score'] / dataset['Average_Score'].max()), axis=1)
        dataset['Average_Publisher_Score_Normalized'] = dataset.apply(lambda x : (x['Average_Publisher_Score'] / dataset['Average_Publisher_Score'].max()), axis=1)
        
        return dataset

    """ Generates new properties which are a categorical reflection of the nominal attributes """
    def generate_categories(dataset):
        # Convert the following attributes from an object to a categorical
        dataset['Name'] = dataset['Name'].astype('category')
        dataset['Platform'] = dataset['Platform'].astype('category')
        dataset['Genre'] = dataset['Genre'].astype('category')
        dataset['Publisher'] = dataset['Publisher'].astype('category')
        dataset['Developer'] = dataset['Developer'].astype('category')
        dataset['Rating'] = dataset['Rating'].astype('category')
        
        # Store the categories in new properties
        dataset['Name_Code'] = dataset.Name.cat.codes
        dataset['Platform_Code'] = dataset.Platform.cat.codes
        dataset['Genre_Code'] = dataset.Genre.cat.codes
        dataset['Publisher_Code'] = dataset.Publisher.cat.codes
        dataset['Developer_Code'] = dataset.Developer.cat.codes
        dataset['Rating_Code'] = dataset.Rating.cat.codes
        
        return dataset
        
    """ Creates new attributes from the available data """
    def create_new_properties_start(dataset):
        # Define all platform generations. Used google to see which platform is which gen
        '''generations = {
                '2600' : 2,
                'NES' : 3,
                'GB' : 4,
                'SNES' : 4,
                'SCD' : 4,
                'NG' : 4,
                'TG16' : 4,
                'GEN' : 4,
                'GG' : 4,
                'SAT' : 5,
                'WS' : 5,
                '3DO' : 5,
                'N64' : 5,
                'PS' : 5,
                'PCFX' : 5,
                'GBA' : 6,
                'XB' : 6,
                'DC' : 6,
                'PS2' : 6,
                'GC' : 6,
                'Wii' : 7,
                'DS' : 7,
                'X360' : 7,
                'PS3' : 7,
                'PSP' : 7,
                'PS4' : 8,
                '3DS' : 8,
                'PSV' : 8,
                'XOne' : 8,
                'WiiU' : 8,
                'PC' : 9,
        }
        
        # Create a new attribute called "Generation", based on the platform generation
        dataset['Generation'] = dataset['Platform'].map(generations)'''
       
        # Create a new attribute (True if a game had a lot of sales, False otherwise)
        dataset['Has_Great_Sales'] = dataset.apply(lambda x : x['Global_Sales'] >= great_sales_requirement, axis=1)

        # Best selling region
        dataset['Best_Sales_Region'] = dataset.apply(lambda x : GameDataCleaning.greatest_sales_region(x), axis=1)
        
        return dataset
    
    def create_new_properties_end(dataset, should_cut):                    
        # Create a new property (True if game has a score of 80 or more, false otherwise)
        dataset['Has_Great_Critic_Score'] = dataset.apply(lambda x : x['Critic_Score'] >= great_game_requirement, axis=1)
        dataset['Has_Great_User_Score'] = dataset.apply(lambda x : x['User_Score'] >= great_game_requirement, axis=1)
        
        dataset['Average_Score'] = dataset.apply(lambda x : GameDataCleaning.calculate_score(x), axis=1)
        dataset['Has_Great_Average_Score'] = dataset.apply(lambda x : x['Average_Score'] >= great_game_requirement, axis=1)

        if (should_cut):
            # Create a new property that combines all sales of a game across a platform
            # Ex. GTA V was released on 5 platforms, so it has 5 entries. This sums the sales of all 5 entries
            series_sales = dataset.groupby(['Name', 'Publisher'])['Global_Sales'].transform('sum')
            dataset['Global_Sales'] = series_sales
            
            # Remove duplicate entries of games
            # Ex. GTA V will now appear only once
            dataset = dataset.drop_duplicates('Name', keep='first').copy()
            
        # Group by publisher and count the number of games a publisher has released
        dataset['Total_Publisher_Games'] = dataset.groupby('Publisher')['Name'].transform('count')
        
        # Group by publisher and calculate the mean sales of all of their games
        dataset['Average_Publisher_Sales'] = dataset.groupby('Publisher')['Global_Sales'].transform('mean')
        #dataset['Total_Publisher_Sales'] = dataset.groupby('Publisher')['Global_Sales'].transform('sum')        
        
        dataset['Average_Publisher_Score'] = dataset.groupby('Publisher')['Average_Score'].transform('mean')
                
        all_publishers = dataset.groupby('Publisher')
        dataset['Publisher_Type'] = dataset.apply(lambda x: GameDataCleaning.publisher_type(all_publishers, x['Publisher']),axis=1)

        dataset['Global_Sales_Bin'] = pd.cut(dataset['Global_Sales'], sales_bins, include_lowest=True, labels=sales_labels)
        #dataset['NA_Sales_Bin'] = pd.cut(dataset['NA_Sales'], sales_bins, include_lowest=True, labels=sales_labels)
        #dataset['EU_Sales_Bin'] = pd.cut(dataset['EU_Sales'], sales_bins, include_lowest=True, labels=sales_labels)
        #dataset['JP_Sales_Bin'] = pd.cut(dataset['JP_Sales'], sales_bins, include_lowest=True, labels=sales_labels)
        #dataset['Other_Sales_Bin'] = pd.cut(dataset['Other_Sales'], sales_bins, include_lowest=True, labels=sales_labels)
        dataset['Critic_Score_Bin'] = pd.cut(dataset['Critic_Score'], score_bins, include_lowest=True, labels=score_labels)
        dataset['User_Score_Bin'] = pd.cut(dataset['User_Score'], score_bins, include_lowest=True, labels=score_labels)
        dataset['Average_Score_Bin'] = pd.cut(dataset['Average_Score'], score_bins, include_lowest=True, labels=score_labels)

        return dataset
    
    def publisher_type(all_publishers, publisher):
        p_data = all_publishers.get_group(publisher)
        
        num_games = p_data['Total_Publisher_Games'].iloc[0]
        average_sales = p_data['Average_Publisher_Sales'].mean()
        #score = p_data['Average_Publisher_Score'].mean()
        
        if (num_games <= 2 and average_sales <= 0.09):
            return 0
        elif (num_games >= 40 and average_sales <= 0.3):
            return 2
        elif (num_games >= 40 and average_sales > 0.3):
            return 3
        elif (num_games > 3 and num_games <= 40 and average_sales >= 0.15 and average_sales < 1):
            return 4
        elif (num_games <= 4 and average_sales >= 0.09 and average_sales <= 0.3):
            return 5
        elif (num_games >= 3 and num_games <= 40 and average_sales < 0.2):
            return 6
        elif (num_games <= 40 and average_sales > 0.3):
            return 1
        else:
            print(str(num_games) + ' ' + str(average_sales))
        
    def calculate_score(game):
        total_critic = game['Critic_Score'] * game['Critic_Count']
        total_user = game['User_Score'] * game['User_Count']
        total = game['User_Count'] + game['Critic_Count']
        average = (total_critic + total_user) / total
        return average
    
    def greatest_sales_region(x):
        NA = x['NA_Sales']
        EU = x['EU_Sales']
        JP = x['JP_Sales']
        other = x['Other_Sales']
        
        if NA > EU and NA > JP and NA > other:
            theGreatest = 0
        elif EU > NA and EU > JP and EU > other:
            theGreatest = 1
        elif JP > NA and JP > EU and JP > other:
            theGreatest = 2
        else:
            theGreatest = 3
        
        return theGreatest
        
    def remove_nulls(dataset):
        # kills null years, names, user and critic score and count.
        # a bit overkill, but can be split up later
        #dataset = dataset[dataset.Name.notnull()]
        #dataset = dataset.dropna()
        dataset = dataset[dataset.Year_of_Release < 2017]
        dataset = dataset[dataset.Publisher != 'nan']
        dataset = dataset[dataset.Publisher.notnull()]

        return dataset
        
    def print_stats(dataset):
        print("Number of entries: {}".format(len(dataset)))
        
        missing = dataset.isnull().sum()
        print(missing)
        print('\n')
        
    def print_correlation(dataset):
        #print(dataset.corr())
        corr = dataset.corr()
        sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)