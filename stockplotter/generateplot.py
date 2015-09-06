from bokeh.plotting import figure
from bokeh.charts import TimeSeries
from bokeh.embed import components
import pandas as pd


def generateplot(data, desired_columns, stock):
    
    note = ""
    if len(desired_columns)==0:
        desired_columns = ['Close']
        note = "Please selected mentioned ticker!"

    desired_columns.append('Date')
    plot = TimeSeries(data.loc[:,desired_columns],index='Date',legend=True,title=stock)
    script, div = components(plot)  
    return script, div, note
