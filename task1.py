import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


labels, uniques = pd.factorize(data['whoAmI'])

one_hot_matrix = np.eye(len(uniques))[labels]

for i, unique_value in enumerate(uniques):
    column_name = f'whoAmI_{unique_value}'
    data[column_name] = one_hot_matrix[:, i]

data.head()
print(data)