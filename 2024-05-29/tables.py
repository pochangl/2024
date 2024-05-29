from dash import Dash, html, dash_table

import pandas as pd

app = Dash()

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
data = pd.read_csv('customers.csv')

app.layout = [
    dash_table.DataTable(data),
]

app.run(debug=True)
