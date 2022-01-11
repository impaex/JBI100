import pandas as pd

data = pd.read_csv(r"C:\Users\20202478\Documents\School\Year 2\Q2\JBI100 Visualization\Visualization_full.csv")

#reduced data to make loading faster
red_data = data

def d_o_w(df):
   data3 = df[['day_of_week']].copy()
   cnt_data3 = data3['day_of_week'].value_counts()

   cnt_data3 = cnt_data3.sort_index()
   cnt_data3.rename(
       index={1: 'Sunday', 2: 'Monday', 3: 'Teusday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'},
       inplace=True)
   return cnt_data3.plot(kind='bar')

fig = d_o_w(red_data)

import dash
import dash_core_components as dcc
from dash import html

app = dash.Dash()
app.layout = html.Div([
   dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
