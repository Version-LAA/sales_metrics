"""
employee.performance
=============
This module contains the functionaly to calculate employee specific metrics.
"""

import pandas as pd
#from ..utils import check_df
from sales_metrics.utils import check_df

def top_employee(df_path,sales_col,employee_col,top=3):
    sales_df = pd.read_csv(df_path)
    top_emp_sorted = sales_df[[employee_col,sales_col]].sort_values(by=sales_col,ascending=False).head(top)
    return top_emp_sorted
