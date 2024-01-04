import dash
from dash import dcc, html
from dash.dependencies import Input, Output

colors = {
    'background': '#111111',
    'text': '#ffffff'
}

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'width': '100%'},
    children=[
        html.Div(
            children=[
                html.H1('A Floating Map of Seoul', style={'color': colors['text']})
            ],
            style={"display": "inline-block", 'width': '30%', "vertical-align": "top"}
        ),
        html.Div(
            children=[
                html.H1('Seoul Population Movement', style={'color': '#fff'}),
                html.P('Move the slider to view the population movement:'),
                dcc.Slider(
                    id='timeSlider',
                    min=0,
                    max=23,
                    value=8,
                    marks={i: str(i) for i in range(24)},
                ),
                html.P(['Time: ', html.Span(id='timeDisplay', children='8'), ':00']),
                html.Iframe(id='map', src='arc_layer_8.html', style={'width': '100%', 'height': '600px'}) 
            ],
            style={'backgroundColor': '#000'}
        )
    ]
)

@app.callback(
    [Output('timeDisplay', 'children'), Output('map', 'src')],
    [Input('timeSlider', 'value')]
)
def update_output(value):
    return value, f"arc_layer_{value}.html"

if __name__ == '__main__':
    app.run_server(debug=True)
