import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from pages.utility import index_page_data_and_figures

dash.register_page(__name__, path='/')


"""layout function for the index page, the data manipulations is at the utility file. this function is for 
having the page graphs update on refresh or load in case of data change(down-side: reading the excel and making df's every page load)
we can define the layout as a variable and the layout will be static and wont change on load or reload"""
def layout():

    return dbc.Container([
        dbc.Row([
            dbc.Col([html.H4('Total profit per month',style={'margin-top': '15px'}),html.Hr(className='colored-hr')],width=4)
        ]),

        dbc.Row([
                dbc.Col(
                    html.Div(dcc.Graph(id='monthly_sales',figure=index_page_data_and_figures()),style={"border": "1px solid black"})
                    ,width=7,
                ),

                dbc.Col(dbc.Button(className='button-85',children="Branches", href='/branches'),width={'offset': 3}),
        ],align='end',style={'margin-top': '80px'})
    ],className="page-container")

