from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout, generate_year_selector, generate_vis_toggle, generate_buttons

from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.map import Map
from jbi100_app.views.accidents_per_hour_of_day import AccidentsPerHour
from jbi100_app.views.accidents_per_vehicle_type import AccidentsPerVehicleType
from jbi100_app.views.accidents_per_light_condition import AccidentsPerLightCondition
from jbi100_app.views.accidents_per_day_of_week import AccidentPerDayOfWeek
from jbi100_app.data import get_data

from dash import html
import plotly.express as px
from dash.dependencies import Input, Output

# code derived from template
if __name__ == '__main__':
    # Create data
    df = get_data()

    map = Map("Map Of Accidents", df)
    accidentsperhour = AccidentsPerHour("Histogram Of Accidents Per Hour", df)
    accidentspertype = AccidentsPerVehicleType("Histogram Of Accidents Per Hour", df)
    accidentsperlight = AccidentsPerLightCondition("Histogram of accidents per light condition", df)
    accidentsperweek = AccidentPerDayOfWeek("Histogram Of Accidents Per Week", df)

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
                className="six columns",
                children=map
            ),

            # Middle column
            html.Div(
                id="middle-column",
                className="three columns",
                children=[
                    accidentspertype,
                    accidentsperlight
                ]
            ),

            # Right column
            html.Div(
                id="right-column",
                className="three columns",
                children=[
                    accidentsperhour,
                    accidentsperweek
                ],
            ),
        ],
    )

    # Define interactions
    # Map interaction
    @app.callback(Output(map.html_id, "figure"),
                  Output(accidentsperlight.html_id, "figure"),
                  Output(accidentspertype.html_id, "figure"),
                  Input('yearSelector', 'value'),
                  Input('roadTypeSelector', 'value'),
                  Input('weatherConditionSelector', 'value'),
                  Input('vehicleTypeSelector', 'value'),
                  Input('lightConditionSelector', 'value'),
                  Input(map.html_id, 'selectedData')
                  )
    def year_selector(year, roadtype, weathercond, vehicletype, lightcond, sel_data):
        temp = df[df.accident_year == year]
        if roadtype is not None:
            if len(roadtype) > 0:
                temp = temp[temp.road_type.isin(roadtype)]
            else:
                temp = temp[temp.road_type.isin(df.road_type.unique())]

        # If it is none, it has not been interacted with yet, no need to do anything.
        if weathercond is not None:
            if len(weathercond) > 0:
                temp = temp[temp.weather_conditions.isin(weathercond)]
            else:
                # Resets this field with original values of df
                temp = temp[temp.weather_conditions.isin(df.weather_conditions.unique())]

        if vehicletype is not None:
            if len(vehicletype) > 0:
                temp = temp[temp.vehicle_type.isin(vehicletype)]
            else:
                temp = temp[temp.vehicle_type.isin(df.vehicle_type.unique())]

        if lightcond is not None:
            if len(lightcond) > 0:
                temp = temp[temp.light_conditions.isin(lightcond)]
            else:
                temp = temp[temp.light_conditions.isin(df.light_conditions.unique())]

        if sel_data is not None:
            selected_index = [x['customdata'][0] for x in sel_data['points']]
            temp = temp[temp.accident_index.isin(selected_index)]

        return map.update(selected_year=temp),  accidentsperlight.update(selected_year=temp), accidentspertype.update(selected_year=temp)


    app.run_server(debug=False, dev_tools_ui=False)