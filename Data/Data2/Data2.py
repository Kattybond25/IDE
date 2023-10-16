import pandas as pd
dates= pd.read_csv('Data\Data2\dates.csv', sep=',')
movies=pd.read_csv('Data\Data2\movies.csv', sep=',')
rating1=pd.read_csv('Data\Data2\ratings1.csv', sep=',')
rating2=pd.read_csv('Data\Data2\ratings2.csv', sep=',')
print(movies.head())
#unique_movies=movies['title'].nunique()

