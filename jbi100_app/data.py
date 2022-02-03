import pandas as pd
import os
import numpy as np
import random


def get_data():
    # We get a sample of 100k items.
    # n = amount of entries total excluding header
    n = sum(1 for line in open(os.path.join(os.path.dirname(__file__), '../dataset/Visualization_full_zonder_text.csv'))) - 1
    # s is sample size
    s = 100000
    skip = sorted(random.sample(range(1, n+1), n-s))
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../dataset/Visualization_full_zonder_text.csv'), skiprows=skip)
    df['date'] = pd.to_datetime(df['date'])

    # drop the nan values in vehicle_type
    df1 = df[df['vehicle_type'].notna()]

    df1['vehicle_type'] = df1['vehicle_type'].astype(int)

    df1['hour'] = df1.apply(lambda row: row['date'].hour, axis=1)
    #df['day_of_year'] = df.apply(lambda row: row['date'].timetuple().tm_yday, axis=1)
    return df1
