import pandas as pd
import os


def get_data():
    # Read data
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../dataset/cleaned_data.csv'))
    df1 = df[df["accident_year"] == 2020]
    return df1
