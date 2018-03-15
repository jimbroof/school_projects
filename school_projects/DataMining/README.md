# DataMining
Data mining


Name		

Platform									

Year_of_Release								

Genre										

Publisher

NA_Sales

EU_Sales

JP_Sales

Other_Sales

Global_Sales

Critic_Score

Critic_Count

User_Score

User_Count

Developer

Rating										ESRB Rating (age restrictions)

Name_Code									Categorized version of the name attribute

Platform_Code								Same, but of platform

Genre_Code									Categorized genre

Publisher_Code								Categorized Publisher

Developer_Code								Categorized Developer

Rating_Code									Categorized ESRB Rating

Generation									Generation of the platform

Has_Great_Sales								Boolean, True if the sales are above X

Best_Sales_Region							Region that had the best sales (NA, EU, Japan, or Other)

Has_Great_Critic_Score						Boolean, True if the critic score is above X

Has_Great_User_Score						Boolean, True if the user score is above X

Average_Score								Average score of the game from both critics and users - (Critic_Score * Critic_Count) + (User_Score * User_Count) / (Critic_Count + User_Count)

Has_Great_Average_Score						Boolean, True if the average score is above X

Total_Publisher_Games						The number of games this publisher has (including this game)

Average_Publisher_Sales						Average sales the publisher has (per game)

Total_Publisher_Sales						Total sales the publisher has (the more games, the better)

Average_Publisher_Score						Average score the publisher gets (mean of all Average_Score attributes of games released by this publisher)

Publisher_Type								"Categorized" version of the publisher. X is for big developers who release lots of games but have low sales per game, X is for big developers who have lots of sales, X is for small devs with low sales, X is for small devs with a lot of sales

Global_Sales_Bin							Global_sales distributed in bins. 1 is used if the sales are between 0 and 0.1. 2 -> [0.1, 0.5], 3 -> [0.5, 1], 4 -> [1, 2], 5 -> [2, infinity]

NA_Sales_Bin								Same but for NA_Sales

EU_Sales_Bin								Same but for EU_Sales

JP_Sales_Bin								Same but for JP_Sales

Other_Sales_Bin								Same but for Other_Sales

Critic_Score_Bin							Critic_Score 

User_Score_Bin

Average_Score_Bin

Year_of_Release_Normalized

NA_Sales_Normalized

EU_Sales_Normalized

JP_Sales_Normalized

Other_Sales_Normalized

Global_Sales_Normalized

Critic_Count_Normalized

Critic_Score_Normalized

User_Score_Normalized

User_Count_Normalized

Generation_Normalized

Total_Publisher_Games_Normalized

Average_Publisher_Sales_Normalized

Total_Publisher_Sales_Normalized

Average_Score_Normalized

Average_Publisher_Score_Normalized

Best_Sales_Region_Code

