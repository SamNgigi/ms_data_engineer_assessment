import dash
import flask

from dash import Dash
from flask import Flask


def create_flask():

    flask_app = Flask(__name__)

    return flask_app


def create_dash():
    flask_app = create_flask()
    ext_styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app = Dash(__name__, server=flask_app, external_stylesheets=ext_styles)
    dash_app.config.suppress_callback_exceptions = True
    return dash_app


# # flask_app = create_flask()
dash_app = create_dash()
server = dash_app.server


