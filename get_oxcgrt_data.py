#!/usr/bin/env python
# coding: utf-8
# PROJECT USED

import numpy as np
import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
from datetime import datetime,timedelta
import time


def get_oxcgrt_data(date_start,date_end):
    start = datetime.strptime(str(date_start),"%Y%m%d")
    end = datetime.strptime(str(date_end),"%Y%m%d")
    day = timedelta(days=1)
    mydate = start
    date_list = []
    while mydate <= end:
        newdate = mydate.strftime("%Y-%m-%d")
        date_list.append(newdate)
        mydate += day
    #print(date_list)
    
    # fetch data from official website
    response = requests.get(f"https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/{date_start}/{date_end}").text
    jsonData = json.loads(response)
    record = pd.json_normalize(jsonData["data"],errors='ignore')
    oxcgrt = []
    

    for i in date_list:
        x = i + ".TWN" + ".stringency_actual"
        if x in record.columns :
            oxcgrt.append(record[x].values[0])
        else:
            oxcgrt.append(0)
            
    df = pd.DataFrame({'date':date_list,'stringency_actual':oxcgrt})
    print(oxcgrt)
    
    #record = pd.json_normalize(jsonData,record_path='countries',meta=[['data',f'{new_start}','TWN','stringency_actual']],errors='ignore')
    #record = pd.json_normalize(jsonData[f"{new_start}"],record_path="TWN",errors='ignore')
    # filed = ["date_value","stringency_actual"]
    # df[filed].to_csv('oxcgrt_day.csv', index = False)
    df.to_csv('oxcgrt_day.csv', index = False,na_rep=0)
        
    

    
    

def get_data(date_start,date_end):
    
    # get oxcgrt data
    get_oxcgrt_data(date_start,date_end)

get_data(20210901,20211222)