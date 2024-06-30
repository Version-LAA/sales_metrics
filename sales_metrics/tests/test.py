# test_script.py
import sys
import os

# Add the path to the sales_metrics package to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'sales_metrics')))

from sales_metrics.utils import check_df
from sales_metrics.company.sales import top_sale_item, total_sales
from sales_metrics.employee.performance import top_employee

df = check_df('sales_data.csv')


print(total_sales('/Users/latoyaalford/code/Version-LAA/sales_metrics/sales_metrics/tests/sales_data.csv','profit'))
print(top_sale_item('/Users/latoyaalford/code/Version-LAA/sales_metrics/sales_metrics/tests/sales_data.csv','brand_name'))

print(top_employee('/Users/latoyaalford/code/Version-LAA/sales_metrics/sales_metrics/tests/test_employee.csv','total_sales','employee_name'))
