from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


class AccidentPerDayOfYear(html.Div):

    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")

        self.new_df = self.df.groupby(['accident_year', 'day_of_year']).size()
        print(self.new_df.head())
        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Amount of accidents per day of the year"),
                dcc.Graph(figure=self.update())
            ]
        )

    def update(self):

        self.fig = px.line(self.new_df, x='day_of_year', color='accident_year')
        self.fig.update_layout(bargap=0.2)

        return self.fig