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
                value=year_selector[0]
            )
        ]
    )

def generate_vis_toggle():
    """

    :return: Returns the visualization toggle
    """
    return html.Div(
        children=[
            html.P("Toggle the side panel with this button."),
            html.Button(id="toggleSide", children="Toggle Side Vis")
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
                html.Div(className="four columns", children=[
                    html.P("Filter on the road type."),
                    dcc.Dropdown(
                        id="roadTypeSelector",
                        options=[
                            {'label': 'Roudabout', 'value': '1'},
                            {'label': 'One way street', 'value': '2'},
                            {'label': 'Dual carriageway', 'value': '3'},
                            {'label': 'Single carriageway', 'value': '6'},
                            {'label': 'Slip road', 'value': '7'},
                            {'label': 'Unknown', 'value': '9'},
                            {'label': 'One way street / Sliproad', 'value': '12'}
                        ],
                        value=['1'],
                        multi=True,
                        style={"max-height": "120px"}
                    )
                ]),
                html.Div(className="four columns", children=[
                    html.P("Filter on the weather condition."),
                    dcc.Dropdown(
                        id="weatherConditionSelector",
                        options=[
                            {'label': 'Fine, no high winds', 'value': '1'},
                            {'label': 'Raining, no high winds', 'value': '2'},
                            {'label': 'Snowing, no high winds', 'value': '3'},
                            {'label': 'Fine, high winds', 'value': '4'},
                            {'label': 'Raining, high winds', 'value': '5'},
                            {'label': 'Snowing, high winds', 'value': '6'},
                            {'label': 'Fog or mist', 'value': '7'},
                            {'label': 'Other', 'value': '8'},
                            {'label': 'Unknown', 'value': '9'}
                        ],
                        value=['1'],
                        multi=True,
                        style={"max-height": "120px"}
                    )
                ]),


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
