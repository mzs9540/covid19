import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

df  = pd.read_csv('full_data.csv')
df = df[(df.T !=0).any()]




