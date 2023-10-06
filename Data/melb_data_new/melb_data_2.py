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


