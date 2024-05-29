from dash import Dash, html, dash_table

import pandas as pd

app = Dash()

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
customers = pd.read_csv('customers.csv')[['customer_id', 'first_name', 'last_name', 'phone', 'email']]

app.layout = [
     dash_table.DataTable(data=customers.to_dict('records'))
]

app.run(debug=True)
