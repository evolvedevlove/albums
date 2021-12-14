# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:23:05 2021

@author: Patty Whack
"""
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
#import plotly

app = dash.Dash(__name__)
app.layout = html.Div(children = [
    html.H1('Albums I listetend to in 2017'),
    html.H2('This is a dash app'),
    dcc.Input(id="x"),
    html.H3(id="x_out")
    ])

@app.callback(Output('x_out', 'children'), [Input('x','value')])
def cb(x):
    return x

app.run_server(debug=True)