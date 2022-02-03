import pandas as pd
import os
import numpy as np
import random


def get_data():
    # We get a sample of 100k items.
    # n = amount of entries total excluding header
    n = sum(1 for line in open(os.path.join(os.path.dirname(__file__), '../dataset/cleaned_data.csv'))) - 1
    # s is sample size
    s = 100000
    skip = sorted(random.sample(range(1, n+1), n-s))
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../dataset/cleaned_data.csv'), skiprows=skip)
    df['date'] = pd.to_datetime(df['date'])

    # drop the nan values in vehicle_type
    df1 = df[df['vehicle_type'].notna()]

    df1['accident_year'] = df1.apply(lambda row: row['date'].year, axis=1)

    df1['hour'] = df1.apply(lambda row: row['date'].hour, axis=1)
    #df1['weekday'] = df1.apply(lambda row: row['date'].weekday(), axis=1)
    #df['day_of_year'] = df.apply(lambda row: row['date'].timetuple().tm_yday, axis=1)
    return df1
