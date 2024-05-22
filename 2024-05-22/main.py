# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, html, Input, Output

app = Dash()

app.layout = [
    html.P(children='Hello world'),

    # 請加上按鈕
    html.Button(id="btn", children='點我', n_clicks=0),

    # 使用 callback, Input, Output 加上點擊次數
    html.P(id="num_clicks", children='己點擊 0 次'),
]

@app.callback(
    [
        Input(component_id='btn', component_property='n_clicks')
    ],
    [
        Output(component_id="num_clicks", component_property='children'),
    ],
)
def on_click(n_clicks):
    return f'己點擊 {n_clicks} 次'

app.run(debug=True)
