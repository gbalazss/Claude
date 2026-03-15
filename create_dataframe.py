"""Create a pandas DataFrame with sample data."""

from typing import Any

import pandas as pd


def create_sample_dataframe() -> pd.DataFrame:
    """Create a DataFrame with 3 columns and 5 rows.

    Returns:
        A DataFrame with numeric, string, and float
        columns.
    """
    data: dict[str, list[Any]] = {
        'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e'],
        'column3': [10.5, 20.5, 30.5, 40.5, 50.5],
    }
    return pd.DataFrame(data)


if __name__ == '__main__':
    df = create_sample_dataframe()
    print(df)



