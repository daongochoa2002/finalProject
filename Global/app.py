from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('haha.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['Measurement Year'].min(),
        df['Measurement Year'].max(),
        step=None,
        value=df['Measurement Year'].min(),
        marks={str(year): str(year) for year in df['Measurement Year'].unique()},
        id='year-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))


def update_figure(selected_year):
    filtered_df = df[df['Measurement Year'] == selected_year]

    fig = px.scatter(filtered_df, x="PM2.5 (μg/m3)", y="PM10 (μg/m3)",
                 size="NO2 (μg/m3)", color="WHO Region", hover_name="WHO Country Name",
                 log_x=True, size_max=60)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
