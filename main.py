from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()


df = pd.read_csv('./data/clean_data.csv')
df.index = df['date'] # sort by date


fig = px.line(
    data_frame=df,
    x='date',
    y='sales'
)


app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales', 
        style={'textAlign': 'center'}
    ),
    dcc.Graph(id='example-graph', figure=fig),
])

if __name__ == '__main__':
    app.run(debug=True)