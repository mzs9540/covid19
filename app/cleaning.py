import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('from_april.csv')
df1 = df[df['Country'].isin(['US', 'China', 'Russia', 'Spain', 'Iran', 
                            'France', 'Italy', 'Germany',
                            'Turkey', 'Ukraine', 'United Kingdom', 'India'])]
china = df1[df1['Country'] == 'China'].drop('Country', axis=1)
china.to_csv('china.csv', index=False)

us = df1[df1['Country'] == 'US'].drop('Country', axis=1)
russia = df1[df1['Country'] == 'Russia'].drop('Country', axis=1)
spain = df1[df1['Country'] == 'Spain'].drop('Country', axis=1)
iran = df1[df1['Country'] == 'Iran'].drop('Country', axis=1)
france = df1[df1['Country'] == 'France'].drop('Country', axis=1)
italy = df1[df1['Country'] == 'Italy'].drop('Country', axis=1)
germany = df1[df1['Country'] == 'Germany'].drop('Country', axis=1)
turkey = df1[df1['Country'] == 'Turkey'].drop('Country', axis=1)
ukraine = df1[df1['Country'] == 'Ukraine'].drop('Country', axis=1)
uk = df1[df1['Country'] == 'United Kingdom'].drop('Country', axis=1)
india = df1[df1['Country'] == 'India'].drop('Country', axis=1)

us.to_csv('us.csv', index=False)
russia.to_csv('russia.csv', index=False)
spain.to_csv('spain.csv', index=False)
iran.to_csv('iran.csv', index=False)
france.to_csv('france.csv', index=False)
italy.to_csv('italy.csv', index=False)
germany.to_csv('germany.csv', index=False)
turkey.to_csv('turkey.csv', index=False)
ukraine.to_csv('ukraine.csv', index=False)
uk.to_csv('uk.csv', index=False)
india.to_csv('india.csv', index=False)