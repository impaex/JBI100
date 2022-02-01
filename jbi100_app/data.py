import pandas as pd
import os


def get_data():
    # Read data
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../dataset/cleaned_data.csv'))
    df['date'] = pd.to_datetime(df['date'])
    df['hour'] = df.apply(lambda row: row['date'].hour, axis=1)
    #df['day_of_year'] = df.apply(lambda row: row['date'].timetuple().tm_yday, axis=1)
    df1 = df[df["accident_year"] == 2020]
    return df1
