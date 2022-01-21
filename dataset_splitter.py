import os
import pandas as pd

print("Starting the loading.")
data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'dataset/Visualization_full.csv'))
print("done loading")
print(data.head())
# Drop all question marks where location is not available.
data.drop(data[(data['longitude'] == '?') | (data['latitude'] == '?')].index, inplace=True)
# Drop all NaN values from location.
data.dropna(subset=['longitude', 'latitude'], inplace=True)
# Drop the unnamed column
data.drop('Unnamed: 0', axis=1, inplace=True)
# Save without index row
print('done cleaning')
data.to_csv('cleaned_data.csv', index=False)