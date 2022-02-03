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
            html.Div(className="container", children=[
                html.Div(className="two columns", children=[
                    html.H5("InfraGraph"),
                    html.P("The accident visualizer.")
                ]),
                html.Div(className="container ten columns", children=[
                    html.Div(className="three columns", children=[
                        html.P("Filter on the road type."),
                        dcc.Dropdown(
                            id="roadTypeSelector",
                            options=[
                                {'label': 'Roudabout', 'value': 1},
                                {'label': 'One way street', 'value': 2},
                                {'label': 'Dual carriageway', 'value': 3},
                                {'label': 'Single carriageway', 'value': 6},
                                {'label': 'Slip road', 'value': 7},
                                {'label': 'Unknown', 'value': 9},
                                {'label': 'One way street / Sliproad', 'value': 12}
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
                                {'label': 'Fine, no high winds', 'value': 1},
                                {'label': 'Raining, no high winds', 'value': 2},
                                {'label': 'Snowing, no high winds', 'value': 3},
                                {'label': 'Fine, high winds', 'value': 4},
                                {'label': 'Raining, high winds', 'value': 5},
                                {'label': 'Snowing, high winds', 'value': 6},
                                {'label': 'Fog or mist', 'value': 7},
                                {'label': 'Other', 'value': 8},
                                {'label': 'Unknown', 'value': 9}
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
                                {'label': 'Pedal cycle', 'value': 1},
                                {'label': 'Motorcycle <= 50cc', 'value': 2},
                                {'label': 'Motorcycle <=125cc', 'value': 3},
                                {'label': 'Motorcycle 125-500cc', 'value': 4},
                                {'label': 'Motorcycle >500cc', 'value': 5},
                                {'label': 'Taxi / Private Hired', 'value': 8},
                                {'label': 'Car', 'value': 9},
                                {'label': 'Minibus', 'value': 10},
                                {'label': 'Bus', 'value': 11},
                                {'label': 'Ridden Horse', 'value': 16},
                                {'label': 'Agricultural vehicle', 'value': 17},
                                {'label': 'Tram', 'value': 18},
                                {'label': 'Van', 'value': 19},
                                {'label': 'Goods >3.5t and <7.5t', 'value': 20},
                                {'label': 'Goods >7.5t', 'value': 21},
                                {'label': 'Mobility Scooter', 'value': 22},
                                {'label': 'Electric Motorcycle', 'value': 23},
                                {'label': 'Other', 'value': 90},
                                {'label': 'Motorcycle unknown cc', 'value': 97},
                                {'label': 'Goods vehicle unknown weight', 'value': 98},
                                {'label': 'Unknown vehicle type', 'value': 99}
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
                                {'label': 'Daylight', 'value': 1},
                                {'label': 'Darkness - lights lit', 'value': 4},
                                {'label': 'Darkness - lights unlit', 'value': 5},
                                {'label': 'Darkness - no lighting', 'value': 6},
                                {'label': 'Darkness - lighting unknown', 'value': 7}
                            ],
                            multi=True,
                            style={"max-height": "120px"}
                        )
                    ])
                ])
            ])

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
