#This code will clean the dataset "movie_metadata.csv"


import pandas as pd



def clean():
	df = pd.read_csv("movie_metadata.csv")	#code to read the csv file as pandas dataframe variable df
	
	rem_list = ['color','num_critic_for_reviews','director_facebook_likes','actor_3_facebook_likes',
       'actor_1_facebook_likes','num_voted_users','cast_total_facebook_likes',
       'facenumber_in_poster','num_user_for_reviews','actor_2_facebook_likes',
       'movie_facebook_likes'] #list of coloumns that are going to be removed
		
	df = df.drop(rem_list,1) #removig the rem_list coloumns
	df = df.dropna() #removing coloumns that contains NaN values
	