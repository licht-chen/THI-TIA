# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:52:44 2021

@author: licht0104
"""

import pandas as pd
import simpledbf

def road_clean(input_path, output_path, data_name):
    ## shapefile dbf 資料欄位篩選
    # use simpledbf read .dbf data and converse .dbf to dataframe()
    df = simpledbf.Dbf5("G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\GIS\\Shapefile\\縣市道路資訊\\TW_ROAD_done.dbf",codec='utf8').to_dataframe()
    data = pd.DataFrame()
    data['ID'] = df.index + 1
    data['ROADCLASS1'] = df['ROADCLASS1']
    data['COUNTY'] = df['COUNTY']
    data['ROADNUM'] = df['ROADNUM']
    data['ROADNUM1'] = df['ROADNUM1']
    data['ROADNUM2'] = df['ROADNUM2']
    data['ROADNAME'] = df['ROADNAME']
    data['WIDTH'] = df['WIDTH']
    position = []
    # asign lon and lat data
    for i in range(df.shape[0]):
        position.append([ df.loc[i,'From_Lat'], df.loc[i,'To_Lat']])
    data['PositionLat'] = position
    position = []
    for i in range(df.shape[0]):
        position.append([ df.loc[i,'From_Long'], df.loc[i,'To_Long']])
    data['PositionLon'] = position
    # output
    data.to_csv(output_path + "ROAD.csv",encoding='utf8',index=None)
    data.to_csv(output_path + "ROAD_ANSI.csv",encoding='ANSI',index=None)
    
input_path = "G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\GIS\\Shapefile\\縣市道路資訊\\"
output_path = "G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\GIS\\Shapefile\\縣市道路資訊\\"
data_name = "TW_ROAD_done.dbf"

road_clean(input_path, output_path, data_name)