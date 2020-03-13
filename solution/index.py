import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import dash_app
from app import server

from dash_apps.app1.dboard import layout as lay1
from dash_apps.app2.dboard import layout as lay2



dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('Navigate to "/page-1"', href='/app1'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/app2'),
])

@dash_app.callback(Output('page-content', 'children'),
                 [Input('url', 'pathname')])
def display_page(pathname):
    if pathname=='/app1':
        return lay1
    elif pathname=='/app2':
        return lay2
    else:
        return layout_index


if __name__ == '__main__':
    dash_app.run_server(debug=True)



