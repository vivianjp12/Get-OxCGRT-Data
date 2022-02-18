#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
import datetime
from datetime import timedelta


def get_oxcgrt_data(date_start,date_end):
    start = datetime.datetime.strptime(str(date_start),"%Y%m%d")
    end = datetime.datetime.strptime(str(date_end),"%Y%m%d")
    day = timedelta(days=1)
    mydate = start
    df = pd.DataFrame()
    while mydate <= end:
    # fetch data from official website
        response = requests.get(f"https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/actions/TWN/{mydate}").text
        jsonData = json.loads(response)
        record = pd.json_normalize(jsonData["stringencyData"],errors='ignore')
        df = df.append(record)
        mydate += day
    filed = ["date_value","stringency_actual"]
    df[filed].to_csv('oxcgrt_day.csv', index = False)
        
    

    
    

def get_data(date_start,date_end):
    
    # get oxcgrt data
    get_oxcgrt_data(date_start,date_end)

get_data(20211201,20211222)