from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Template from course template
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

    # Code derived from plotly docs
    def update(self, selected_year=None, selected_data=None):
        if selected_year is None:
            selected_year = self.df

        if selected_data is not None:
            selected_index = [  # show only selected indices
                x['customdata'][0]
                for x in selected_data['points']
            ]

            selected_year = selected_year[selected_year.accident_index.isin(selected_index)]

        self.fig = px.histogram(selected_year, x='light_conditions', labels={"light_conditions": "Light Condition"})
        self.fig.update_layout(bargap=0.2)

        return self.fig