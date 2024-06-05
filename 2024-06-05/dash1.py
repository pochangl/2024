from dash import Dash, html, dcc
import pandas as pd

customers = pd.read_csv('customers.csv')

app = Dash()
app.layout = dcc.DataTable()


app.run(debug=True)