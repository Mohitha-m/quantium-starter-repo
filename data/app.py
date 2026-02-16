import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello, Dash!'),
    html.P(children='This is your test app running correctly.')
])

if __name__ == '__main__':
    app.run(debug=True)

