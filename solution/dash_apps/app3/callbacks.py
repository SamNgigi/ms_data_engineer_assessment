from dash.dependencies import Input, Output
import plotly.graph_objs as go

from app import dash_app
from ..visualization_data import people_class, gapminder, modulebyClass


@dash_app.callback(Output('module-class-count', 'figure'),
                  [Input('cohort-module-col', 'value')])
def update_graph(selected_module):
    filtered_df = modulebyClass[modulebyClass['module_name'] == selected_module]

    return {
        'data': [
            go.Bar(
                x=filtered_df['class_name'],
                y=filtered_df['mod_count'],
                marker_color='rgb(26, 118, 255)'
            )
        ],
        'layout': go.Layout(
            xaxis={'title': 'Class name'},
            yaxis={'title': f'{selected_module} module count'},
            title='Total Student Count per Class by module'
        )
    }


@dash_app.callback(
    Output('hogwarts-cohort', 'figure'),
    [Input('cohort-col', 'value')]
)
def update_figure(selected_cohort):
    filtered_df = modulebyClass[modulebyClass['class_name']
                                == selected_cohort]

    return {
        'data': [
            go.Bar(
                x=filtered_df['module_name'],
                y=filtered_df['mod_count'],
                text=round((max(filtered_df['mod_count']) -filtered_df['mod_count'])/ max(filtered_df['mod_count']), 2) * 100,
                textposition='auto',
                marker_color='rgb(26, 118, 255)'
            )
        ],
        'layout': go.Layout(
            xaxis={'title': 'Module Name'},
            yaxis={'title': f'{selected_cohort} per module count'},
            title='Total Student Count & % drop per Class by module'
        )
    }
