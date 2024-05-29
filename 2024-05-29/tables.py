from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc

import pandas as pd

app = Dash()

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
customers = pd.read_csv('customers.csv')[['customer_id', 'first_name', 'last_name', 'phone', 'email']]

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/orders.csv
orders = pd.read_csv('orders.csv')

app.layout = [
    dbc.Row(childdren=[
        dbc.Col(children='left'),
        dbc.Col(children='right'),
    ]),
     dash_table.DataTable(data=customers.to_dict('records')),
     dash_table.DataTable(data=orders.to_dict('records')),
]

app.run(debug=True)
