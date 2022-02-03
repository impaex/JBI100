import os
import pandas as pd

print("Starting the loading.")
data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'dataset/Visualization_final_2.csv'))
print("done loading")

# Drop all question marks where location is not available.
#data.drop(data[(data['longitude'] == '?') | (data['latitude'] == '?')].index, inplace=True)
# Drop all NaN values from location.
#data.dropna(subset=['longitude', 'latitude'], inplace=True)
# Drop the unnamed column
#data.drop('Unnamed: 0', axis=1, inplace=True)
# Save without index row
#data['longitude'] = pd.to_numeric(data['longitude'])
#data['latitude'] = pd.to_numeric(data['latitude'])
data['vehicle_type'].replace({'Car (including private hire cars) (1979-2004)': 'Car',
                              'Van / Goods 3.5 tonnes mgw or under': 'Van',
                              'Goods over 3.5t. and under 7.5t': 'Goods >3.5t and <7.5t',
                              'Goods 7.5 tonnes mgw and over': "Goods >7.5t",
                              'Motorcycle over 125cc (1999-2004)': 'Motorcycle 125-500cc',
                              'Bus or coach (17 or more pass seats)': 'Bus',
                              'Motorcycle 125cc and under': 'Motorcycle <=125cc',
                              'Taxi (excluding private hire cars) (1979-2004)': 'Taxi / Private Hired',
                              'Motorcycle 50cc and under': 'Motorcycle <= 50cc',
                              'Minibus (8 - 16 passenger seats)': 'Minibus',
                              'Other vehicle': 'Other',
                              'Agricultural vehicle': 'Agricultural vehicle',
                              'Ridden horse': 'Ridden horse',
                              'Motorcycle over 500cc': 'Motorcycle >500cc',
                              'Motorcycle over 125cc and up to 500cc': 'Motorcycle 125-500cc',
                              'Taxi/Private hire car': 'Taxi / Private Hired',
                              'Motorcycle - unknown cc': 'Motorcycle unknown cc',
                              'Mobility scooter': 'Mobility Scooter',
                              'Goods vehicle - unknown weight': 'Goods vehicle unknown weight',
                              'Electric motorcycle': 'Electric Motorcycle',
                              'Unknown vehicle type (self rep only)': 'Unknown vehicle type',
                              }, inplace=True)

data['weather_conditions'].replace({'Fine no high winds': 'Fine, no high winds',
                                    'Raining no high winds': 'Raining, no high winds',
                                    'Snowing no high winds': 'Snowing, no high winds',
                                    'Fine + high winds': 'Fine, high winds',
                                    'Raining + high winds': 'Raining, high winds',
                                    'Snowing + high winds': 'Snowing, high winds',
                                    'Fog or mist': 'Fog or mist',
                                    'Other': 'Other',
                                    'Unknown': 'Unknown'
                                    }, inplace=True)

data['road_type'].replace({'Roundabout': 'Roudabout',
                           'One way street': 'One way street',
                           'Dual carriageway': 'Dual carriageway',
                           'Single carriageway': 'Single carriageway',
                           'Slip road': 'Slip road',
                           'One way street/Slip road': 'One way street / Slip road',
                           'Unknown': 'Unknown',
                           }, inplace=True)

data['light_conditions'].replace({'Daylight': 'Daylight',
                           'Darkness - lights lit': 'Darkness - lights lit',
                           'Dual carriageway': 'Darkness - lights unlit',
                           'Single carriageway': 'Darkness - no lighting',
                           'Slip road': 'Darkness - lighting unknown'
                           }, inplace=True)

data.drop(data.index[data['light_conditions'] == 'Data missing or out of range'], inplace=True)
print('done cleaning')
data.to_csv('cleaned_data.csv', index=False)