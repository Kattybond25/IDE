import pandas as pd
ufo_data = pd.read_csv ("Data\UFO\raw.githubusercontent.com_justmarkham_pandas-videos_master_data_ufo.csv", sep=',')
ufo_df=pd.DataFrame(ufo_data)
print(ufo_df.head())