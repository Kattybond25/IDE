import pandas as pd
melb_df_3= pd.read_csv('Data\melb_3\melb_data_fe.csv', sep=',')
#print(melb_df_3.head())
#print(melb_df_3.info())
#melb_df_3['Date']=pd.to_datetime(melb_df_3['Date'])
#melb_df_3['quarter']=melb_df_3['Date'] .dt.to_period('Q')
#quartals=melb_df_3['quarter'].value_counts()
#second_popular_quarter=quartals.index[1]
#print(second_popular_quarter)
#print(quartals)
#exclude_columns=['Date', 'Rooms', 'Bedroom', 'Bathroom','Car']
#columns_to_convert=[col for col in melb_df_3.columns if col not in exclude_columns and melb_df_3[col].nunique()<150]
#for col in columns_to_convert:
#    melb_df_3[col]=melb_df_3[col].astype('category')
#sum_of_category_columns=melb_df_3[columns_to_convert].value_counts()
#print(len(columns_to_convert))
#melb_df_3=melb_df_3.sort_values(by='AreaRatio', ascending=False).reset_index(drop=True)
#value_1558=melb_df_3.at[1558,'BuildingArea']
#print(value_1558)
filtered_melb_df_3=melb_df_3[(melb_df_3['Type']=='townhouse')& (melb_df_3['Rooms']>2)]
sorted_melb_df_3=filtered_melb_df_3.sort_values(by=['Rooms', 'MeanRoomsSquare'], ascending=[True,False]).reset_index()
print(filtered_melb_df_3)
print(sorted_melb_df_3.at [18, 'Price'])
#print(melb_df_3['Type'].value_counts())
average_price=melb_df_3.groupby('Rooms')['Price'].mean()
max_average_price_rooms=average_price.idxmax()
print(max_average_price_rooms)
std_deviation_by_region=melb_df_3.groupby('Regionname')['Lattitude'].std()
region_with_min_deviation=std_deviation_by_region.idxmin()
print(region_with_min_deviation)
melb_df_3['Date']=pd.to_datetime(melb_df_3['Date'])
start_date=pd.to_datetime('2017-05-01')
end_date=pd.to_datetime('2017-09-01')
filtered_df=melb_df_3[(melb_df_3['Date'] >=start_date)&(melb_df_3['Date']<=end_date)]
total_sales_by_seller=filtered_df.groupby('SellerG')['Price'].sum()
seller_with_min_revenue=total_sales_by_seller.idxmin()
print(seller_with_min_revenue)
pivot_table=melb_df_3.pivot_table(index='Type', columns='Rooms', values='BuildingArea', aggfunc='median')
max_buiding_area=pivot_table.stack().idxmax()
max_building_area_value=pivot_table.stack().max()
print(pivot_table)
print(max_buiding_area)
print(max_building_area_value)
pivot_table=melb_df_3.pivot_table(index='SellerG', columns='Type', values='Price', aggfunc='median')
max_median_price_seller=pivot_table['unit'].idxmax()
print(max_median_price_seller)








