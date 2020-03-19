import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd

from app import dash_app

from flask_apps.models.Applications import ApplicationsSql

from ..visualization_data import graduates, class_applications, classes_df, admitted_students

from ..app3.layout import layout3

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = go.Figure()


# Graduation numbers per class
gradbyClass = graduates.groupby('class_id').size().to_frame(
    name='grad_count').reset_index()
gradbyClass = pd.merge(
    gradbyClass, classes_df[['class_id', 'class_name']], how='inner', on='class_id')
gradbyClass.drop('class_id', axis=1, inplace=True)
gradbyClass

# Application numbers per class
appbyClass = class_applications.groupby(
    'class_id').size().to_frame(name='app_count').reset_index()
appbyClass = pd.merge(
    appbyClass, classes_df[['class_id', 'class_name']], how='inner', on='class_id')
appbyClass.drop('class_id', axis=1, inplace=True)
appbyClass

# Admission numbers per class
admissionsbyClass = admitted_students.groupby(
    'class_id').size().to_frame(name='admission_count').reset_index()
admissionsbyClass = pd.merge(admissionsbyClass, classes_df[[
                             'class_id', 'class_name']], how='inner', on='class_id')
admissionsbyClass.drop('class_id', axis=1, inplace=True)
admissionsbyClass

layout = html.Div([

    html.H1(
        children='Hogwarts Dashboard',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(children='This dashboard was created for the MS data-engineering assesment. It is still in development.', style={
        'textAlign': 'center',
    }),

    # *VISUALIZATION 1
    html.Div([dcc.Graph(
        id='ms-bars',
        figure={
            'data': [go.Bar(
                x=['graduates', 'applicants'],
                y=[graduates.shape[0], class_applications.shape[0]],
                name='graduates',
                marker_color='rgb(26, 118, 255)')],

            'layout': go.Layout(
                yaxis={'title': 'Counts'},
                title='Total Graduates and Applicants'
            )
        }
    )
    ], style={'width': '50%', 'display': 'inline-block'}),

    # *VISUALIZATION 2
    html.Div([dcc.Graph(
        id='ms-group-bars',
        figure={
            'data': [
                go.Bar(
                    x=gradbyClass['class_name'].values.tolist(),
                    y=gradbyClass['grad_count'].values.tolist(),
                    name='Graduates',
                    marker_color='rgb(26, 118, 255)'
                ),
                go.Bar(
                    x=appbyClass['class_name'].values.tolist(),
                    y=appbyClass['app_count'].values.tolist(),
                    name='Applicants',
                    marker_color='rgb(55, 83, 109)'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Class name'},
                yaxis={'title': 'Counts'},
                title='Total Graduates & Applicants per Class',
                barmode='group'
            )
        }
    )],style={'width': '50%', 'display': 'inline-block'}),

    # *VISUALIZATION 3
    html.Div([dcc.Graph(
        id='ms-bars',
        figure={
            'data': [go.Bar(
                x= admissionsbyClass['class_name'].values.tolist(),
                y= admissionsbyClass['admission_count'].values.tolist(),
                name='admitted students',
                marker_color='lightsalmon')],

            'layout': go.Layout(
                title='No of students admitted per Class'
            )
        }
    )
    ], style={'width': '50%', 'display': 'inline-block'}),

    # *VISUALIZATION 4
    html.Div([dcc.Graph(
        id='ms-bars',
        figure={
            'data': [
                go.Bar(
                    x=sorted(graduates['gender'].unique()),
                    y=graduates['gender'].value_counts().sort_index(),
                    name='Graduates',
                    marker_color='rgb(26, 118, 255)'
                ),
                go.Bar(
                    x=sorted(class_applications['gender'].unique()),
                    y=class_applications['gender'].value_counts().sort_index(),
                    name='Applicants',
                    marker_color='rgb(55, 83, 109)'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Gender'},
                yaxis={'title': 'Counts'},
                title='Total Graduates & Applicants by Gender',
                barmode='group'
            )
        }
    )
    ], style={'width': '50%', 'display': 'inline-block'}),

    layout3
])
