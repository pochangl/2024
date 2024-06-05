from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd


app = Dash()
app.layout = html.Div(
    children=[
        dcc.Input(id='filter', placeholder='請輸入您想尋找的資料', value=''),
        dash_table.DataTable(id='datatable', data=[]),
    ]
)

# 把 read_csv 跟 datatable data 的部份放到 callback 裡
@app.callback(
[
    Output(component_id='datatable', component_property='data'),
],
[
    Input(component_id='filter', component_property='value'),
])
def onFilter(filter):
    customers = pd.read_csv('customers.csv')
    return [customers.to_dict('records')]
        
app.run(debug=True)
