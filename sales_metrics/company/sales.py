"""
company.sales
=============
This module contains the functionaly to calculate company wide specific metrics.
"""

import pandas as pd


def total_sales(df_path,sales_col_name):

    sales_df = pd.read_csv(df_path)

    print(sales_df.head())
    return sales_df[sales_col_name].sum()

def top_sale_item(df_path,item_filter,num=3):
    sales_df = pd.read_csv(df_path)
    top_items = sales_df[['brand_name','profit']].sort_values(by='profit',ascending=False)
    top_items = top_items.groupby(item_filter).sum().head(num).sort_values(by='profit',ascending=False)
    print(top_items)

print(total_sales('/Users/latoyaalford/code/Version-LAA/sales_metrics/sales_data.csv','profit'))
top_sale_item('/Users/latoyaalford/code/Version-LAA/sales_metrics/sales_data.csv','brand_name')
