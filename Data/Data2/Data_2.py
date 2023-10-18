import pandas as pd
dates_file = pd.read_csv('Data\Data2\dates.csv', sep=',')
#print(dates_file.head())
#movies_file = pd.read_csv('Data\Data2\movies.csv', sep=',')
#print(movies_file.head())
ratings1 = pd.read_csv('Data\Data2\ratings1.csv', sep=',')
#print(rating1_file.head())
ratings2 = pd.read_csv('Data\Data2\ratings2.csv', sep=',')
#userId — уникальный идентификатор пользователя, который выставил оценку;
#movieId — уникальный идентификатор фильма;
#rating — рейтинг фильма.
#dates — таблица с датами выставления всех оценок
#date — дата и время выставления оценки фильму.
#movies — таблица с информацией о фильмах.
#unique_movies=movies_file['movieId'].nunique()
#print(unique_movies)
#dates_file['date']=pd.to_datetime(dates_file['date'])
#max_year=dates_file['date'].dt.year.value_counts().idxmax()
#print(max_year)
ratings = pd.concat([ratings1, ratings2])
print(ratings)

