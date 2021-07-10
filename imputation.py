# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:20:17 2021

@author: Ugurhan Uzkal
"""

import pandas as pd
import numpy as np

df = pd.read_csv('country_vaccination_stats.csv')

filtered_df = df[['country', 'daily_vaccinations']]

country_df = filtered_df[['country']]

arr_country = np.unique(country_df.values)
        
for country in arr_country:
    temp_df = filtered_df[filtered_df['country']==country]
    tdf = temp_df.min()
    if np.isnan(tdf['daily_vaccinations']):
        df_min = temp_df.fillna(0)
    else:
        df_min = temp_df.fillna(tdf)
        
    df.update(df_min)

df_int = df.convert_dtypes(convert_integer=True)

df.update(df_int)
    
df.to_csv('country_vaccination_stats_imputation.csv', index=False)