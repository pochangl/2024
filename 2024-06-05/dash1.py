from dash import Dash, html, dcc, dash_table
import pandas as pd

customers = pd.read_csv('customers.csv')

app = Dash()
app.layout = html.Div(
    children=[
        dcc.Input(id='filter', placeholder='請輸入您想尋找的資料'),
        dash_table.DataTable(id='datatable', data=customers.to_dict('records')),
    ]
)

# 把 read_csv 跟 datatable data 的部份放到 callback 裡
        
app.run(debug=True)
