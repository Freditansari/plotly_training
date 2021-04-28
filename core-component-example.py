import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('OldFaithful.csv')
colors ={'background':'#111111', 'text':'#7FDBFF'}
app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options =[{
        'label': 'New York City',
        'value': 'NYC'
    },
    {
        'label': 'San Francisco',
        'value': 'SF'
    }
    ],
        value='SF'
    ),

    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step=0.5, value=0),

    html.Label('Slider with marks '),
    dcc.Slider(min=-10, max=10, step=0.5, value=0, marks ={i: i for i in range(-10, 10)}),


    html.Label('Some Radio items'),
    dcc.RadioItems(options=[
    {
        'label': 'New York City',
        'value': 'NYC'
    },
    {
        'label': 'San Francisco',
        'value': 'SF'
    }
    ],
        value='SF'
    )
])

if __name__=='__main__':
    app.run_server()