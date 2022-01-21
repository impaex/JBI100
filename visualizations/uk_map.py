import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os

data = pd.read_csv(os.path.join(os.path.dirname(__file__), '../dataset/cleaned_data.csv'))

#reducing data for faster loading time
red_data = data[data["accident_year"] == 2015]

def uk_map(df, name):
   data1 = df
   data1 = data1[(data1['longitude'] != '?') & (data1['latitude'] != '?')].copy()

   data1['longitude'] = pd.to_numeric(data1['longitude'])
   data1['latitude'] = pd.to_numeric(data1['latitude'])

   fig = px.scatter_mapbox(data1, lat="latitude", lon="longitude", title=name, hover_name="accident_index",
                           hover_data=["date", "time", "vehicle_type", "casualty_type", "vehicle_manoeuvre",
                                       "road_surface_conditions", "light_conditions", "speed_limit"],
                           color='accident_severity', color_continuous_scale=['red', 'yellow', 'lime'], zoom=4,
                           height=600)
   fig.update_layout(mapbox_style="open-street-map")
   fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
   fig.update_layout(title_x=0.5, title_y=0.95, title_font_color="black")

   return fig.show()

fig = uk_map(red_data, "Map of road accidents in the UK from 2000 until 2020")

import dash
import dash_core_components as dcc
from dash import html

app = dash.Dash()
app.layout = html.Div([
   dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
