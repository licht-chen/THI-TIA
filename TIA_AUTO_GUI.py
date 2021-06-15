# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:32:51 2020

@author: user
"""
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import pandas as pd
from configparser import ConfigParser
import TIA_AUTO_no_station_address_othercity
import time

def bool_str(modal):
    string = 'Y'
    if modal.get() == False:
        string = 'N'
    return string
def parking_check():
    cfg = ConfigParser()
    cfg.optionxform = str  ##更改設定，保留大小寫
    # cfg.read(path+'Mode_City_information.ini', encoding='utf-8')
    cfg.read('Mode_City_information.ini', encoding='utf-8')
    parking_outside_cityname = {}
    parking_roadside_cityname = {}
    for i in cfg.items("parking_roadside_cityname"):
        parking_roadside_cityname[i[0]] = i[1]
    for i in cfg.items("parking_outside_cityname"):
        parking_outside_cityname[i[0]] = i[1]
    if main_city_box.get() != "" and main_city_box.get() not in list(parking_outside_cityname.keys()):
        # Parking_Outside['var'] = False
        Parking_Outside['state'] = 'disabled'
        # print(Parking_Outside['var'])
    elif Parking_Outside['state'] == 'disabled' and main_city_box.get() != "" and main_city_box.get() in list(parking_outside_cityname.keys()):
        Parking_Outside['state'] = 'normal' 
        # Parking_Outside['var'] = True
    if main_city_box.get() != "" and  main_city_box.get() not in list(parking_roadside_cityname.keys()):
        # Parking_Roadside['var'] = False
        # Parking_Roadside.config(state='disabled')
        Parking_Roadside['state'] = 'disabled'
        # print(Parking_Roadside['var'])
    elif Parking_Roadside['state'] == 'disabled' and main_city_box.get() != "" and  main_city_box.get() in list(parking_roadside_cityname.keys()):
        Parking_Roadside['state'] = 'normal'
        # Parking_Roadside['var'] = True
# def PO_check():
#     cfg = ConfigParser()
#     cfg.optionxform = str  ##更改設定，保留大小寫
#     # cfg.read(path+'Mode_City_information.ini', encoding='utf-8')
#     cfg.read('Mode_City_information.ini', encoding='utf-8')
#     parking_outside_cityname = {}
#     for i in cfg.items("parking_outside_cityname"):
#         parking_outside_cityname[i[0]] = i[1]
#     if main_city_box.get() != "" and main_city_box.get() not in list(parking_outside_cityname.keys()):
#         Parking_Outside['var'] = False
#         # Parking_Outside.config(state=DISABLED)
#         # Parking_Outside['state'] = 'active'
#         # print(Parking_Outside['var'])
#     elif Parking_Outside['state'] == 'disabled' and main_city_box.get() != "" and main_city_box.get() in list(parking_outside_cityname.keys()):
#         Parking_Outside['state'] = 'normal' 
#         Parking_Outside['var'] = True
# def PR_check():
#     cfg = ConfigParser()
#     cfg.optionxform = str  ##更改設定，保留大小寫
#     # cfg.read(path+'Mode_City_information.ini', encoding='utf-8')
#     cfg.read('Mode_City_information.ini', encoding='utf-8')
#     parking_roadside_cityname = {}
#     for i in cfg.items("parking_roadside_cityname"):
#         parking_roadside_cityname[i[0]] = i[1]
#     if main_city_box.get() != "" and  main_city_box.get() not in list(parking_roadside_cityname.keys()):
#         # Parking_Roadside['var'] = False
#         Parking_Roadside.config(state='disabled')
#         # Parking_Roadside['state'] = 'disabled'
#         # print(Parking_Roadside['var'])
#     elif Parking_Roadside['state'] == 'disabled' and main_city_box.get() != "" and  main_city_box.get() in list(parking_roadside_cityname.keys()):
#         Parking_Roadside['state'] = 'normal'
#         Parking_Roadside['var'] = True
def Run_TIA():
    "=========== 運具與城市名稱對照資訊表 ==========="
    # path = "G:\\共用雲端硬碟\\台北鼎漢(C_Public)\\Public\\014程式開發 TIA\\Program-Data_Download\\"
    cfg = ConfigParser()
    cfg.optionxform = str  ##更改設定，保留大小寫
    # cfg.read(path+'Mode_City_information.ini', encoding='utf-8')
    cfg.read('Mode_City_information.ini', encoding='utf-8')
    ptx_bike_cityname = {}
    for i in cfg.items("bike_cityname"):
        ptx_bike_cityname[i[0]] = i[1]
    ptx_innercity_bus_stopofroute_cityname = {}
    ptx_innercity_bus_station_cityname = {}
    ptx_innercity_bus_route_cityname = {}
    parking_outside_cityname = {}
    parking_roadside_cityname = {}
    for i in cfg.items("innercity_bus_cityname_stopofroute"):
        ptx_innercity_bus_stopofroute_cityname[i[0]] = i[1]
    for i in cfg.items("innercity_bus_cityname_station"):
        ptx_innercity_bus_station_cityname[i[0]] = i[1]
    for i in cfg.items("innercity_bus_cityname_route"):
        ptx_innercity_bus_route_cityname[i[0]] = i[1]
    for i in cfg.items("parking_outside_cityname"):
        parking_outside_cityname[i[0]] = i[1]
    for i in cfg.items("parking_roadside_cityname"):
        parking_roadside_cityname[i[0]] = i[1]
        
    "========= 基地資訊 get =========="
    project_name = project_entry.get()
    # print(project_name)
    base_name = []
    base_coordinate = {}
    base_range = {}
    base_across_city = {}
    if base_entry_1.get() != '':
        base_name.append(base_entry_1.get())
        base_coordinate[base_entry_1.get()] = base_position_entry_1.get().split(', ')
        base_range[base_entry_1.get()] = base_range_entry_1.get()
        # base_across_city[base_entry_1.get()] = base_crosscity_entry_1.get()
        base_across_city[base_entry_1.get()] = base_crosscity_1_check.get()
        # print(base_across_city)
    if base_entry_2.get() != '':
        base_name.append(base_entry_2.get())
        base_coordinate[base_entry_2.get()] = base_position_entry_2.get().split(', ')
        base_range[base_entry_2.get()] = base_range_entry_2.get()
        # base_across_city[base_entry_2.get()] = base_crosscity_entry_2.get()
        base_across_city[base_entry_2.get()] = base_crosscity_2_check.get()
        # print(base_across_city)

    city = {}
    # city['主縣市'] = ptx_innercity_bus_stopofroute_cityname[main_city_box.get()]
    city['主縣市'] = main_city_box.get()
    if cross_city_box.get() != '':
        # city['跨縣市'] = ptx_innercity_bus_stopofroute_cityname[cross_city_box.get()]
        city['跨縣市'] = cross_city_box.get()
    modal_choice = []
    modal_choice.append(bool_str(InnerCity_Bus_type))
    modal_choice.append(bool_str(InterCity_Bus_type))
    modal_choice.append(bool_str(Bike_type))
    modal_choice.append(bool_str(Parking_Outside_type))
    modal_choice.append(bool_str(Parking_Roadside_type))
    modal_choice.append(bool_str(THSR_type))
    modal_choice.append(bool_str(TRA_type))
    modal_choice.append(bool_str(TRTC_type))
    modal_choice.append(bool_str(KRTC_type))
    modal_choice.append(bool_str(TYMC_type))
    modal_choice.append(bool_str(KLRT_type))
    modal_choice.append(bool_str(NTDLRT_type))
    modal_choice.append(bool_str(TRTCMG_type))
    modal = {}
    modal_category = ['InnerCity_Bus', 'InterCity_Bus', 'Bike', 'Parking_Outside', 'Parking_Roadside', 'THSR', 'TRA',
                      'TRTC','KRTC', 'TYMC', 'KLRT', 'NTDLRT', 'TRTCMG']    
    for i in range(len(modal_category) ):
        modal[modal_category[i]] = modal_choice[i]

    road_choice = []
    road_choice.append(bool_str(road_check))
    road_choice.append(bool_str(sidewalk_check))
    road_category = ['Road','SideWalk']
    road_type_choice = {}
    for i in range(len(road_category)):
        road_type_choice[road_category[i]] = road_choice[i]
    # project_name = 'C000_府中美學'
    # base_name = ['府中站', '市民廣場']
    # base_coordinate = {'府中站': [25.00853207650213, 121.45942177851646],
    #                     '市民廣場': [25.01234076405166, 121.46571388726626]}
    # base_range = {'府中站': 500, '市民廣場': 500}
    # city['主縣市'] = '新北市'
    # city['跨縣市'] = ''
    # other_city = []
    # base_across_city = {'府中站': 'N', '市民廣場': 'N'}
    
    # project_name = '2.Twe_base(範例檔案)'
    # base_name = ['府中站', '市民廣場']
    # base_coordinate = {'府中站': [25.00853207650213, 121.45942177851646],
    #                     '市民廣場': [25.01234076405166, 121.46571388726626]}
    # base_range = {'府中站': 500, '市民廣場': 500}
    # city['主縣市'] = '新北市'
    # city['跨縣市'] = ''
    # other_city = []
    # base_across_city = {'府中站': 'N', '市民廣場': 'N'}
    
    # project_name = '1.One_base(範例檔案)'
    # base_name = ['府中站']
    # base_coordinate = {'府中站': [25.00853207650213, 121.45942177851646]}
    # base_range = {'府中站': 500}
    # city['主縣市'] = '新北市'
    # city['跨縣市'] = ''
    # other_city = []
    # base_across_city = {'府中站': 'N'}
    
    # project_name = 'C000_西門'
    # base_name = ['捷運西門站']
    # base_coordinate = {'捷運西門站': [25.042163997223607, 121.50829715210693]}
    # base_range = {'捷運西門站': 500}
    # city['主縣市'] = '臺北市'
    # city['跨縣市'] = ''
    # other_city = [] 
    # base_across_city = {'捷運西門站': 'N'}
    
    # project_name = 'C000_test'
    # base_name = ['THI']
    # base_coordinate = {'THI': [25.047795700115252, 121.57754008241648]}
    # base_range = {'THI': 500}
    # city['主縣市'] = '臺北市'
    # city['跨縣市'] = ''
    # other_city = [] 
    # base_across_city = {'THI': 'N'}
    
    # project_name = 'C975_南松山再生'
    # base_name = ['南松山']
    # base_coordinate = {'南松山': [25.047346526888532, 121.56316124176087]}
    # base_range = {'南松山': 900}
    # city['主縣市'] = '臺北市'
    # city['跨縣市'] = ''
    # other_city = [] 
    # base_across_city = {'南松山': 'N'}
    
    # project_name = 'C961'
    # base_name = ['桃園火車站']
    # base_coordinate = {'桃園火車站': [24.989109647446853, 121.31487290669371]}
    # base_range = {'桃園火車站': 1500}
    # city['主縣市'] = '桃園市'
    # city['跨縣市'] = ''
    # other_city = [] 
    # base_across_city = {'桃園火車站': 'N'}
    
    # project_name = 'C000_test'
    # base_name = ['台北車站']
    # base_coordinate = {'台北車站': [25.048077709955578, 121.51694045423902]}
    # base_range = {'台北車站': 1000}
    # city['主縣市'] = '臺北市'
    # city['跨縣市'] = ''
    # other_city = [] 
    # base_across_city = {'台北車站': 'N'}
    
    # project_name = 'Test_THI台中'
    # base_name = ['THI台中']
    # base_coordinate = {'THI台中': [24.162737489416855, 120.6694385060803]}
    # base_range = {'THI台中': 1000}
    # city['主縣市'] = '臺中市'
    # city['跨縣市'] = '彰化縣'
    # other_city = [] 
    # base_across_city = {'THI台中': 'N'}

    other_city = {'主縣市':[], '跨縣市':[]}
    if project_name == '':
        result_label.config(text="請輸入專案名稱", font=('標楷體', 20 , "bold"),background='white')
    elif len(base_name) == 0:
        result_label.config(text="請輸入基地名稱", font=('標楷體', 20 , "bold"),background='white')
    elif city['主縣市'] == "":
        result_label.config(text="請輸入主縣市", font=('標楷體', 20 , "bold"),background='white')
    elif city['主縣市'] not in list(parking_roadside_cityname.keys()) and Parking_Roadside_type.get() == True:
        # print("yeeeeeeeeeeee")
        result_label.config(text="該縣市無「路邊停車資訊」，請勿勾選", font=('標楷體', 20 , "bold"),background='white')
    elif city['主縣市']  not in list(parking_outside_cityname.keys()) and Parking_Outside_type.get() == True:
        result_label.config(text="該縣市無「路外停車資訊」，請勿勾選", font=('標楷體', 20 , "bold"),background='white')
    else:
    ### 城市
        # cityname = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市","新竹市",
        #             "新竹縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市","屏東縣", "宜蘭縣",
        #             "花蓮縣", "臺東縣", "金門縣", "澎湖縣", "連江縣"]
        # analysis_check = 0
        if result_label['text'] !="分析即將開始\n請再按一次分析開始":
            result_label.config(text="分析即將開始\n請再按一次分析開始", font=('標楷體', 20 , "bold"),background='white')
            # print(result_label['text'])
        else :
            for i in list(city.keys()):
                if city[i] != '':
                    if i == '主縣市':
                        if ( city[i] == '臺北市') or (city[i] == '新北市') or (city[i] == '基隆市') or (city[i] == '桃園市'):
                            other_city[i] = ['臺北市', '新北市', '基隆市', '桃園市'] 
                        elif (city[i] == '新竹縣') or (city[i] == '新竹市'):
                            other_city[i] = ['新竹縣', '新竹市']
                        elif (city[i] == '嘉義縣') or (city[i] == '嘉義市'):
                            other_city[i] = ['嘉義縣', '嘉義市']
                        elif (city[i] == '臺中市') or (city[i]=='彰化縣') or (city[i] == '南投縣') or (city[i]=='雲林縣'):
                            other_city[i] = ['臺中市', '彰化縣', '南投縣', '雲林縣']
                    elif i == '跨縣市':
                        if city[i] not in other_city['主縣市']:
                            if ( city[i] == '臺北市') or (city[i] == '新北市') or (city[i] == '基隆市') or (city[i] == '桃園市'):
                                other_city[i] = ['臺北市', '新北市', '基隆市', '桃園市'] 
                            elif (city[i] == '新竹縣') or (city[i] == '新竹市'):
                                other_city[i] = ['新竹縣', '新竹市']
                            elif (city[i] == '嘉義縣') or (city[i] == '嘉義市'):
                                other_city[i] = ['嘉義縣', '嘉義市']
                            elif (city[i] == '臺中市') or (city[i]=='彰化縣') or (city[i] == '南投縣') or (city[i]=='雲林縣'):
                                other_city[i] = ['臺中市', '彰化縣', '南投縣', '雲林縣']
            result_label.config(text="分析中，請稍後", font=('標楷體', 20 , "bold"),background='white')
            TIA_AUTO_no_station_address_othercity.TIA(project_name, base_name, base_coordinate, base_range, city, base_across_city, other_city, modal, 
                                                      ptx_innercity_bus_stopofroute_cityname, ptx_innercity_bus_station_cityname,
                                                      ptx_innercity_bus_route_cityname, ptx_bike_cityname,
                                                      parking_outside_cityname, parking_roadside_cityname, road_type_choice, output_bool = True)
            result_label.config(text="分析完畢，請按離開", font=('標楷體', 20 , "bold"),background='white')

def close():
    window.destroy()

## 鼠標滾輪+ tkinter中滾動條
def on_mousewheel(event): 
    shift = (event.state & 0x1) != 0 
    scroll = -1 if event.delta > 0 else 1 
    if shift: 
     can.xview_scroll(scroll, "units") 
    else: 
     can.yview_scroll(scroll, "units") 

name = ""
## TK 視窗宣告
window = tk.Tk()
window.title('TIA 基地周邊公共運輸站點分析')
# # window.geometry('600x900+500+0')
# window.state("zoomed")
# window.configure(background = '#F0FFFF')
## 畫布設定
can = tk.Canvas(window, width = 400, height = 850,  relief = 'raised', bg = '#F0FFFF', scrollregion=(0,0,900,900))

## 滑動條設定
vbar=tk.Scrollbar(window,orient='vertical', activebackground='black')
vbar.pack(side='right',fill='y')
vbar.config(command=can.yview)
can.config(yscrollcommand=vbar.set)
can.bind_all("<MouseWheel>", on_mousewheel) 
can.pack()
title_label = tk.Label(window, text='TIA 基地周邊公共運輸站點分析', bg = '#F0FFFF', font=('微軟正黑體', 18))
can.create_window(200, 25, window=title_label)

## 宣告porjcet_name 視窗物件(Entry)
#name = tk.StringVar()
# project_name = tk.Frame(window, background = '#F0FFFF')
# project_name.place(x = 30,y = 50)
# project_name.pack(side=tk.TOP)
# project_label = ttk.Label(project_name, text='專案名稱', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# project_label.place(x = 30,y = 50)
# project_label.pack(side=tk.LEFT)
# project_label.grid(column=0, row=0, pady=5, sticky=tk.W+tk.N)
# project_entry = ttk.Entry(project_name)
# project_entry.pack(side=tk.LEFT)
# project_entry.grid(column=1, row=0, pady=5, sticky=tk.W+tk.N)
project_label = ttk.Label(window, text='專案名稱', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 70, window = project_label)
project_entry = ttk.Entry(window)
can.create_window(280, 70, window = project_entry)


## 宣告 base_name_1 物件(Entry)
# base_name_1 = tk.Frame(window, background = '#F0FFFF')
# base_name_1.pack(side=tk.TOP)
# base_label_1 = ttk.Label(base_name_1, text='基地1名稱', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))  
# base_label_1.grid(column=0, row=1, pady=5, sticky=tk.W+tk.N)
# base_entry_1 = ttk.Entry(base_name_1)
# base_entry_1.grid(column=1, row=1, pady=5, sticky=tk.W+tk.N)
base_label_1 = ttk.Label(window, text='基地1名稱', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 100, window = base_label_1)
base_entry_1 = ttk.Entry(window)
can.create_window(280, 100, window = base_entry_1)


## 宣告 base_position_1 物件 (Entry)
# base_position_1 = tk.Frame(window, background = '#F0FFFF')
# base_position_1.pack(side=tk.TOP)
# base_position_label_1 = ttk.Label(base_position_1, text='基地1位置(經緯度)', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# base_position_label_1.grid(column=0, row=2, pady=5, sticky=tk.W+tk.N)
# base_position_entry_1 = ttk.Entry(base_position_1)
# base_position_entry_1.grid(column=1, row=2, pady=5, sticky=tk.W+tk.N)
base_position_label_1 = ttk.Label(window, text='基地1位置(經緯度)', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 130, window = base_position_label_1)
base_position_entry_1 = ttk.Entry(window)
can.create_window(280, 130, window = base_position_entry_1)

## 宣告 base_range_1 物件 (Entry)
# base_range_1 = tk.Frame(window, background = '#F0FFFF')
# base_range_1.pack(side=tk.TOP)
# base_range_label_1 = ttk.Label(base_range_1, text='基地1分析範圍(m)', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# base_range_label_1.grid(column=0, row=3, pady=5, sticky=tk.W+tk.N)
# base_range_entry_1 = ttk.Entry(base_range_1)
# base_range_entry_1.grid(column=1, row=3, pady=5, sticky=tk.W+tk.N)
base_range_label_1 = ttk.Label(window, text='基地1分析範圍(m)', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 160, window = base_range_label_1)
base_range_entry_1 = ttk.Entry(window)
can.create_window(280, 160, window = base_range_entry_1)

## 宣告 base_crosscity_1 物件 (Entry)
# base_crosscity_1 = tk.Frame(window, background = '#F0FFFF')
# base_crosscity_1.pack(side=tk.TOP)
# base_crosscity_label_1 = ttk.Label(base_crosscity_1, text='基地1分析範圍跨縣市', width=22, background = '#F0FFFF', font=('微軟正黑體', 12))
# base_crosscity_label_1.pack(side=tk.LEFT)
# base_crosscity_label_1.grid(column=0, row=4, pady=5, sticky=tk.W+tk.N)
# === Radiobutton === #
# base_crosscity_1_check=tk.IntVar()
# base_crosscity_1_yes = tk.Radiobutton(base_crosscity_1, text='Yes', variable=base_crosscity_1_check, value=True, background = '#F0FFFF',
#                                       font=('Times New Roman', 12))
# base_crosscity_1_no = tk.Radiobutton(base_crosscity_1, text='No', variable=base_crosscity_1_check, value=False, background = '#F0FFFF',
#                                       font=('Times New Roman', 12))
# base_crosscity_1_yes.pack(side=tk.LEFT)
# base_crosscity_1_no.pack(side=tk.LEFT)
# base_crosscity_1_yes.grid(column=1, row=4, pady=5, sticky=tk.W+tk.N)
# base_crosscity_1_no.grid(column=2, row=4, pady=5, sticky=tk.W+tk.N)

base_crosscity_label_1 = ttk.Label(window, text='基地1分析範圍跨縣市', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 190, window = base_crosscity_label_1)
base_crosscity_1_check=tk.IntVar()
base_crosscity_1_yes = tk.Radiobutton(window, text='Yes', variable=base_crosscity_1_check, value=True, background = '#F0FFFF',
                                      font=('Times New Roman', 12))
base_crosscity_1_no = tk.Radiobutton(window, text='No', variable=base_crosscity_1_check, value=False, background = '#F0FFFF',
                                      font=('Times New Roman', 12))
can.create_window(250, 190, window = base_crosscity_1_yes)
can.create_window(310, 190, window = base_crosscity_1_no)


## 宣告 base_name_2 物件(Entry)
# base_name_2 = tk.Frame(window, background = '#F0FFFF')
# base_name_2.pack(side=tk.TOP)
# base_label_2 = ttk.Label(base_name_2, text='基地2名稱', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# base_label_2.grid(column=0, row=5, pady=5, sticky=tk.W+tk.N)
# base_entry_2 = ttk.Entry(base_name_2)
# base_entry_2.grid(column=1, row=5, pady=5, sticky=tk.W+tk.N)
base_label_2 = ttk.Label(window, text='基地2名稱', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 220, window = base_label_2)
base_entry_2 = ttk.Entry(window)
can.create_window(280, 220, window = base_entry_2)

## 宣告 base_position_2 物件 (Entry)
# base_position_2 = tk.Frame(window, background = '#F0FFFF')
# base_position_2.pack(side=tk.TOP)
# base_position_label_2 = ttk.Label(base_position_2, text='基地2位置(經緯度)', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# base_position_label_2.grid(column=0, row=6, pady=5, sticky=tk.W+tk.N)
# base_position_entry_2 = ttk.Entry(base_position_2)
# base_position_entry_2.grid(column=1, row=6, pady=5, sticky=tk.W+tk.N) 
base_position_label_2 = ttk.Label(window, text='基地2位置(經緯度)', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 250, window = base_position_label_2)
base_position_entry_2 = ttk.Entry(window)
can.create_window(280, 250, window = base_position_entry_2)

## 宣告 base_range_2 物件 (Entry)
# base_range_2 = tk.Frame(window, background = '#F0FFFF')
# base_range_2.pack(side=tk.TOP)
# base_range_label_2 = ttk.Label(base_range_2, text='基地2分析範圍(m)', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# base_range_label_2.grid(column=0, row=7, pady=5, sticky=tk.W+tk.N)
# base_range_entry_2 = ttk.Entry(base_range_2)
# base_range_entry_2.grid(column=1, row=7, pady=5, sticky=tk.W+tk.N)
base_range_label_2 = ttk.Label(window, text='基地2分析範圍(m)', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 280, window = base_range_label_2)
base_range_entry_2 = ttk.Entry(window)
can.create_window(280, 280, window = base_range_entry_2)

## 宣告 base_crosscity_2 物件 (Entry)
# base_crosscity_2 = tk.Frame(window, background = '#F0FFFF')
# base_crosscity_2.pack(side=tk.TOP)
# base_crosscity_label_2 = ttk.Label(base_crosscity_2, text='基地2分析範圍跨縣市', width=22, background = '#F0FFFF', font=('微軟正黑體', 12))
# # base_crosscity_label_2.pack(side=tk.LEFT)
# base_crosscity_label_2.grid(column=0, row=8, pady=5, sticky=tk.W+tk.N)
# # base_crosscity_entry_2 = tk.Entry(base_crosscity_2)
# # # base_position_entry_2.place(x = 50,y = 130)
# # base_crosscity_entry_2.pack(side=tk.LEFT)
# base_crosscity_2_check=tk.IntVar()
# base_crosscity_2_yes = tk.Radiobutton(base_crosscity_2, text='Yes', variable=base_crosscity_2_check, value=True, background = '#F0FFFF',
#                                       font=('Times New Roman', 12))
# base_crosscity_2_no = tk.Radiobutton(base_crosscity_2, text='No', variable=base_crosscity_2_check, value=False, background = '#F0FFFF',
#                                      font=('Times New Roman', 12))
# base_crosscity_2_yes.grid(column=1, row=8,pady=5, sticky=tk.W+tk.N)
# base_crosscity_2_no.grid(column=2, row=8, pady=5, sticky=tk.W+tk.N)

base_crosscity_label_2 = ttk.Label(window, text='基地2分析範圍跨縣市', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 310, window = base_crosscity_label_2)
base_crosscity_2_check=tk.IntVar()
base_crosscity_2_yes = tk.Radiobutton(window, text='Yes', variable=base_crosscity_2_check, value=True, background = '#F0FFFF',
                                      font=('Times New Roman', 12))
base_crosscity_2_no = tk.Radiobutton(window, text='No', variable=base_crosscity_2_check, value=False, background = '#F0FFFF',
                                      font=('Times New Roman', 12))
can.create_window(250, 310, window = base_crosscity_2_yes)
can.create_window(310, 310, window = base_crosscity_2_no)
# window.mainloop()
### 城市
cityname = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市","新竹市",
            "新竹縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市","屏東縣", "宜蘭縣",
            "苗栗縣", "花蓮縣", "臺東縣", "金門縣", "澎湖縣", "連江縣"]
## 主縣市
# main_city = tk.Frame(window, background = '#F0FFFF')
# main_city.pack(side=tk.TOP)
# main_city_label = ttk.Label(main_city, text='主縣市', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# main_city_label.grid(column=0, row=9, pady=5, sticky=tk.W+tk.N)
# main_city_box = tk.ttk.Combobox(main_city, values = cityname, width = 17)
# main_city_box.grid(column=1, row=9, pady=5, sticky=tk.W+tk.N)

main_city_label = ttk.Label(window, text='主縣市', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 340, window = main_city_label)
main_city_box = tk.ttk.Combobox(window, values = cityname, width = 17)
can.create_window(280, 340, window = main_city_box)

## Parking check button
# button2 = tk.Button(main_city, text="Parking_check", command = parking_check)
# button2.grid(column=1, row=10, pady=5, sticky=tk.W+tk.N)
button2_label = ttk.Label(window, text='縣市路外停車檢核紐', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 370, window = button2_label)
button2 = tk.Button(window, text="Parking_check", command = parking_check)
can.create_window(280, 370, window = button2)

## 跨縣市
# cross_city = tk.Frame(window, background = '#F0FFFF')
# cross_city.pack(side=tk.TOP)
# cross_city_label = ttk.Label(cross_city, text='跨縣市', width=15, background = '#F0FFFF', font=('微軟正黑體', 12))
# cross_city_label.grid(column=0, row=10,pady=5, sticky=tk.W+tk.N)
# cross_city_box = tk.ttk.Combobox(cross_city, values = cityname, width = 17)
# cross_city_box.grid(column=1, row=10,pady=5, sticky=tk.W+tk.N)
cross_city_label = ttk.Label(window, text='跨縣市', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 400, window = cross_city_label)
cross_city_box = tk.ttk.Combobox(window, values = cityname, width = 17)
can.create_window(280, 400, window = cross_city_box)

## 運具
# modal = tk.Frame(window, background = '#F0FFFF')
# modal.pack(side=tk.TOP)
# modal_label = ttk.Label(modal, text='公共運具', width=13, background = '#F0FFFF', font=('微軟正黑體', 12))
# modal_label.grid(column=0,row=14, pady=5, sticky=tk.W+tk.N)
modal_label = ttk.Label(window, text='公共運具選擇', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 500, window = modal_label)
# window.mainloop()

InnerCity_Bus_type = tk.BooleanVar()
InterCity_Bus_type = tk.BooleanVar()
Bike_type = tk.BooleanVar()
Parking_Outside_type = tk.BooleanVar()
Parking_Roadside_type = tk.BooleanVar()
THSR_type = tk.BooleanVar()
TRA_type = tk.BooleanVar()
TRTC_type = tk.BooleanVar()
KRTC_type = tk.BooleanVar()
TYMC_type = tk.BooleanVar()
KLRT_type = tk.BooleanVar()
NTDLRT_type = tk.BooleanVar()
TRTCMG_type = tk.BooleanVar()

InnerCity_Bus_type.set(True)
InterCity_Bus_type.set(True)
Bike_type.set(True)
Parking_Outside_type.set(False) 
Parking_Roadside_type.set(False)
THSR_type.set(True)
TRA_type.set(True)
TRTC_type.set(True)
KRTC_type.set(False)
TYMC_type.set(False)
KLRT_type.set(False)
NTDLRT_type.set(False)
TRTCMG_type.set(False)

## 市區公車
# InnerCity_Bus = tk.Checkbutton(modal, text = '市區公車',var=InnerCity_Bus_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# InnerCity_Bus.grid(column=1,row=11, pady=5, sticky=tk.W+tk.N)
InnerCity_Bus = tk.Checkbutton(window, text = '市區公車',var=InnerCity_Bus_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(200, 440, window = InnerCity_Bus)
## 公路客運
# InterCity_Bus = tk.Checkbutton(modal, text = '公路客運',var=InterCity_Bus_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# InterCity_Bus.grid(column=2,row=11, pady=5, sticky=tk.W+tk.N)
InterCity_Bus = tk.Checkbutton(window, text = '公路客運',var=InterCity_Bus_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(300, 440, window = InterCity_Bus)
## 自行車
# Bike = tk.Checkbutton(modal, text = '自行車',var=Bike_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# Bike.grid(column=1,row=12, pady=5, sticky=tk.W+tk.N)
Bike = tk.Checkbutton(window, text = '自行車',var=Bike_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(192, 470, window = Bike)
## 路外停車
# Parking_Outside = tk.Checkbutton(modal, text = '路外停車',var=Parking_Outside_type, background = '#F0FFFF', font=('微軟正黑體', 12), command = PO_check)
# Parking_Outside = tk.Checkbutton(modal, text = '路外停車',var=Parking_Outside_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# Parking_Outside.grid(column=1,row=13, pady=5, sticky=tk.W+tk.N)
Parking_Outside = tk.Checkbutton(window, text = '路外停車',var=Parking_Outside_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(200, 500, window = Parking_Outside)
## 路邊停車
# Parking_Roadside = tk.Checkbutton(modal, text = '路邊停車',var=Parking_Roadside_type, background = '#F0FFFF', font=('微軟正黑體', 12), command = PR_check)
# Parking_Roadside = tk.Checkbutton(modal, text = '路邊停車',var=Parking_Roadside_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# Parking_Roadside.grid(column=2,row=13, pady=5, sticky=tk.W+tk.N)
Parking_Roadside = tk.Checkbutton(window, text = '路邊停車',var=Parking_Roadside_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(300, 500, window = Parking_Roadside)
## 高鐵
# THSR = tk.Checkbutton(modal, text = '臺灣高鐵',var=THSR_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# THSR.grid(column=1,row=14, pady=5, sticky=tk.W+tk.N)
THSR = tk.Checkbutton(window, text = '臺灣高鐵',var=THSR_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(200, 530, window = THSR)
## 台鐵
# TRA = tk.Checkbutton(modal, text = '臺灣鐵路',var=TRA_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# TRA.grid(column=2,row=14, pady=5, sticky=tk.W+tk.N)
TRA = tk.Checkbutton(window, text = '臺灣鐵路',var=TRA_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(300, 530, window = TRA)
## 台北捷運
# TRTC = tk.Checkbutton(modal, text = '臺北捷運',var=TRTC_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# TRTC.grid(column=1,row=15, pady=5, sticky=tk.W+tk.N)
TRTC = tk.Checkbutton(window, text = '臺北捷運',var=TRTC_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(200, 560, window = TRTC)
## 桃園捷運
# TYMC = tk.Checkbutton(modal, text = '桃園捷運',var=TYMC_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# TYMC.grid(column=2,row=15, pady=5, sticky=tk.W+tk.N)
TYMC = tk.Checkbutton(window, text = '桃園捷運',var=TYMC_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(300, 560, window = TYMC)
## 高雄捷運
# KRTC = tk.Checkbutton(modal, text = '高雄捷運',var=KRTC_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# KRTC.grid(column=1,row=16, pady=5, sticky=tk.W+tk.N)
KRTC = tk.Checkbutton(window, text = '高雄捷運',var=KRTC_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(200, 590, window = KRTC)
## 高雄輕軌
# KLRT = tk.Checkbutton(modal, text = '高雄輕軌',var=KLRT_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# KLRT.grid(column=2,row=16, pady=5, sticky=tk.W+tk.N)
KLRT = tk.Checkbutton(window, text = '高雄輕軌',var=KLRT_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(300, 590, window = KLRT)
## 淡海輕軌
# NTDLRT = tk.Checkbutton(modal, text = '淡海輕軌',var=NTDLRT_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# NTDLRT.grid(column=1,row=17, pady=5, sticky=tk.W+tk.N)
NTDLRT = tk.Checkbutton(window, text = '淡海輕軌',var=NTDLRT_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(200, 620, window = NTDLRT)
## 貓空纜車
# TRTCMG = tk.Checkbutton(modal, text = '貓空纜車',var=TRTCMG_type, background = '#F0FFFF', font=('微軟正黑體', 12))
# TRTCMG.grid(column=1,row=18, pady=5, sticky=tk.W+tk.N)
TRTCMG = tk.Checkbutton(window, text = '貓空纜車',var=TRTCMG_type, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(300, 620, window = TRTCMG)
# window.mainloop()

## 人行道
# sidewalk = tk.Frame(window, background = '#F0FFFF')
# sidewalk.pack(side=tk.TOP)
# sidewalk_label = ttk.Label(sidewalk, text='人行道', width=10, background = '#F0FFFF', font=('微軟正黑體', 12))
# sidewalk_label.grid(column=0, row=19, pady=5, sticky=tk.W+tk.N)
# sidewalk_check=tk.IntVar()
# sidewalk_check.set(True)
# sidewalk_yes = tk.Radiobutton(sidewalk, text='Yes', variable=sidewalk_check, value=True, background = '#F0FFFF', font=('Times New Roman', 12))
# sidewalk_no = tk.Radiobutton(sidewalk, text='No', variable=sidewalk_check, value=False, background = '#F0FFFF', font=('Times New Roman', 12))
# sidewalk_yes.grid(column=1, row=19, pady=5, sticky=tk.W+tk.N)
# sidewalk_no.grid(column=2, row=19, pady=5, sticky=tk.W+tk.N)
sidewalk_label = ttk.Label(window, text='人行道資訊', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 650, window = sidewalk_label)
sidewalk_check=tk.IntVar()
sidewalk_check.set(True)
sidewalk_yes = tk.Radiobutton(window, text='Yes', variable=sidewalk_check, value=True, background = '#F0FFFF', font=('Times New Roman', 12))
sidewalk_no = tk.Radiobutton(window, text='No', variable=sidewalk_check, value=False, background = '#F0FFFF', font=('Times New Roman', 12))
can.create_window(250, 650, window = sidewalk_yes)
can.create_window(310, 650, window = sidewalk_no)

## 道路
# road = tk.Frame(window, background = '#F0FFFF')
# road.pack(side=tk.TOP)
# road_label = ttk.Label(road, text='道路', width=10, background = '#F0FFFF', font=('微軟正黑體', 12))
# road_label.grid(column=0, row=20, pady=5, sticky=tk.W+tk.N)
# road_check=tk.IntVar()
# road_check.set(True)
# road_yes = tk.Radiobutton(road, text='Yes', variable=road_check, value=True, background = '#F0FFFF', font=('Times New Roman', 12))
# road_no = tk.Radiobutton(road, text='No', variable=road_check, value=False, background = '#F0FFFF', font=('Times New Roman', 12))
# road_yes.grid(column=1, row=20, pady=5, sticky=tk.W+tk.N)
# road_no.grid(column=2, row=20, pady=5, sticky=tk.W+tk.N)
road_label = ttk.Label(window, text='道路資訊', width=18, background = '#F0FFFF', font=('微軟正黑體', 12))
can.create_window(110, 680, window = road_label)
road_check=tk.IntVar()
road_check.set(True)
road_yes = tk.Radiobutton(window, text='Yes', variable=road_check, value=True, background = '#F0FFFF', font=('Times New Roman', 12))
road_no = tk.Radiobutton(window, text='No', variable=road_check, value=False, background = '#F0FFFF', font=('Times New Roman', 12))
can.create_window(250, 680, window = road_yes)
can.create_window(310, 680, window = road_no)

# window.mainloop()

### result 
## ttk button font style setting
s = ttk.Style(window)
s.configure('my.TButton', font=('微軟正黑體', 12 , "bold"), background = '#F0FFFF')
result_label = ttk.Label(window, background = '#F0FFFF')
can.create_window(200, 800, window = result_label)
calculate_btn = ttk.Button(window, text='分析開始', command=Run_TIA, style='my.TButton')
# calculate_btn.pack(pady = 5)
can.create_window(130, 750, window = calculate_btn)
# calculate_btn.grid(column=1, row=19, pady=5, sticky=tk.W+tk.N)
quit_btn = ttk.Button(window, text="離開", command=close, style='my.TButton')
# quit_btn.pack()
can.create_window(280, 750, window = quit_btn)
# quit_btn.grid(column=1, row=19, pady=5, sticky=tk.W+tk.N)
window.mainloop()
