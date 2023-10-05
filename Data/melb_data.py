import pandas as pd
melb_data = pd.read_csv('data/melb_data.csv', sep=',')
df=pd.DataFrame(melb_data)
#obj=df.iloc[3521] ['Landsize']
#obj2=df.loc[1690] ['Landsize']
#print((obj/obj2).round(0))
#print(melb_data.head())
#print(melb_data.tail(7))
#print( melb_data.shape)
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
#print(melb_data.info())
#print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])
#print(melb_data.describe(include=['object']))
print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])
#print(melb_data.describe(include=['object']))
print(melb_data['Regionname'].value_counts())
print(melb_data['Regionname'].value_counts(normalize=True))
print(melb_data['CouncilArea'].isnull().sum())
print(melb_data.astype)
integer_columns=melb_data.select_dtypes(include=['int'])
count_integer_columns=len(integer_columns.columns)
print(count_integer_columns)
print((melb_data['Price'].median())/(melb_data['Price'].mean()))
print(sum(melb_data['Distance'].between(6.1, 13)))
print(melb_data.shape)
print(melb_data['BuildingArea'].mean())
print(melb_data['Coordinates'][37:145])
print(melb_data['Regionname'].value_counts())
print(melb_data[melb_data.duplicated(subset='Coordinates', keep=False)])
print(melb_data['Suburb'])
print(((melb_data['Type'].value_counts().get('t',0)))/(len(melb_data['Type']))*100)
print(max(melb_data['Propertycount']))
print(melb_data['Distance']. std())
print((melb_data['BuildingArea'].mean())-(melb_data['BuildingArea'].median()))
print(melb_data['BuildingArea'].median())
import statistics
print(statistics.mode(melb_data))
print(statistics.mode(melb_data['Bedroom']))
#mask = melb_data['Price'] > 2000000
#print(mask)
#print(melb_data[mask].head())
#print(melb_data['Bathroom'].value_counts())
#print(melb_data['Bathroom'].isnull().sum())
#print(melb_data[(melb_data['SellerG'] == 'Nelson') and (melb_data['Price']>3000000)].shape[0])
#filt=melb_data[(melb_data['SellerG'] == 'Nelson') and (melb_data['Price']>3000000)]
#print(filt.shape[0])
#m1=melb_data[melb_data['Price']>3000000]
#m2=melb_data[melb_data['SellerG']=='Nelson']
#print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3000000)].shape[0])
#print(melb_data[melb_data['BuildingArea']==0]['Price'].min())
#filtered_data=melb_data[((melb_data['Price']<1000000) & (melb_data['Rooms']>5)) | (melb_data['YearBuilt']>2015)]
#average_price=filtered_data.loc[filtered_data['Price']<1000000, 'Price'].mean()
#print(average_price)
filtered=melb_data[((melb_data['Type']=='h')) & (melb_data['Price']<3000000)]
most_common=filtered['Regionname'].mode()[0]
print(most_common)









