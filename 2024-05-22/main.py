# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, html

app = Dash()

app.layout = [
    html.P(children='Hello world')
    # 請加上按鈕
]

app.run(debug=True)
