# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:58:50 2021

@author: licht0104
"""

import shapefile as shp
import pandas as pd
import math
# import simpledbf
# data = pd.read_csv("G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\Output Data\\Gis\\C000_府中美學\\gis_sidewalk.csv", encoding='ANSI')
# output_path = "G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\Output Data\\Gis\\C000_府中美學"

def sidewalk_to_shp(data, output_path, shp_name):
    shp_name = 'sidewalk_shp'
    df = data
    check = {}
    for i in pd.unique(df['name']):
        check[i] = 0
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=3,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('city','C',size=255)
    w.field('area','C',size=255)
    w.field('name','C',size=255)
    w.field('start','C',size=255)
    w.field('end','C',size=255)
    w.field('direction','C',size=255)
    w.field('totalwidth','C',size=255)
    w.field('walkwidth','C',size=255)
    w.field('ramp','C',size=255)
    w.field('geometry','C',size=255)
    for i in range(df.shape[0]):        
        lon = df.loc[i,'PositionLon'].split('[')[1].split(']')[0].split(', ')
        lat = df.loc[i,'PositionLat'].split('[')[1].split(']')[0].split(', ')
        ## shapefile-> 線性資料設定
        a = []
        for j in range(len(lon)):
            a.append([float(lon[j]) , float(lat[j]) ])
        ## 數據轉換為shapefile 線性圖像
        w.line([a])
        if check[df.loc[i,'name']] <1:
            if ('街' in df.loc[i,'name']) or ('巷' in df.loc[i,'name']) or ('無' in df.loc[i,'name']):
                w.record(number=df.loc[i,'Number'], city=df.loc[i,'city'], area=df.loc[i,'area'], name="", start=df.loc[i,'start'], 
                         end=df.loc[i,'end'], direction=df.loc[i,'direction'], totalwidth=df.loc[i,'totalwidth'], walkwidth=df.loc[i,'walkwidth'], 
                         ramp=df.loc[i,'ramp'], geometry=df.loc[i,'geometry'])
            else:
                w.record(number=df.loc[i,'Number'], city=df.loc[i,'city'], area=df.loc[i,'area'], name=df.loc[i,'name'], start=df.loc[i,'start'], 
                         end=df.loc[i,'end'], direction=df.loc[i,'direction'], totalwidth=df.loc[i,'totalwidth'], walkwidth=df.loc[i,'walkwidth'], 
                         ramp=df.loc[i,'ramp'], geometry=df.loc[i,'geometry'])
            check[df.loc[i,'name']] = check[df.loc[i,'name']]+1
        else:
            w.record(number=df.loc[i,'Number'], city=df.loc[i,'city'], area=df.loc[i,'area'], name="", start=df.loc[i,'start'], 
                end=df.loc[i,'end'], direction=df.loc[i,'direction'], totalwidth=df.loc[i,'totalwidth'], walkwidth=df.loc[i,'walkwidth'], 
                ramp=df.loc[i,'ramp'], geometry=df.loc[i,'geometry'])
    w.close()

# data = pd.read_csv("G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\GIS\\Shapefile\\縣市道路資訊\\ROAD.csv",encoding='utf8')
output_path = "G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\Output Data\\Gis\\C000_府中美學"
def road_to_shp(data, output_path, shp_name):
    # base_coordinate = {'府中站': [25.00853207650213, 121.45942177851646],
    #                     '市民廣場': [25.01234076405166, 121.46571388726626]}
    # df = dist_cal_road(data, base_coordinate['府中站'], 500, 'PositionLat', 'PositionLon', '新北','COUNTY')
    # df = df.reset_index().drop(['index'],axis=1)
    # shp_name = 'road_shp'
    df = data
    # 道路出現次數變數
    check = {}
    for i in pd.unique(df['ROADNAME']):
        if i == None:
            check['nan'] = 0
        else:
            check[i] = 0
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number','C',size=255)
    w.field('city','C',size=255)
    w.field('roadclass','C',size=255)
    w.field('name','C',size=255)
    w.field('width','C',size=255)
    w.field('geometry','C',size=255)
    for i in range(df.shape[0]):
        # print(i)
        # print(df.loc[i,'ROADNAME'])
        # print(type(df.loc[i,'ROADNAME']))
        # i = 0
        lon = df.loc[i,'PositionLon'].split('[')[1].split(']')[0].split(', ')
        lat = df.loc[i,'PositionLat'].split('[')[1].split(']')[0].split(', ')
        ## shapefile-> 線性資料設定
        a = []
        for j in range(len(lon)):
            a.append([float(lon[j]) , float(lat[j]) ])
        ## 數據轉換為shapefile 線性圖像
        w.line([a])
        if check[df.loc[i,'ROADNAME']] <1:
            if str(df.loc[i,'ROADNAME']) != 'nan':
                if ('無名' in df.loc[i,'ROADNAME']) or ('街' in df.loc[i,'ROADNAME']) :
                    w.record(number=str(i+ 1), city=df.loc[i,'COUNTY'], roadclass=df.loc[i,'ROADCLASS1'], name="", width=df.loc[i,'WIDTH'],
                         geometry=a)
                else:
                    w.record(number=str(i+ 1), city=df.loc[i,'COUNTY'], roadclass=df.loc[i,'ROADCLASS1'], name=df.loc[i,'ROADNAME'], width=df.loc[i,'WIDTH'],
                             geometry=a)
                check[df.loc[i,'ROADNAME']] = check[df.loc[i,'ROADNAME']]+1
            else:
                w.record(number=str(i+ 1), city=df.loc[i,'COUNTY'], roadclass=df.loc[i,'ROADCLASS1'], name="", width=df.loc[i,'WIDTH'],
                geometry=a)
        else:
            w.record(number=str(i+ 1), city=df.loc[i,'COUNTY'], roadclass=df.loc[i,'ROADCLASS1'], name=" ", width=df.loc[i,'WIDTH'],geometry=a)
    w.close()
    # dbf = simpledbf.Dbf5(output_path + "\\road_shp.dbf",codec='utf8').to_dataframe()

def base_station_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    w.field('base_name','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(float(df.loc[i,'PositionLon']) , float(df.loc[i,'PositionLat']) )
        w.record(number=df.loc[i,'Number'], base_name=df.loc[i,'Base_name'], positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'])
    w.close()

def base_range_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(df.loc[i,'PositionLon'] , df.loc[i,'PositionLat'])
        w.record(number=df.loc[i,'Number'], positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'])
    w.close()

def bus_station_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('name','C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    w.field('cityname','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(df.loc[i,'PositionLon'] , df.loc[i,'PositionLat'])
        w.record(number=df.loc[i,'Number'], name=df.loc[i,'StopName_Zh_tw'],
                 positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'], cityname=df.loc[i,'CityName'])
    w.close()
def ubike_station_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('name','C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(df.loc[i,'PositionLon'] , df.loc[i,'PositionLat'])
        w.record(number=df.loc[i,'Number'], name=df.loc[i,'StationName_Zh_tw'],
                 positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'])
    w.close()
def parking_outside_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('name','C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(df.loc[i,'PositionLon'] , df.loc[i,'PositionLat'])
        w.record(number=df.loc[i,'Number'], name=df.loc[i,'name'],
                 positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'])
    w.close()
def parking_roadside_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(df.loc[i,'PositionLon'] , df.loc[i,'PositionLat'])
        w.record(number=df.loc[i,'Number'], positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'])
    w.close()
def track_mode_to_shp(data, output_path, shp_name):
    df = data
    # print(check)
    # 道路分類對照表
    # road_class_relation = {'HW':'國道', 'HU': '國道附屬道路', 'OE':'公務專用道路', '1E':'省道快速公路', '1W':'省道', '1U':'省道共線', '2W':'縣道',
    #                    '2U':'縣道共線', '3W':'鄉(鎮)道路', '3U':'鄉道共線', '4W':'產業道路', '4U':'專用公路/產業道路共線', 'RE':'市區快速道路(含匝道)',
    #                    'RD':'市區道路(路、街)(含圓環)', 'AL':'市區道路(巷、弄)', 'BR':'區塊道路', 'OR':'有路名但無法歸類(含林道)', 'OT':'無路名'}
    ## 建立空白 shapefile, encoding 編碼為 utf8, shapeType: shapefile 圖檔型態
    ''' shapefile.NULL = 0, shapefile.POINT = 1, shapefile.POLYLINE = 3, shapefile.POLYGON = 5, shapefile.MULTIPOINT = 8, 
        shapefile.POINTZ = 11, shapefile.POLYLINEZ = 13, shapefile.POLYGONZ = 15, shapefile.MULTIPOINTZ = 18, shapefile.POINTM = 21,
        shapefile.POLYLINEM = 23, shapefile.POLYGONM = 25, shapefile.MULTIPOINTM = 28, shapefile.MULTIPATCH = 31'''
    w = shp.Writer(output_path+"\\"+ shp_name,shapeType=1,encoding='utf8')
    ## shapefile-> .dbf 欄位設定
    w.field('number', 'C',size=255)
    w.field('name','C',size=255)
    w.field('positionLat','C',size=255)
    w.field('positionLon','C',size=255)
    w.field('locationtown','C',size=255)
    for i in range(df.shape[0]):        
        ## 數據轉換為shapefile point 圖像
        w.point(df.loc[i,'PositionLon'] , df.loc[i,'PositionLat'])
        w.record(number=df.loc[i,'Number'], name=df.loc[i,'StationName_Zh_tw'],
                 positionLat=df.loc[i,'PositionLat'], positionLon=df.loc[i,'PositionLon'], locationtown=df.loc[i,'LocationTown'])
    w.close()