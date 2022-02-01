from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout, generate_year_selector, generate_vis_toggle, generate_buttons

from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.map import Map
from jbi100_app.views.accidents_per_hour_of_day import AccidentsPerHour
from jbi100_app.views.accidents_per_vehicle_type import AccidentsPerVehicleType
from jbi100_app.views.accidents_per_day_of_year import AccidentPerDayOfYear
from jbi100_app.data import get_data

from dash import html
import plotly.express as px
from dash.dependencies import Input, Output


if __name__ == '__main__':
    # Create data
    df = get_data()

    map = Map("Map Of Accidents", df)
    accidentsperhour = AccidentsPerHour("Histogram Of Accidents Per Hour", df)
    accidentspertype = AccidentsPerVehicleType("Histogram Of Accidents Per Hour", df)
    #accidentsperday = AccidentPerDayOfYear("Line Chart Of Accidents Per Day Per Year", df)

    app.layout = html.Div(
        id="app-container",
        children=[
            html.Div(
                id="topRow",
                className="container",
                children=[html.Div(id="left-title", className="two columns border-right", children=generate_year_selector()),
                          html.Div(className="eight columns", children=generate_buttons()),
                          html.Div(id="right-title", className="two columns", children=generate_vis_toggle())]
            ),

            # Left column
            html.Div(
                id="left-column",
                className="nine columns",
                children=map
            ),

            # Right column
            html.Div(
                id="right-column",
                className="three columns",
                children=[
                    accidentsperhour,
                    accidentspertype,
                    #accidentsperday
                ],
            ),
        ],
    )

    # Define interactions
    # @app.callback(
    #     Output(scatterplot1.html_id, "figure"), [
    #     Input("select-color-scatter-1", "value"),
    #     Input(scatterplot2.html_id, 'selectedData')
    # ])
    # def update_scatter_1(selected_color, selected_data):
    #     return scatterplot1.update(selected_color, selected_data)
    #
    # @app.callback(
    #     Output(scatterplot2.html_id, "figure"), [
    #     Input("select-color-scatter-2", "value"),
    #     Input(scatterplot1.html_id, 'selectedData')
    # ])
    # def update_scatter_2(selected_color, selected_data):
    #     return scatterplot2.update(selected_color, selected_data)


    app.run_server(debug=False, dev_tools_ui=False)