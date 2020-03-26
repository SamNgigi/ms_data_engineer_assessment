import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt

import pandas as pd

# Data
from ..visualization_data import people_class, gapminder, people_enrolled_final, graduate_persons


PAGE_SIZE = 50

common_style = {'width': '50%', 'display': 'inline-block'}


# *TABLE 1
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

# *TABLE 2
enrollment_datatable = html.Div([

    html.H5(
        children='Enrolled Student List by Module & Class',
        style={
            'textAlign': 'center',
        }
    ),

    html.P(
        children='Filter by class or/and module',
        style={
            'textAlign': 'center',
        }
    ),

    dt.DataTable(
        id="table",
        columns=[{"name": col_name, "id": col_name}
                 for col_name in people_enrolled_final.columns],
        data=people_enrolled_final.to_dict("records"),
        fixed_rows={'headers': True, 'data': 0},
        style_header={
            "backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
        style_cell={"textAlign": "left", "maxWidth": 0},
        style_table={
            'marginTop': '30px',
            'maxHeight': '300px',
            'overflowY': 'scroll'
        },
        filter_action="native"
    )
], style={"padding": "50px"})


# *TABLE 3
graduate_datatable = html.Div([

    html.H5(
        children='Graduates table filterable by class',
        style={
            'textAlign': 'center',
        }
    ),

    html.P(
        children='Filter table by class',
        style={
            'textAlign': 'center',
        }
    ),

    dt.DataTable(
        id="table",
        columns=[{"name": col_name, "id": col_name}
                 for col_name in graduate_persons.columns],
        data=graduate_persons.to_dict("records"),
        fixed_rows={'headers': True, 'data': 0},
        style_header={
            "backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
        style_cell={"textAlign": "left", "maxWidth": 0},
        style_table={
            'marginTop': '30px',
            'maxHeight': '300px',
            'overflowY': 'scroll'
        },
        filter_action="native"
    )
], style={"padding": "50px"})

# *VISUALIZATION 1
gapminder_lay = html.Div([
    html.Label('Select Module'),
    dcc.Dropdown(
        id='cohort-module-col',
        options=[{"label": col_val, "value": col_val}
                 for col_val in people_enrolled_final['module_name'].unique()],
        value="charms"
    ),
    # Ouput graph
    dcc.Graph(id='module-class-count'),

    # Gapminder slider
    dcc.Slider(
        id='year-slider',
        min=gapminder['year'].min(),
        max=gapminder['year'].max(),
        value=gapminder['year'].min(),
        marks={str(year): str(year) for year in gapminder['year'].unique()},
        step=None
    )
], style=common_style)

# *VISUALIZATION 2
hogwarts_yr = html.Div([
    html.Label('Select Hogwarts Cohort'),
    dcc.Dropdown(
        id='cohort-col',
        options=[{"label": col_val, "value": col_val}
                 for col_val in people_class['class_name'].unique()],
        value='HC_1'
    ),

    dcc.Graph(id='hogwarts-cohort'),

    dcc.Slider(
        id='hogwarts-year-slider',
        min=people_class["year"].min(),
        max=people_class["year"].max(),
        value=people_class["year"].min(),
        marks={str(yr): str(yr) for yr in people_class["year"].unique()},
        step=None
    )
], style=common_style)



layout3 = html.Div([

#     

    # *TABLE 1
    applicant_datatable,
    
    # *TABLE 2
    enrollment_datatable,
    # *TABLE 3
    graduate_datatable,

    html.Div([
        # *VISUALIZATION 1
        gapminder_lay,

        # *VISUALIZATION 2
        hogwarts_yr,
    ], style={"display": "inline-block", "width": "100%"})
])



