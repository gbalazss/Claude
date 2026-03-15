import pandas as pd

# Create a dataframe with 3 columns and 5 rows
df = pd.DataFrame({
    'column1': [1, 2, 3, 4, 5],
    'column2': ['a', 'b', 'c', 'd', 'e'],
    'column3': [10.5, 20.5, 30.5, 40.5, 50.5]
})

print(df)
