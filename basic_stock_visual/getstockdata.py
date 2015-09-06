import pandas as pd
import numpy as np
import requests
import simplejson as json
import datetime
def getstockdata(stock):    
    today     = datetime.date.today()
    
    startdate = today - datetime.timedelta(30)
    
    quandl_url = "https://www.quandl.com/api/v3/datasets/WIKI"
    quandl_api_request = "%s/%s.json?start_date=%s&end_date=%s"%(quandl_url,stock,startdate,today)
    
    re = requests.get(quandl_api_request)
    
    data_set1 = pd.read_json(re.content)["dataset"]
    
    dataset_final = pd.DataFrame(data =data_set1["data"],columns=data_set1["column_names"])
    
    dataset_final["Date"] = pd.to_datetime(dataset_final["Date"])
    
    dataset_final_plot = dataset_final.loc[:,['Date','Close','Adj. Close','Volume']]
    
    
    return dataset_final_plot
    
if __name__=="__main__":


    stock = "GOOG"
    df = getstockdata(stock)
    import IPython
    IPython.embed()