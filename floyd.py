import numpy as np

from read import read_dist

def Floyd(d):
    n = d.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d
if __name__=="__main__":
    graph=np.array(read_dist(0))
    print(graph)
    print("=================================================")
    graph=Floyd(graph)
    print(graph)