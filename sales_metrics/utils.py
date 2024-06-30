"""
Utilities module
"""
import pandas as pd


def check_df(dataframe_path):
    try:
        df = pd.read_csv(dataframe_path)
        print('successful import')
    except:
        print('Error reading df')
        return(False,'')
    return (True,df)
