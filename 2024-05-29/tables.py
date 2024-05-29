from dash import Dash, html, dash_table, Input, Output, dcc
import dash_bootstrap_components as dbc

import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = [
    dbc.Row(children=[
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal', multi=True),
        dbc.Col(
            children=dash_table.DataTable(id='customers'),
        ),
        dbc.Col(
            children=dash_table.DataTable(id='orders'),
        ),
    ]),
]


@app.callback(
    [
        Output(component_id='customers', component_property='data'),
        Output(component_id='orders', component_property='data'),
    ],
    [
        Input(component_id='customers', component_property='style'),
    ]
)
def update(_):
    ## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
    customers = pd.read_csv('customers.csv')[['customer_id', 'first_name', 'last_name']]

    ## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/orders.csv
    orders = pd.read_csv('orders.csv')[['order_id', 'customer_id', 'order_date']]
    return customers.to_dict('records'), orders.to_dict('records')

app.run(debug=True)
