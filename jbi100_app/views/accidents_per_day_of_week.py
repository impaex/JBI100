from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Template from course template
class AccidentPerDayOfWeek(html.Div):

    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Amount of accidents per day of the week"),
                dcc.Graph(figure=self.update())
            ]
        )

    def update(self):
        # Code derived from plotly docs
        self.fig = px.histogram(self.df, x='weekday', color='accident_severity', labels={"accident_severity": "Severity"}, color_discrete_sequence=['darkblue', 'blue', '#00A1E4'])
        self.fig.update_layout(bargap=0.2)

        return self.fig