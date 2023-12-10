# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for car, row in cars.iterrows() :
    print(car)
    print(row)
