from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


class AccidentsPerLightCondition(html.Div):

    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Amount of accidents per light condition"),
                dcc.Graph(figure=self.update(), id=self.html_id)
            ]
        )

    def update(self, selected_year=None):
        if selected_year is None:
            selected_year = self.df

        self.fig = px.histogram(selected_year, x='light_conditions')
        self.fig.update_layout(bargap=0.2)

        return self.fig