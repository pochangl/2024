# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, html

app = Dash()

app.layout = [
    html.P(children='共點 0 次'),
    # 請加上按鈕
    html.Button(children='點我')
]

app.run(debug=True)
