import csv
import pandas

accident_dataset = "./dataset/dft-road-casualty-statistics-accident-1979-2020.csv"
casualty_dataset = "./dataset/dft-road-casualty-statistics-casualty-1979-2020.csv"
vehicle_dataset = "./dataset/dft-road-casualty-statistics-vehicle-1979-2020.csv"

# Load a dataset in a pandas dataframe. We only import the first 50.000 rows.
dataframe = pandas.read_csv(casualty_dataset, nrows=50000)

# Print some statistics
# Assignment 1 exercise 2d
print(dataframe.describe())

# Loop through columns and see where the empty values are.
# This does not seem to work yet.
# This is assignment 1 exercise 2F.
for column in dataframe:
    for item in dataframe[column].values:
        if item is None:
            print("is empty")


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