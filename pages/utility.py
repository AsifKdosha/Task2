"""this file is utility functions for data and figures reading and manipulating for efficiency and order """
import pandas as pd
import plotly.express as px

#for sorting by month
month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}


"""function for making the base df with sales (quantity*unit price), used by other function for avoiding code duplication"""
def make_sales_main_df():
    #every sale is (quatity * unit price)
    df = pd.read_excel('pages/data/DB.xlsx', engine='openpyxl', parse_dates=['Date'])

    # making a DF with total sale price (quatity * unit price) and the month of the deal and the branch
    sales_df=pd.DataFrame({'Month': df['Date'].dt.month_name(), 'Income': df['Unit price'] * df['Quantity'], 'Branch': df['Branch']})
    sales_df.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
    return sales_df


"""function that return the relevant data for the index page bar chart
(if we needed more data or figures options we could add request like in the next function)"""
def index_page_data_and_figures():
    monthly_sales_df=make_sales_main_df().groupby('Month').agg(Income=('Income', 'sum'))
    sorted_monthly_df=monthly_sales_df.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
    # making a figur by making a DF with monthly income for every month
    return px.bar(sorted_monthly_df,y='Income',text_auto=True)




"""function that return the relevant data by request (arg 'request') for the 
branches page"""
def branches_page_data_and_figures(request):

    sales_df=make_sales_main_df()

    if request=='total_income':
        return sales_df['Income'].sum()

    if request=='pie_chart_figure':
        fig = px.pie(sales_df.groupby('Branch', as_index=False).agg(Income=('Income', 'sum')).groupby('Branch', as_index=False).agg(Income=('Income', 'sum')),
            values='Income',
            names='Branch', height=400)

        fig.update_traces(textposition='inside', textinfo='label', texttemplate='%{label}',
                          marker={'colors': ['#1f77b4'] * len(fig.data[0].values), 'line': {'width': 2}})
        return fig

