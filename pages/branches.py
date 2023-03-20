import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, callback
from pages.utility import branches_page_data_and_figures




dash.register_page(__name__, name='branches')


"""layout function for the branches page, the data manipulations is at the utility file. this function is for 
having the page graphs update on refresh or load in case of data change(down-side: reading the excel and making df's every page load)
we can define the layout as a variable and the layout will be static and wont change on load or reload"""
def layout():

    return dbc.Container([
                dbc.Row([
                    dbc.Col(
                        dbc.Button(html.Span("Back"),href='/',className="back-button"),width=1)
                ], align='end'),

                dbc.Row([
                    dbc.Col([html.H4("Branches"),html.Hr(className='colored-hr')],width=4)
                ],align="end"),

                dbc.Row([
                    dbc.Col(
                        dbc.Card(id='income_card',className="align-items-center justify-content-center"),
                    width=4,style={ 'margin-top': '160px'}),

                    dbc.Col([
                        html.H5('Market Share',style={'margin-left': '60px'}),
                        dcc.Graph(id='branches-pie-chart',figure=branches_page_data_and_figures('pie_chart_figure'))],
                    width=5)
                ],justify='around',style={'margin-top': '80px'})
            ],className="page-container")



"""callback function that update the pie-chart colors by clicking on a slice the function 
will update the card info for the clicked slice branch income, and return it to total income when no slice is toggeled"""
@callback(
    Output('branches-pie-chart', 'figure'),
    Output('income_card', 'children'),
    Input('branches-pie-chart', 'clickData'),
    State('branches-pie-chart', 'figure')
)
def update_pie_chart(clickData, figure):
    if clickData is None:
        colors = ['#1f77b4'] * len(figure['data'][0]['values'])
        return figure,dbc.CardBody([html.H2(f"{branches_page_data_and_figures('total_income')}$"),html.H6("Total profit")])


    else:
        colors = []
        for i, val in enumerate(figure['data'][0]['values']):
            if figure['data'][0]['labels'][i] == clickData['points'][0]['label'] and figure['data'][0]['marker']['colors'][i]=='#0CAFFF':
                figure['data'][0]['marker']['colors'] = ['#1f77b4'] * len(figure['data'][0]['values'])
                return figure,dbc.CardBody([html.H2(f"{branches_page_data_and_figures('total_income')}$"),html.H6("Total profit")])


            if figure['data'][0]['labels'][i] == clickData['points'][0]['label']:
                colors.append('#0CAFFF')
            else:
                colors.append('#636363')

    # Update the figure with the new marker colors and return it
    figure['data'][0]['marker']['colors'] = colors
    return figure,dbc.CardBody(html.H2(f"Branch {clickData['points'][0]['label']} Income: {clickData['points'][0]['value']}$"))




