import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv('Premier League Player Stats.csv')
app = dash.Dash()

fig = px.bar(data, x="MIN", y="SHOTS")
app.layout = html.Div(children=[
    html.H1(children='Premier League Player Stat (Minute Played)'), 
    dcc.Dropdown(id='team-dropdown', 
                 options=[{'label': i, 'value': i}
                         for i in data['TEAM'].unique()],
                value='Manchester United'),
    dcc.Graph(id='player-graph')
])
@app.callback(
    Output(component_id='player-graph', component_property='figure'),
    Input(component_id='team-dropdown', component_property='value')
)
def update_graph(selected_team):
    filter_data = data[data['TEAM'] == selected_team]
    fig = go.Figure()
    line_fig = px.bar(filter_data, x='PLAYER', y='MIN')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)