# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, dcc, html, Input, Output, Graph
import numpy as np
import plotly.express as px

x = np.arange(-5, 5)
y = 2 * x + 3

app = Dash()

app.layout = [
    # 試著加入2個文字輸入框, 使用 dcc.Input
    dcc.Input(placeholder="請輸入 a", id="a_input", type="number", value=2),
    dcc.Input(placeholder="請輸入 b", id="b_input", type="number", value=3),

    # 在頁面上顯示輸入的文字跟數字
    html.P(children='您輸入的a是: ', id='a_output'),
    html.P(children='您輸入的b是: ', id='b_output'),
    dcc.Graph(figure=px.line(x=x, y=y)),
]

app.run(debug=True)
