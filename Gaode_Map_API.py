import numpy as np
import pandas as pd
import requests
import json
from read import *
AK = "359d174bffb9a5cef70c67256469eaaa"  #你自己的注册码。
def getLocation(address):
    url = f"https://restapi.amap.com/v3/geocode/geo?address={address}&output=json&key={AK}"      #高德地图
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data["status"] == "1":        # 成功时返回1
        lnglat = json_data["geocodes"][0]["location"]
    else:
        return "no data", json_data["status"]
    return lnglat, json_data["status"]

def getDistance(start, end):
    url = f"https://restapi.amap.com/v3/direction/driving?origin={start}&destination={end}&output=json&key={AK}"
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data["status"] == "1":
        return json_data["route"]["paths"][0]["distance"]
    else:
        return -1

def calDistance(startAddr, endAddr):
    start, status1 = getLocation(startAddr)
    end, status2 = getLocation(endAddr)

    if status1 == "1" and status2 == "1":
        return getDistance(start, end)
    else:
        return -1
def Add_start_Matrix(startname):
    Matr_List=[]
    Matrix0 = read_dist(0)
    Matrix0.append([0] * 13)
    for x in Matrix0:
        x.append(0)
    Matrix1 = read_dist(1)
    Matrix1.append([0] * 13)
    for x in Matrix1:
        x.append(0)
    Matrix2 = read_dist(2)
    Matrix2.append([0] * 13)
    for x in Matrix2:
        x.append(0)
    data = [startname]
    res = []
    startName = data
    for j in range(13):
        all_row_dict = read_info()
        endName = all_row_dict[j]['景点名称']
        kilometre = calDistance(startName, endName)
        # duration = calDuration(startName, endName)
        res.append([round(float(kilometre) / 1000, 1), round(float(kilometre) / 285, 1)])
        Matrix0[j][-1] =Matrix0[-1][j]= res[-1][0]
        Matrix1[j][-1] = Matrix1[-1][j] = res[-1][1]
        Matrix2[j][-1] = Matrix2[-1][j] = res[-1][2]
    Matr_List.append(Matrix0)
    Matr_List.append(Matrix1)
    Matr_List.append(Matrix2)
    return Matr_List

if __name__ == "__main__":
    M = Add_start_Matrix("山东大学威海")
    for i in range(2):
        print(np.array(M[i]))
        print("=======================================================")