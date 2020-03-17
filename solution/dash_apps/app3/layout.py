import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt

import pandas as pd

# Data
from ..visualization_data import people_class, gapminder


PAGE_SIZE = 50

common_style = {'width': '50%', 'display': 'inline-block'}


# *VISUALIZATION 1
gapminder_lay = html.Div([
    html.Label('Select Year'),
    dcc.Dropdown(
        id='cohort-year-col',
        options=[{"label": col_val, "value": col_val}
                 for col_val in people_class['year'].unique()]
    ),
    # Ouput graph
    dcc.Graph(id='graph-with-slider'),

    # Gapminder slider
    dcc.Slider(
        id='year-slider',
        min=gapminder['year'].min(),
        max=gapminder['year'].max(),
        value=gapminder['year'].min(),
        marks={str(year):str(year) for year in gapminder['year'].unique()},
        step=None
    )
],style=common_style)

# *VISUALIZATION 2
hogwarts_yr = html.Div([
    html.Label('Select Hogwarts Cohort'),
    dcc.Dropdown(
        id='cohort-col',
        options=[{"label": col_val, "value": col_val}
                    for col_val in people_class['class_name'].unique()]
    ),

    dcc.Graph(id='hogwarts-slider'),

    dcc.Slider(
        id='hogwarts-year-slider',
        min=people_class["year"].min(),
        max=people_class["year"].max(),
        value=people_class["year"].min(),
        marks={str(yr): str(yr) for yr in people_class["year"].unique()},
        step=None
    )
], style=common_style)

# *VISUALIZATION 3
applicant_datatable = html.Div([

    html.H5(
        children='Applicant List',
        style={
            'textAlign': 'center',
        }
    ),

    html.P(
        children='Filter by class',
        style={
            'textAlign': 'center',
        }
    ),

    dt.DataTable(
        id="table",
        columns=[{"name": col_name, "id": col_name}
                 for col_name in people_class.columns],
        data=people_class.to_dict("records"),
        fixed_rows={'headers': True, 'data': 0},
        style_header={
            "backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
        style_cell = {"textAlign": "left", "maxWidth":0},
        style_table={
            'marginTop': '30px',
            'maxHeight': '300px',
            'overflowY': 'scroll'
        },
        filter_action="native"
    )
], style={"padding":"50px"})



layout3 = html.Div([

#     # *VISUALIZATION 1
#    gapminder_lay,

#     # *VISUALIZATION 2
#     hogwarts_yr,

    # *VISUALIZATION 3
    applicant_datatable,

    html.Div([
        gapminder_lay,
        hogwarts_yr
    ], style={"display": "inline-block", "width": "100%"})
])



