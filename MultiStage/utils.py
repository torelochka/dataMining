import pandas as pd

SUPPORT_S = 3


def get_data():
    df = pd.read_csv('dataset.csv', sep=';', nrows=1000)
    df: pd.DataFrame = df[df['CustomerID'].notna()]
    return df


def get_index_from_dict(dictionary):
    return len(dictionary.keys())+1
