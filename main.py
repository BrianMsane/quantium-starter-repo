from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)
df = pd.read_csv('./data/clean_data.csv').sort_values(by='date')


app.layout = html.Div(style={
        'backgroundColor': '#f4f7f6', 
        'fontFamily': 'Arial, sans-serif', 
        'padding': '40px',
        'minHeight': '100vh'
    }, 
    children=[
        html.H1(
            children='Pink Morsel Sales Visualiser', 
            style={
                    'textAlign': 'center', 
                    'color': '#2c3e50',
                    'marginBottom': '30px',
                    'fontWeight': 'bold'
                }
    ),

    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '15px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            inputStyle={"margin-left": "20px", "margin-right": "5px"}
        )
    ], style={
        'textAlign': 'center', 
        'backgroundColor': 'white', 
        'padding': '20px', 
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
        'marginBottom': '30px'
    }),

    html.Div(
        [dcc.Graph(id='sales-line-chart')], 
        style={
            'backgroundColor': 'white', 
            'padding': '10px', 
            'borderRadius': '10px',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
        }
    ),
])

# Callback to update the graph based on radio button selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title=f"Sales Trend: {selected_region.capitalize()}",
        template="plotly_white"
    )

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 50, 'r': 0},
        hovermode='closest',
        transition_duration=500
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
