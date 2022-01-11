import csv
import pandas as pd

accident_dataset = "venv/dataset/dft-road-casualty-statistics-accident-1979-2020.csv"
casualty_dataset = "venv/dataset/dft-road-casualty-statistics-casualty-1979-2020.csv"
vehicle_dataset = "venv/dataset/dft-road-casualty-statistics-vehicle-1979-2020.csv"

# Load a dataset in a pandas dataframe. We only import the first 50.000 rows.
df = pd.read_csv(casualty_dataset, nrows=50000)

# Print some statistics
# Assignment 1 exercise 2d
print(df.describe())

# See the NaN values for the columns
# This is assignment 1 exercise 2F.
pd.set_option('display.max_rows', 100)
print('These are the number of NaN values in the columns:')
print(df.isna().sum())
print('And their stats:')
print(df.isna().sum().describe())

print(' ')
# Create a transposed version of the table to get the NaN-values per row:
df_entries = df.transpose()

# See the NaN values for the rows
print('These are the number of NaN values in the columns:')
print(df_entries.isna().sum())
print('And their stats:')
print(df_entries.isna().sum().describe())


# Replace de dataset variable hier onder met 1 van de predefined datasets om andere sets te laten parsen.
# 'r' staat voor de read modus.
# Dit is assignment 1 exercise 2c.
with open(casualty_dataset, 'r') as dataset:
    reader = csv.reader(dataset)

    # Print de eerste 10 rows van de dataset.
    limit = 10
    for row in reader:
        if limit == 0:
            break
        else:
            print(row)
            limit -= 1
