import random

from baidu_Map_API import *
from read import *
import Gaode_Map_API as MAP
scenic_info = read_info()


def dijkstra(matrix, source):
    INF = float('inf')
    n = len(matrix)
    m = len(matrix[0])
    assert n == m, "Error, please examine matrix dim"
    assert source < n, "Error, start point should be in the range!"
    S = [source]  # 已找到最短路径的节点集合
    U = [v for v in range(n) if v not in S]  # 记录还未确定最短路径的节点集合
    distance = [INF] * n  # source到已找到最短路径的节点的最短距离
    distance[source] = 0  # 起点到自己的距离
    path_optimal = [[]] * n  # source到其他节点的最短路径
    path_optimal[source] = [source]
    while len(S) < n:  # 当已找到最短路径的节点小于n时
        min_value = INF
        col = -1
        row = -1
        for s in S:  # 以已找到最短路径的节点所在行为搜索对象
            for u in U:  # 从U中搜索尚未记录的节点
                if matrix[s][u] + distance[s] < min_value:  # 找出最小值
                    # 在某行找到最小值要加上source到该行的最短路径
                    min_value = matrix[s][u] + distance[s]
                    row = s  # 记录所在行列
                    col = u
        if col == -1 or row == -1:  # 若没找出最小值且节点还未找完，说明图中存在不连通的节点
            break
        S.append(col)  # 在S中添加已找到的节点
        U.remove(col)  # 从U中移除已找到的节点
        distance[col] = min_value  # source到该节点的最短距离即为min_value
        path_optimal[col] = path_optimal[row][:]  # 复制source到已找到节点的上一节点的路径
        path_optimal[col].append(col)  # 再其后添加已找到节点即为source到该节点的最短路径
    return S, distance, path_optimal


def local_plan(matrix_list, end_id, transport, price_or_time):

    def Price(lst):
        if transport == 0:
            return list(map(lambda x:x*0.8,lst))
        if transport == 1:
            return list(map(taxi_cost, lst))
        if transport == 2:
            return [50]*len(lst)
    def Time(lst):
        return list(map(lambda x:round(x/60,1),lst))
    if price_or_time == 0:
        flag=0
        matrix = matrix_list[flag]
        matrix = list(map(Price, matrix))
        for i in range(14):
            for j in range(13):
                matrix[i][j] += scenic_info[j]['门票']
    else:
        if transport==2:
            flag=2
        else:
            flag=1
        matrix = matrix_list[flag]
        matrix=list(map(Time,matrix))
        for i in range(14):
            for j in range(13):
                matrix[i][j] += scenic_info[j]['建议游览时间']
    near_list=matrix[end_id]
    S, distance, path_optimal = dijkstra(matrix, 13)
    alternative_road = []
    alter_dist = []
    for p in path_optimal:
        if p[-1] == end_id:
            temp_dist = []
            alternative_road = p
            for i in range(len(p) - 1):
                temp_dist.append(matrix[p[i]][p[i + 1]])
            alter_dist = temp_dist
    return alternative_road, sum(alter_dist),near_list,matrix


def one_day_tour(matrix_list, transport, price_or_time, must_id):
    tour,cost,n_list,matrix=local_plan(matrix_list,must_id,transport,price_or_time)
    if(len(tour[1:])<3):
        alte=filter(lambda x:x not in tour and x!=13,range(13))
        new_cost=min(n_list[i] for i in alte)
        new_index=n_list.index(new_cost)
        tour.append(new_index)
        cost+=new_cost
    return tour,cost,matrix



def two_day_tour(matrix_list, transport, price_or_time, must_id):
    road1, cost1,matrix1 = one_day_tour(matrix_list,transport,price_or_time,must_id)
    cost1+=matrix1[road1[-1]][13]
    for row in range(14):
        for col in range(14):
            if row in road1[1:] or col in road1[1:]:
                matrix1[row][col]=float('inf')
    S, distance, path_optimal = dijkstra(matrix1, 13)
    road2=list(filter(lambda p:3<=len(p)<=4,path_optimal))[0]
    cost2=0.0
    cost2+=distance[road2[-1]]
    cost2+=matrix1[road2[-1]][13]
    road1.append(13)
    road2.append(13)
    result=[(road1,cost1),(road2,cost2)]
    return result




if __name__ == '__main__':
    matrix_list=Add_start_Matrix("哈尔滨工业大学威海")
    # result=two_day_tour(matrix_list,0,1,10)
    # for i in range(2):
    #     print(f"第{i+1}天：")
    #     print(result[i][0])
    #     print("代价：")
    #     print(result[i][1])
    #     print("----------------------------------------------------------------")
    road,cost,M=one_day_tour(matrix_list,1,0,8)
    print(road)
    print(cost)







