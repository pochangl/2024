# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, html, Input, Output

app = Dash()

app.layout = [
    html.P(children='Hello world'),

    # 請加上按鈕
    html.Button(children='點我'),

    # 加上點擊次數
    html.P(children='己點擊 0 次'),
]

app.run(debug=True)
