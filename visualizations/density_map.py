import pandas as pd
import plotly.express as px

data = pd.read_csv(r"C:\Users\20202478\Documents\School\Year 2\Q2\JBI100 Visualization\Visualization_full.csv")

#Reduced data for faster loading
red_data = data[data["accident_year"] >= 2018]
	
def dens_map(df, rad):
   fig = px.density_mapbox(df, lat='latitude', lon='longitude', radius=rad, center=dict(lat=52, lon=-3), zoom=5, mapbox_style="stamen-terrain")
   return fig.show()

fig = dens_map(red_data, 5)

import dash
import dash_core_components as dcc
from dash import html

app = dash.Dash()
app.layout = html.Div([
   dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
