# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, html

app = Dash()

app.layout = [html.P(children='Hello world')]

app.run(debug=True)
