from dash import Dash, html

app = Dash()

app.layout = [
    html.Div(children='Hello world')
]

app.run(debug=True)
