from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc

import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
customers = pd.read_csv('customers.csv')[['customer_id', 'first_name', 'last_name']]

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/orders.csv
orders = pd.read_csv('orders.csv')[['order_id', 'customer_id', 'order_date']]

app.layout = [
    dbc.Row(children=[
        dbc.Col(
            style={"padding": "10px"},
            children=dash_table.DataTable(data=customers.to_dict('records')),
            xs=4,
        ),
        dbc.Col(
            style={"padding": "10px"},
            children=dash_table.DataTable(data=orders.to_dict('records')),
            xs=8,
        ),
    ]),
     
     
]

app.run(debug=True)
