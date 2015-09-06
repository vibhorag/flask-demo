from bokeh.plotting import figure
import pandas as pd
from bokeh.charts import TimeSeries
from bokeh.embed import components

def plot_generate(data,check_columns,stock):
    
    note = ""
    if len(check_columns)==0:
        desired_columns = ['Close']
        note = "NOTE: No desired features selected!"
    
    check_columns.append("Date")
    p = TimeSeries(data.loc[:,check_columns],index='Date',legend=True,title=stock, ylabel='Stock Prices')
    
    script, div = components(p)  
    return script, div, note