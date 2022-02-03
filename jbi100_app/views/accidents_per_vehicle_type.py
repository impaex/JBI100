from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Template from course template
class AccidentsPerVehicleType(html.Div):

    # Rest of code derived from course template.
    def __init__(self, name, df):
        self.df = df
        # Given that the name of the map represents the ID of the node.
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            children=[
                html.H6("Amount of accidents per vehicle type"),
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

        selected_yearx = selected_year[['vehicle_type', 'accident_index']].groupby('vehicle_type')['accident_index'].count().reset_index(
            name='Count').sort_values(['Count'], ascending=False).head(10)
        self.fig = px.bar(selected_yearx, x='vehicle_type', y='Count', color="vehicle_type", labels={"vehicle_type": "Vehicle Type"})
        self.fig.update_layout(bargap=0.2)
        self.fig.update_xaxes(showticklabels=False)

        return self.fig