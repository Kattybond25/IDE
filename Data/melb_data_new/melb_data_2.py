import pandas as pd
melb_data = pd.read_csv ("Data\melb_data_new\melb_data_ps.csv", sep=',')
melb_df=pd.DataFrame(melb_data)
print(melb_df.head())
#index — номер строки
#Suburb — наименование пригорода
#Address — адрес
#Rooms — количество комнат в помещении
#Type — тип здания (h — дом, коттедж, вилла, терраса; u — блочный, дуплексный дом; t — таунхаус)
#Price — цена помещения
#Method — метод продажи 
#SellerG — риэлторская компания
#Date — дата продажи (в формате день/месяц/год)
#Distance — расстояния до объекта от центра Мельбурна 
#Postcode — почтовый индекс
#Bedroom — количество спален
#Bathroom — количество ванных комнат
#Car — количество парковочных мест
#Landsize — площадь прилегающей территории
#BuildingArea — площадь здания
#YearBuilt — год постройки
#CouncilArea — региональное управление
#Lattitude — географическая широта
#Longitude — географическая долгота
#Regionname — наименование района Мельбурна
#Propertycount — количество объектов недвижимости в районе, выставленных на продажу
#Coordinates — широта и долгота, объединённые в кортеж
melb_df = melb_data.copy()
melb_df.head()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
melb_df.head()
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
print(total_rooms)
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms
print(melb_df['MeanRoomsSquare'])
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
print(melb_df['AreaRatio'])
melb_df['Date']=pd.to_datetime(melb_df['Date'],dayfirst=True)
melb_df['WeekdaySale']=melb_df['Date'].dt.day_name()
weekend_count=melb_df[(melb_df['WeekdaySale']=='Saturday')|(melb_df['WeekdaySale']=='Sunday')].shape[0]
print(weekend_count)
#Sales in Weekend
def get_weekend(weekday):
    if weekday in ['Saturday','Sunday']:
        return 1
    else:
        return 0
melb_df['Weekend']=melb_df['WeekdaySale'].apply(get_weekend)
averga_price_weekend=melb_df['Weekend']=melb_df[melb_df['Weekend']==1]['Price'].mean()
averga_price_weekend_rounded=round(averga_price_weekend)
print(averga_price_weekend_rounded)
#Change SellerG
most_popular_names=melb_df['SellerG'].value_counts()
popular_names=most_popular_names.head(49).index
#print(popular_names)
def replace_with_other(seller):
    return seller if seller in popular_names else 'other'
melb_df['SellerG'] = melb_df['SellerG'].apply(replace_with_other)
#Во сколько раз минимальная цена Нельсон больше others
nelson_data=melb_df[melb_df['SellerG']=='Nelson']
other_data=melb_df[melb_df['SellerG']=='other']
min_price_nelson=nelson_data['Price'].min()
min_price_other=other_data['Price'].min()
ratio=min_price_nelson/min_price_other
print(round(ratio,1))
#print(melb_df['SellerG'])
# КАТЕГОРИИ
melb_df.info()
suburb_names=melb_df['Suburb']. value_counts()
most_popular_names_suburb=suburb_names.head(119)
print(most_popular_names_suburb)
def replace_with_other_suburb(suburb):
    return suburb if suburb in most_popular_names_suburb else 'other_suburb'
melb_df_suburb_new = melb_df['Suburb'].apply(replace_with_other_suburb)
print(melb_df_suburb_new)
melb_df['Suburb']=melb_df['Suburb'].astype('category')
print (melb_df['Suburb'].dtypes)
melb_df.info()

    








    

