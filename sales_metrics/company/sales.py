"""
company.sales
=============
This module contains the functionaly to calculate company wide specific metrics.
"""

import pandas as pd
#from ..utils import check_df
from sales_metrics.utils import check_df

def total_sales(df_path,sales_col_name):

    sales_df = pd.read_csv(df_path)

    print(sales_df.head())
    return sales_df[sales_col_name].sum()

def top_sale_item(df_path,item_filter,num=3):
    if check_df(df_path)[0]:
        sales_df = check_df(df_path)[1]
    else:
        print('error')
        return False
    top_items = sales_df[['brand_name','profit']].sort_values(by='profit',ascending=False)
    top_items = top_items.groupby(item_filter).sum().head(num).sort_values(by='profit',ascending=False)
    return top_items
