#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
import pandas as pd


football = pd.read_csv('football.csv')
football['goal_diff']=football['Goals']-football['Goals Allowed']
goalDiffMin = football.loc[football['goal_diff'].idxmin()]
print(goalDiffMin[0])



