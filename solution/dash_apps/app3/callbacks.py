from dash.dependencies import Input, Output

from app import dash_app
from ..visualization_data import people_class, gapminder

@dash_app.callback(
    Output('gap-with-slider', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_year):
    filtered_df = gapminder[gapminder.year == selected_year]
    traces = []
    for ucontinent in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == ucontinent]
        traces.append(dict(
            x = df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=.7,
            marker = {
                'size': 15,
                'line': {"width": .5, "color": 'white'}
                },
            name=ucontinent
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita',
                   'range': [2.3, 4.8]},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode="closest",
            transition={"duration": 500}
        )
    }

# @dash_app.callback(
#     Output('table', 'data'),
#     [Input('table', "page_current"),
#      Input('table', "page_size")]
# )
# def update_table(page_current, page_size):
#     return df.iloc[page_current*page_size : (page_current + 1) * page_size].to_dict('records')