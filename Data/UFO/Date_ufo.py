import pandas as pd
ufo_data = pd.read_csv("Data\\UFO\\master_data_ufo.csv", sep=',')
ufo_df=pd.DataFrame(ufo_data)
#print(ufo_df)
#"City" — город, где был замечен НЛО;
#"Colors Reported" — цвет объекта;
#"Shape Reported" — форма объекта;
#"State" — обозначение штата;
#"Time" — время, когда был замечен НЛО (данные отсортированы от старых наблюдений к новым)
#print(ufo_df['Time']. value_counts())
ufo_df['Date']=pd.to_datetime(ufo_df['Time'])
nevada_ufo_df=ufo_df[ufo_df['State']=='NV']
nevada_ufo_df=nevada_ufo_df.sort_values(by='Date')
time_diff=nevada_ufo_df['Date'].diff().dt.days.mean()
#average_interval_timedelta=time_diff.mean()
#average_interval_days=average_interval_timedelta.days
print(time_diff)
#interval_between_last_two=nevada_ufo_df['TimeDiff'].iloc[-1]
#last_two_dates=nevada_ufo_df['Time'].tail(2)
#interval_between_last_two=(last_two_dates.iloc[1]-last_two_dates.iloc[0]).days
#nevada_ufo_df['TimeDiff']=nevada_ufo_df['Time'].diff().dt.days
#average_interval=nevada_ufo_df['TimeDiff'].mean()
#average_interval_time=average_interval_timedelta.days
#print(interval_between_last_two)
#print(last_two_dates)