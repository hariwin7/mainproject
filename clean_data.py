#This code will clean the dataset "movie_metadata.csv"


import pandas as pd



def clean():
	#code which cleans the dataset
	df = pd.read_csv("movie_metadata.csv")	#code to read the csv file as pandas dataframe variable df

	rem_list = ['color','num_critic_for_reviews','director_facebook_likes','actor_3_facebook_likes',
       'actor_1_facebook_likes','num_voted_users','cast_total_facebook_likes',
       'facenumber_in_poster','num_user_for_reviews','actor_2_facebook_likes',
       'movie_facebook_likes'] #list of coloumns that are going to be removed
		
	df = df.drop(rem_list,1) #removig the rem_list coloumns
	df = df.dropna() #removing coloumns that contains NaN values
	


 #code to compute all the required attributes for machine learning

	df['profit']=df.apply (lambda row: profit (row),axis=1) #creates a new column profit in df which has the profit of each movie
	#initialize the variables for director profit and gross
	count=[]
	tot_prof=[]
	avg_prof=[]
	top_prof=[]
	tot_gross=[]
	avg_gross=[]
	
	dir_name= df['director_name'].unique()#selecting the unique list of director name
	#looping to find director gross(total and average),director profit(total,average and top)	
	for name in dir_name:
	    x=df.ix[df['director_name']==name]#selecting the movies of each director
	    gross=x['gross'].sum()#finding sum of gross for  director's movies
	    prof=x['profit'].sum()#finding sum of profit for  director's movies
	    no_mov= (x['director_name'].count())#counting the number of movies of a director
	    count.append(no_mov)#appending the number of movies to count
	    tot_gross.append(gross)#appending to total_gross list the gross calculated above
	    tot_prof.append(prof)#appending to total_prof list the profit calculated above
	    avg_gross.append(gross/no_mov)#appending to avg_gross list the average gross 
	    avg_prof.append(prof/no_mov)#appending to avg_profit list the average profit
	    top_prof.append(x['profit'].max())#appending most profitable movie profit of a director

	    #create a new dataframe with calculated values
	dfdir = pd.DataFrame({"director_name":dir_name,"total_profit":tot_prof,"no_of_movies":count,"total_gross":tot_gross
		,"avg_profit":avg_prof,"avg_gross":avg_gross,"top_profit":top_prof})
	return dfdir

def profit(row): #function that  computes the profit of each movie
    return row['gross']-row['budget']

if __name__=='__main__':
	clean()
	