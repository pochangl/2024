from dash import Dash, html

import pandas as pd

app = Dash()

## https://raw.githubusercontent.com/pochangl/2024/main/2024-05-08/customers.csv
data = pd.read_csv('customers.csv')

app.layout = [
    html.Div(children='Hello world')
]

app.run(debug=True)
