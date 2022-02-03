from dash import dcc, html
from ..config import year_selector, color_list2, color_list1


def generate_year_selector():
    """

    :return: the year selector content.
    """
    return html.Div(
        children=[
            html.P("Choose a year which you want to visualize."),
            dcc.Dropdown(
                id="yearSelector",
                options=[{"label": x, "value": x} for x in year_selector],
                value=year_selector[0],
                clearable=False
            )
        ]
    )

def generate_vis_toggle():
    """

    :return: Returns the visualization toggle
    """
    return html.Div(
        children=[
            html.P("Toggle the yearly plots with this button."),
            html.Button(id="toggleSide", children="Toggle Yearly")
        ]
    )

def generate_buttons():
    """

    :return: the buttons used for the visualization
    """
    return html.Div(
        children=[
            html.Div(className="container remove-margin", children=[
                html.Div(className="two columns", children=[
                    html.H5("InfraGraph"),
                    html.P("The accident visualizer."),
                ]),
                html.Div(className="container ten columns", children=[
                    html.Div(className="three columns", children=[
                        html.P("Filter on the road type."),
                        dcc.Dropdown(
                            id="roadTypeSelector",
                            options=[
                                {'label': 'Roudabout', 'value': 'Roudabout'},
                                {'label': 'One way street', 'value': 'One way street'},
                                {'label': 'Dual carriageway', 'value': 'Dual carriageway'},
                                {'label': 'Single carriageway', 'value': 'Single carriageway'},
                                {'label': 'Slip road', 'value': 'Slip road'},
                                {'label': 'Unknown', 'value': 'Unknown'},
                                {'label': 'One way street / Sliproad', 'value': 'One way street / Sliproad'}
                            ],
                            multi=True,
                            style={"max-height": "120px"}
                        )
                    ]),
                    html.Div(className="three columns", children=[
                        html.P("Filter on the weather condition."),
                        dcc.Dropdown(
                            id="weatherConditionSelector",
                            options=[
                                {'label': 'Fine, no high winds', 'value': 'Fine, no high winds'},
                                {'label': 'Raining, no high winds', 'value': 'Raining, no high winds'},
                                {'label': 'Snowing, no high winds', 'value': 'Snowing, no high winds'},
                                {'label': 'Fine, high winds', 'value': 'Fine, high winds'},
                                {'label': 'Raining, high winds', 'value': 'Raining, high winds'},
                                {'label': 'Snowing, high winds', 'value': 'Snowing, high winds'},
                                {'label': 'Fog or mist', 'value': 'Fog or mist'},
                                {'label': 'Other', 'value': 'Other'},
                                {'label': 'Unknown', 'value': 'Unknown'}
                            ],
                            multi=True,
                            style={"max-height": "120px"}
                        )
                    ]),
                    html.Div(className="three columns", children=[
                        html.P("Filter on the vehicle type."),
                        dcc.Dropdown(
                            id="vehicleTypeSelector",
                            options=[
                                {'label': 'Pedal cycle', 'value': 'Pedal cycle'},
                                {'label': 'Motorcycle <= 50cc', 'value': 'Motorcycle <= 50cc'},
                                {'label': 'Motorcycle <=125cc', 'value': 'Motorcycle <=125cc'},
                                {'label': 'Motorcycle 125-500cc', 'value': 'Motorcycle 125-500cc'},
                                {'label': 'Motorcycle >500cc', 'value': 'Motorcycle >500cc'},
                                {'label': 'Taxi / Private Hired', 'value': 'Taxi / Private Hired'},
                                {'label': 'Car', 'value': 'Car'},
                                {'label': 'Minibus', 'value': 'Minibus'},
                                {'label': 'Bus', 'value': 'Bus'},
                                {'label': 'Ridden Horse', 'value': 'Ridden Horse'},
                                {'label': 'Agricultural vehicle', 'value': 'Agricultural vehicle'},
                                {'label': 'Tram', 'value': 'Tram'},
                                {'label': 'Van', 'value': 'Van'},
                                {'label': 'Goods >3.5t and <7.5t', 'value': 'Goods >3.5t and <7.5t'},
                                {'label': 'Goods >7.5t', 'value': 'Goods >7.5t'},
                                {'label': 'Mobility Scooter', 'value': 'Mobility Scooter'},
                                {'label': 'Electric Motorcycle', 'value': 'Electric Motorcycle'},
                                {'label': 'Other', 'value': 'Other'},
                                {'label': 'Motorcycle unknown cc', 'value': 'Motorcycle unknown cc'},
                                {'label': 'Goods vehicle unknown weight', 'value': 'Goods vehicle unknown weight'},
                                {'label': 'Unknown vehicle type', 'value': 'Unknown vehicle type'}
                            ],
                            multi=True,
                            style={"max-height": "120px"}
                        )
                    ]),
                    html.Div(className="three columns", children=[
                        html.P("Filter on light condition."),
                        dcc.Dropdown(
                            id="lightConditionSelector",
                            options=[
                                {'label': 'Daylight', 'value': 'Daylight'},
                                {'label': 'Darkness - lights lit', 'value': 'Darkness - lights lit'},
                                {'label': 'Darkness - lights unlit', 'value': 'Darkness - lights unlit'},
                                {'label': 'Darkness - no lighting', 'value': 'Darkness - no lighting'},
                                {'label': 'Darkness - lighting unknown', 'value': 'Darkness - lighting unknown'}
                            ],
                            multi=True,
                            style={"max-height": "120px"}
                        )
                    ])
                ])
            ]),
            html.P("If no graphs are visible, there's no data for the given filters.")

        ]
    )

def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Example dashboard"),
            html.Div(
                id="intro",
                children="You can use this as a basic template for your JBI100 visualization project.",
            ),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.Label("Color scatterplot 1"),
            dcc.Dropdown(
                id="select-color-scatter-1",
                options=[{"label": i, "value": i} for i in color_list1],
                value=color_list1[0],
            ),
            html.Br(),
            html.Label("Color scatterplot 2"),
            dcc.Dropdown(
                id="select-color-scatter-2",
                options=[{"label": i, "value": i} for i in color_list2],
                value=color_list2[0],
            ),
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
