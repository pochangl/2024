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
def onFilter(text: str):
    customers = pd.read_csv('customers.csv')

    # 把 last_name 抽出來, 然後每個比對看有沒有包含 text 的字串
    filter1 = customers['last_name'].str.contains(text)
    filter2 = customers['first_name'].str.contains(text)
    try:
        filter3 = customers['customer_id'] == int(text)
    except ValueError:
        filter3 = False
    customers = customers[filter1 | filter2 | filter3]
    data = customers.to_dict('records')
    return [data]
        
app.run(debug=True)
