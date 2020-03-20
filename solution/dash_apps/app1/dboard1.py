import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd

from app import dash_app

from flask_apps.models.Applications import ApplicationsSql

from ..visualization_data import graduates, class_applications

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


layout = html.Div([
    html.Div([dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([dcc.Graph(
        id='crime-stacked',
        figure={
            'data': [go.Bar(
                x=['graduates', 'applicants'],
                y=[graduates.shape[0], class_applications.shape[0]],
                name='graduates',
                marker_color='rgb(26, 118, 255)')],

         			'layout': go.Layout(
                title='Total Applicants vs Graduates'
            )
        }
    )
    ], style={'width': '50%', 'display': 'inline-block'})
])
