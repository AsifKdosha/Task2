import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

"""this function define the layout of the app,contaning the 'dash.page_container' that
bring the layout from the pages we created (using 'dash pages') format."""
def serve_layout():
	return dbc.Container([
		html.Div( className="app-header",children= [html.H1("Focuse Sales")]),
		dash.page_container,
		html.Div( className="app-footer")

	],className="page-container")



app.layout = serve_layout




if __name__ == '__main__':
	app.run_server(debug=True)