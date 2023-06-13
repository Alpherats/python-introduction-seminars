# Узнать какая максимальная households в зоне минимального значения population.
import pandas as pd
data = pd.read_csv('california_housing_test.csv')

min_population = data['population'].min()
min_population_data = data[data['population'] == min_population]
max_households = min_population_data['households'].max()
print(max_households)