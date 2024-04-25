import pandas as pd
import numpy as np

df = pd.DataFrame({
    'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
    'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']
})

df['FlightNumber'] = df['FlightNumber'].interpolate(method='linear', limit_direction='forward')
df['FlightNumber'] = df['FlightNumber'].astype(int)

temp_df = df['From_To'].str.split('_', expand=True)
temp_df.columns = ['From', 'To']
temp_df['From'] = temp_df['From'].str.capitalize()
temp_df['To'] = temp_df['To'].str.capitalize()

df.drop(columns=['From_To'], inplace=True)
df = pd.concat([df, temp_df], axis=1)

print(df)
