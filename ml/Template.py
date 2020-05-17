import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df  = pd.read_csv('from_april.csv', parse_dates=['Date'])
df = df[(df.T !=0).any()]

india = df[df['Country/Region'] == 'India']
india = india.drop(['Country/Region', 'Province/State', 'Lat', 'Long'], axis=1)
india_confirmed = india.drop(['Recovered', 'Deaths'], axis=1)
india_deaths = india.drop(['Recovered', 'Confirmed'], axis=1)
india_recovered = india.drop(['Confirmed', 'Deaths'], axis=1)

india_confirmed.to_csv('india_confirmed.csv', index=False)

print(india.dtypes)



