import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import numpy as np
import pandas as pd


app = dash.Dash()
df = pd.read_csv('mpg.csv')

features = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis', 
            options=[{'label': i, 'value':i } for i in features], 
            value='displacement'
            )
    ],
    style ={'width':'48%', 'display': 'inline-block'} 
    ),
    html.Div([
        dcc.Dropdown(id='yaxis', 
        options=[{'label': i, 'value':i } for i in features], 
        value='mpg')
    ],
    style ={'width':'48%', 'display': 'inline-block'} 
    ),
    dcc.Graph(id='feature-graphic')
], style={'padding':10})


@app.callback(Output('feature-graphic', 'figure'), 
                [
                    Input('xaxis', 'value'),
                    Input('yaxis', 'value')
                ]
            )
def update_graph(xaxis_name, y_axis_name):
    return {
        'data':[
            go.Scatter(
                x=df[xaxis_name],
                y=df[y_axis_name], 
                text =df['name'], 
                mode='markers', 
                marker={
                    'size':15,
                    'opacity': 0.5, 
                    'line':{
                        'width': 0.5, 
                        'color': 'red'
                    }
                    }
        )],
     'layout':go.Layout(
         title='My Dashboard for MPG', 
         xaxis ={'title': xaxis_name}, 
         yaxis={'title': y_axis_name}, 
         hovermode='closest'
     )}


if __name__ == '__main__':
    app.run_server()