from dash import Dash, html, dash_table, Input, Output, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = [
    dcc.Dropdown(
        id='dropdown', options=[], value='', style={'margin': '12px'}),
    dbc.Row(children=[
        dbc.Col(
            children=dash_table.DataTable(id='customers'),
        ),
        dbc.Col(
            children=dash_table.DataTable(id='orders'),
        ),
    ]),
    dcc.Graph(id='graph'),
]


@app.callback(
    [
        Output(component_id='customers', component_property='data'),
        Output(component_id='orders', component_property='data'),
        Output(component_id='dropdown', component_property='options'),
        Output(component_id='graph', component_property='figure'),
    ],
    [
        Input(component_id='dropdown', component_property='value'),
    ]
)
def update(last_name):
    ## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
    all_customers = pd.read_csv('customers.csv')[['customer_id', 'first_name', 'last_name']]
    customers = all_customers[all_customers['last_name'] == last_name]

    ## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/orders.csv
    orders = pd.read_csv('orders.csv')[['order_id', 'customer_id', 'order_date']]

    filtered_orders = pd.merge(left=customers, right=orders, on='customer_id')

    groups = filtered_orders.groupby('customer_id').size().reset_index()
    groups.columns = ['customer_id', 'count']
    
    return [
        customers.to_dict('records'),
        filtered_orders.to_dict('records'),
        all_customers.last_name,
        px.bar(groups),
    ]

app.run(debug=True)
