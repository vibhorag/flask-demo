import requests
import datetime
import pandas as pd
import numpy as np

def getstockdata(stock):
    url_link = "https://www.quandl.com/api/v3/datasets/WIKI"

    today     = datetime.date.today()    
    startdate = today - datetime.timedelta(30)

    quandl_api = "%s/%s.json?start_date=%s&end_date=%s"%(url_link,stock,startdate,today)
    
    print quandl_api
    
    # Grab the data from Quandl 
    r = requests.get(quandl_api)

    # Loading of  data into a pandas dataframe to trim the need of the API 
    df_first = pd.read_json(r.text)['dataset']
    df_final  = pd.DataFrame(df_first['data'],columns=df_first['column_names'])
    df_final['Date'] = pd.to_datetime(df_final['Date'])

    return df_final.loc[:,['Date','Close','Adj. Close','Volume']]


if __name__=="__main__":


    stock = "GOOG"
    df_final = getstockdata(stock)
    import IPython
    IPython.embed()
