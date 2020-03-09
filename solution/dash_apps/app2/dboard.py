import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

from app import dash_app

import pandas as pd

crimedata = pd.read_csv(
	'https://raw.githubusercontent.com/itsimplified/dash-web-app/master/crimedata.csv')
features = crimedata.columns
crimetypes = features[:-1]

#add markdown text
markdown_text = """
DATA used for this dashboard was taken from the US Department of Justice website which can be accessed [here.](https://ucr.fbi.gov/crime-in-the-u.s/2016/crime-in-the-u.s.-2016/topic-pages/tables/table-1)
"""


layout = html.Div([
	html.Div([
            #Here is the interactive component
          		html.Div([
                            dcc.Dropdown(
				id='yaxis',
				options=[{'label': i, 'value': i} for i in crimetypes],
				value='Assault'
                            )
                        ], style={'width': '40%'})
	]),
	html.Div([dcc.Graph(
		id='crime-graphic',
		figure={
			'data': [go.Scatter(
				x=crimedata['Year'],
				y=[0, 0],
				mode='markers'
			)],
			'layout': go.Layout(
				title='Use the dropdown to display the chart ...',
				xaxis={'tickformat': 'd'}
			)
		})], 
        style={'width': '50%', 'display': 'inline-block'}
    ),
	html.Div([dcc.Graph(
		id='crime-stacked',
		figure={
			'data': [go.Bar(
				x=crimedata['Year'],
				y=crimedata[i],
				name=i)
                            for i in crimetypes],

			'layout': go.Layout(
				title='Crime in the United States by Volume, 1997–2016',
				barmode='stack'
			)
		}
        )
	], style={'width': '50%', 'display': 'inline-block'}),
	html.Div([dcc.Graph(
		id='crime-boxplot',
		figure={
			'data': [go.Box(y=crimedata[i],
                            name=i
                   ) for i in crimedata],
			'layout': go.Layout(
                            title='Crime in the United States by Volume, 1997–2016'
			)
		}
	)
	], style={'width': '50%', 'display': 'inline-block'}),
	html.Div([
		dcc.Markdown(children=markdown_text)
	])
], style={'padding': 10})

#Here is the callback


@dash_app.callback(
	Output('crime-graphic', 'figure'),
	[Input('yaxis', 'value')])
def update_graphic(yaxis_crime):
	return {
		'data': [go.Scatter(
			x=crimedata['Year'],
			y=crimedata[yaxis_crime],
			mode='lines+markers',
			marker={
				'size': 15,
				'opacity': 0.5,
				'line': {'width': 0.5, 'color': 'white'}
			}
		)],
		'layout': go.Layout(
			title='{} in the US by Volume, 1997-2016'.format(yaxis_crime),
			xaxis={'title': 'Year'},
			yaxis={'title': yaxis_crime},
			hovermode='closest'
		)
	}
