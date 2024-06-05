from dash import Dash, html, dcc, dash_table
import pandas as pd

customers = pd.read_csv('customers.csv')

app = Dash()
app.layout = dash_table.DataTable()


app.run(debug=True)