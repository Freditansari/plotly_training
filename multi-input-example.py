import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('mpg.csv')

app = dash.Dash()