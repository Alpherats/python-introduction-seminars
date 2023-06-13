# Работать с файлом california_housing_train.csv
#
import pandas as pd
data = pd.read_csv('california_housing_test.csv')

# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

median_house_value_filtered = filtered_data['median_house_value']

print(median_house_value_filtered)

