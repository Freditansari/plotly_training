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
    dcc.Graph(id="scatterplot",
              figure={'data': [
                  go.Scatter(
                      x=df['X'],
                      y=df['Y'],
                      mode='markers',
                      marker={
                          'size': 12,
                          'color': 'rgb(51,204,153)'
                      }
                  )
              ],
                  'layout': go.Layout(
                      title='Ye ol faithful',
                      plot_bgcolor= colors['background'],
                      paper_bgcolor= colors['background'],
                      font={'color': colors['text']},
                      xaxis={'title': 'Duration'},
                      yaxis={'title': 'Interval'}
                  )
              }

              ),
])

if __name__=='__main__':
    app.run_server()