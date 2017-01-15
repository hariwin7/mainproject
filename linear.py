#predicted with only director feature with  r-squared of 0.8898336276518769

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

#%matplotlib inline

df = pd.read_csv("mach_learn.csv")
df=df[df['title_year']>=1990]

feature = df.ix[:,['dir_profit','max_pro','no_of_movies','budget','imdb_score','title_year','total_gross','total_budg','duration']]

label= df['profit']
feat_train,feat_test,lab_train,lab_test = train_test_split(feature,label,random_state=1)
clf = linear_model.LinearRegression()
clf.fit(feat_train,lab_train)

print "coef:",clf.coef_
print "intercpet:",clf.intercept_
print "score:",clf.score(feat_test,lab_test)