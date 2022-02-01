from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


class Map(html.Div):

    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")
        px.set_mapbox_access_token("pk.eyJ1IjoiaW1wYWV4IiwiYSI6ImNreXZseGtxeTAyeWoydnFsb2pmODZmZHUifQ.B-5SHypoZaj2Mu47_suE6Q")

        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Interactive Map of Accidents"),
                dcc.Graph(figure=self.update())
            ]
        )

    def update(self):
        #df1 = self.df[self.df['accident_year'] == 2020]
        self.fig = px.scatter_mapbox(self.df,
                lat="latitude",
                lon="longitude",
                hover_name="accident_index",
                hover_data=["date", "time", "vehicle_type", "casualty_type", "vehicle_manoeuvre",
                            "road_surface_conditions", "light_conditions", "speed_limit"],

                color='accident_severity',
                color_discrete_sequence=['darkblue', 'blue', 'lightblue'],

                zoom=4,
                height=700,
                custom_data=[self.df['accident_index'], self.df['date'], self.df['latitude'], self.df['longitude'],
                             self.df['speed_limit'], self.df['vehicle_type'], self.df['road_surface_conditions'],
                             self.df['vehicle_manoeuvre'], self.df['accident_severity'], self.df['light_conditions'],
                             self.df['hour']]
                )
        self.fig.update_traces(hovertemplate=
                            '<b>Accident %{customdata[0]}</b><br>' +
                            '<br>' +
                            'Date: <i>%{customdata[1]}</i><br>' +
                            'Lat / Lon: <i>%{customdata[2]} / %{customdata[3]}</i><br>' +
                            'Speed limit: <i>%{customdata[4]}</i><br>' +
                            'Vehicle Type: <i>%{customdata[5]}</i><br>' +
                            'Road Surface Condition: <i>%{customdata[6]}</i><br>' +
                            'Vehicle Manoeuvre: <i>%{customdata[7]}</i><br>' +
                            'Severity: <i>%{customdata[8]}</i><br>' +
                            'Light Condition: <i>%{customdata[9]}</i><br>'
                               )

        self.fig.update_layout(mapbox_style="dark",
                               margin={"r": 0, "t": 0, "l": 0, "b": 0},
                               title_x=0.5,
                               title_y=0.95,
                               title_font_color="black"
                               )

        return self.fig