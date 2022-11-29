import pandas as pd
import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Output, Input


df = pd.read_csv('uk_renewable_energy.csv')
res = pd.DataFrame(df)

fig = px.line(
    res,
    x="Year",
    y="Hydroelectric power",
    title="Energy Resource Consumption"
)

app = dash.Dash(__name__)

app.layout = html.Div([
        html.Div(
            id='header-area-div1',
            children=[
                html.Div(className='Dropdown resource',
                         children=[
                             html.H2('Dash - Renewable Energy'),
                             html.P('''Visualising time series with Plotly - Dash''')
                         ]
                         ),
                html.Label('Dropdown'),
                dcc.Dropdown(
                    id='my-input',
                    options=[{"label": resource, "value": resource} for resource in res.columns[4:]],
                    clearable=False,
                    multi=True,
                    value='Hydroelectric power'
                )
            ],
            style={
                'padding': 70,
                'flex': 1,
                'height': '500px',
                'margin-left': '100px',
                'margin-right': '200px',
                'margin-top': '50px',
                'width': '10%',
                'background-color': 'rgb(229, 235, 239)'
            }
        ),
        html.Div(
            id='header-area-div2',
            children=[
                html.Div(className='Chart resource',
                         children=[
                             html.H2('Dash - Renewable Energy Chart'),
                             html.P('''Visualising time series with Plotly - Dash'''),
                         ]
                         ),
                html.Div(
                    id="graph-container",
                    children=dcc.Graph(
                        id="graph-chart",
                        figure=fig,
                    ),
                )
            ],
            style={
                'padding': 10,
                'flex': 1,
                'height': '620px',
                'margin-right': '100px',
                'margin-top': '50px',
                'text-align': 'center',
                'background-color': 'rgb(208, 227, 103)'
            }
        )
    ],
    style={
        'display': 'flex',
        'flex-direction': 'row'
    }
)


@app.callback(
    Output("graph-chart", "figure"),
    Input("my-input", "value")
)
def update_chart(resource):
    fig = px.line(df,
                  x='Year',
                  y=resource,
                  title="Energy Resource Consumption"
                  )
    fig.update_layout(
        template='plotly_dark',
        xaxis_title='Year',
        yaxis_title='Energy Rate'
        )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
