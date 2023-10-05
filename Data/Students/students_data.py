import pandas as pd
students_data=pd.read_csv('Data\Students\students_performance.csv', sep=',')
df=pd.DataFrame(students_data)
print(df)
#gender — пол;
#race/ethnicity — раса/этническая принадлежность;
#parental level of education — уровень образования родителей;
#lunch — какие обеды получал студент во время обучения (standard — платный, free/reduced — бесплатный);
#test preparation course — посещал ли студент курсы подготовки к экзаменам (none — не посещал, completed — посещал);
#math score, reading score, writing score — баллы по математике, чтению и письму по сто балльной шкале.
print(df.shape[0])
print(df.loc[155, 'writing score'])
print(df.isnull().sum())
print(df.describe(include=['object']))
print(df.select_dtypes(include=['object']).shape[1])
print(df.describe())
print(df.memory_usage(deep=True).sum()/1024)
import sys
print(sys.getsizeof(df)/1024)
print(df.info())
print(df['math score'].mean())
print(df['race/ethnicity'].mode(0))
mask1=df[df['test preparation course']=='completed']['reading score'].mean()
print(mask1)
print(sum(df['math score']==0))
mask2=df[df['lunch']=='free/reduced']['math score']
mask3=df[df['lunch']=='standard']['math score']
print(mask2.mean())
print(mask3.mean())
print(sum(df['parental level of education']=="bachelor's degree"))
print(df['parental level of education'].shape[0])
med_A=(df[df['race/ethnicity']=='group A']['writing score'])
print(med_A.median())
#ave_C=(df[df['race/ethnicity']=='group C']['writing score'])
#print(ave_C.mean())