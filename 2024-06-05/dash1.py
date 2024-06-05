from dash import Dash, html, dcc, dash_table
import pandas as pd

customers = pd.read_csv('customers.csv')

app = Dash()
app.layout = html.Div(
    children=[
        dcc.Input(id='filter', placeholder='請輸入您想尋找的資料'),
        dash_table.DataTable(id='datatable', customers.to_dict('records')),
    ]
)

        
app.run(debug=True)
