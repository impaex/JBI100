from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


class Map(html.Div):

    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Interactive Map of Accidents"),
                dcc.Graph(figure=self.update())
            ]
        )

    def update(self):
        self.fig = px.scatter_mapbox(self.df,
                lat="latitude",
                lon="longitude",
                hover_name="accident_index",
                hover_data=["date", "time", "vehicle_type", "casualty_type", "vehicle_manoeuvre",
                            "road_surface_conditions", "light_conditions", "speed_limit"],
                color='accident_severity', color_continuous_scale=['red', 'yellow', 'lime'],
                zoom=4,
                height=800
                )
        self.fig.update_layout(mapbox_style="open-street-map")
        self.fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        self.fig.update_layout(title_x=0.5, title_y=0.95, title_font_color="black")

        return self.fig