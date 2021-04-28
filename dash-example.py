import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

colors ={'background':'#111111', 'text':'#7FDBFF'}



app.layout = html.Div(children=[
    html.H1('Hello world!', style ={'textAlign' :'center', 'color': colors['text']}),

    dcc.Graph(id="scatterplot",
              figure ={'data':[
                  go.Scatter(
                      x=random_x,
                      y=random_y,
                      mode='markers',
                      marker={
                          'size': 12,
                          'color': 'rgb(51,204,153)'
                      }
                  )
              ],
              'layout': go.Layout(title='my scatterplot')
              }

              ),

    dcc.Graph(id='example',
              figure={
                      'data':[
                          {'x':[1,2,3], 'y' :[4,5,6], 'type':'bar', 'name':'SF'},
                          {'x':[1,2,3], 'y' :[2,4,5], 'type':'bar', 'name':'NY'}

                      ],
                    'layout':{
                    'plot_bgcolor' : colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font':{'color': colors['text']},
                    'title': 'BAR PLOTS!'
                  }
              })
],
    style={'backgroundColor': colors['background']}
)


if __name__=='__main__':
    app.run_server()