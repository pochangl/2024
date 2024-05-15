from dash import Output, Input, Dash, html

app = Dash()


app.layout = [
    html.Div(id='my-output', children=2),
    html.Div(id='my-output-1'),
    html.Img(src='assets/A229.png'),
    html.Button(id='my-button', n_clicks=0, children='+1'),
]


@app.callback(
        Output(component_id="my-output", component_property="children"),   #Output("my-output", "children"),
        Output(component_id="my-output-1", component_property="children"),
        Input(component_id="my-button", component_property="n_clicks"),
)  # @表裝飾器，下面一行須直接接函式

def click_button(n):  #兩個input，()內就有兩個代數
    return n, n+10

app.run(debug=True)