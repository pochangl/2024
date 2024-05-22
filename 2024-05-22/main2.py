# 目標建立 Hello world 的 dash 程式
# 在網頁上顯示 Hello World

from dash import Dash, dcc, html, Input, Output

app = Dash()

app.layout = [
    # 試著加入2個文字輸入框, 使用 dcc.Input
    dcc.Input(placeholder="請輸入文字"),
    dcc.Input(placeholder="請輸入數字", type="number"),

    # 在頁面上顯示輸入的文字跟數字
    html.P('您輸入的文字是: '),
    html.P('您輸入的數字是: '),
]

app.run(debug=True)
