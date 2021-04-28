import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('OldFaithful.csv')
colors = {'background': '#111111', 'text': '#7FDBFF'}
app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-id', value='Initial Text', type='text'),
    html.Div(id='my-div')

])


@app.callback(Output(component_id='my-div', component_property='children'),
              [Input(component_id='my-id', component_property='value')])
def update_output_div(input_value):
    return "You entered : {}".format(input_value)


if __name__ == '__main__':
    app.run_server()
