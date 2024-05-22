# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, html

app = Dash()

app.layout = [
    html.P(children='Hello world'),

    # 請加上按鈕
    html.Button(children='點我', n_clicks=0),

    # 使用 callback, Input, Output 加上點擊次數
    html.P(children='己點擊 0 次'),
]

@app.callback(
    [],
    []
)
def on_click(n_clcks):

    return

app.run(debug=True)
