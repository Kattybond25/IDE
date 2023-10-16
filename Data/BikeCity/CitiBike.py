import pandas as pd
bike_data = pd.read_csv ("Data\BikeCity\citibike-tripdata (3).csv", sep=',')
bike_data_df=pd.DataFrame(bike_data)
#print(bike_data_df.head())
#starttime — время начала поездки (дата, время);
#stoptime — время окончания поездки (дата, время);
#start station id — идентификатор стартовой стоянки;
#start station name — название стартовой стоянки;
#start station latitude, start station longitude — географическая широта и долгота стартовой стоянки;
#end station id — идентификатор конечной стоянки;
#end station name — название конечной стоянки;
#end station latitude, end station longitude — географическая широта и долгота конечной стоянки;
#bikeid — идентификатор велосипеда;
#usertype — тип пользователя (Customer — клиент с подпиской на 24 часа или на три дня, Subscriber — подписчик с годовой арендой велосипеда);
#birth year — год рождения клиента;
#gender — пол клиента (0 — неизвестный, 1 — мужчина, 2 — женщина)
#empty_spaces=bike_data_df.isnull().sum()
#print(empty_spaces)
print(bike_data_df['starttime'].dtype)
print(bike_data_df['stoptime'].dtype)
print(bike_data_df['start station id'].mode())
print(bike_data_df['bikeid'].mode())
mods=bike_data_df['usertype'].mode()
if len(mods)>1:
    mod1=mods[0]
    mod2=mods[1]
    print(mod1)
    print(mod2)
else:
    mod3=mods[0]
    print(mod3)
all_in_usertype=bike_data_df['usertype'].count()
sum_subscriber=bike_data_df[bike_data_df['usertype'].str.contains('Subscriber')]['usertype'].count()
print(sum_subscriber/all_in_usertype)
print(bike_data_df['gender'].value_counts())
uniq_start_station_name=bike_data_df['start station name'].nunique()
uniq_end_station_name=bike_data_df['end station name'].nunique()
print(uniq_start_station_name)
print(uniq_end_station_name)
print(bike_data_df['birth year'].max())
print(bike_data_df['starttime'])
print(bike_data_df['start station name'].value_counts())
print(bike_data_df['end station name'].value_counts())
bike_data_df=bike_data_df.drop('start station id', axis=1)
bike_data_df=bike_data_df.drop('end station id', axis=1)
#print(bike_data_df.shape[1])
#bike_data_df.rename(columns={'birth year': 'age'}, inplace=True)
#print(bike_data_df['age'])
#bike_data_df['age']=2018-bike_data_df['birth year']
#print(bike_data_df['age'])
#bike_data_df.drop(columns=['birth year'], inplace=True)
#filtered_bike_data_df=(bike_data_df['age']>60)
#print(filtered_bike_data_df.value_counts())
#bike_data_df['stoptime']=pd.to_datetime(bike_data_df['stoptime'])
#bike_data_df['starttime']=pd.to_datetime(bike_data_df['starttime'])
#bike_data_df['trip duration']=(bike_data_df['stoptime']-bike_data_df['starttime']).dt.total_seconds()/60
#trip_duration=bike_data_df=bike_data_df.loc[3, 'trip duration']
#print(trip_duration)
#Weekend race
#print(bike_data_df['starttime'].head())
#bike_data_df['starttime']=pd.to_datetime(bike_data_df['starttime'], format='%Y-%m-%d %H:%M:%S.%f')
#bike_data_df['weekend']=(bike_data_df['starttime'].dt.weekday>=5).astype(int)
#sum_weekend_races=bike_data_df['weekend'].sum()
#print(sum_weekend_races)
# Time of day
bike_data_df['starttime']=pd.to_datetime(bike_data_df['starttime'], format='%Y-%m-%d %H:%M:%S.%f')
def find_time_of_date (hour):
    if 0<=hour<=6:
        return 'night'
    elif 6< hour<=12:
        return 'morning'
    elif 12<hour<=18:
        return 'day'
    else:
        return 'evening'
bike_data_df['time_of_day']=bike_data_df['starttime'].dt.hour.apply(find_time_of_date)
nights=bike_data_df[bike_data_df['time_of_day']=='night'].shape[0]
days=bike_data_df[bike_data_df['time_of_day']=='day'].shape[0]
result=days/nights
print(result)


