from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


class AccidentsPerHour(html.Div):

    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Average amount of accidents per hour of the day"),
                dcc.Graph(figure=self.update())
            ]
        )

    def update(self):
        self.fig = px.histogram(self.df, x='hour')
        self.fig.update_layout(bargap=0.2)

        return self.fig