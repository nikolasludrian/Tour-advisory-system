import numpy as np
from read import read_dist
class HamiltonUtil:
    def __init__(self, input_matrix):
        self.graph = input_matrix
        self.point_num = np.shape(self.graph)[0]
        self.HamSolve = []
        self.HamLength = 0

    def search_min(self, index, matrix):
        min_val = float('inf')
        for i in matrix:
            if self.graph[index][i - 1] < min_val:
                min_val = self.graph[index][i - 1]
        return min_val

    def find_match_vex(self, index, match_val):
        ret_index = 0
        for i in self.graph[index]:
            if i != match_val:
                ret_index += 1
            else:
                break
        return ret_index

    def find_index(self, vec, value):
        index = 0
        for i in vec:
            if i != value:
                index += 1
            else:
                break
        return index
    def clear_stack(self):
        self.HamSolve = []
        self.HamLength = 0

    def neibor_point(self):
        self.clear_stack()
        start = 1
        V = np.arange(1, self.point_num + 1, 1)
        self.HamSolve.append(start)
        V = np.delete(V, start - 1)
        BetweenPoint = start
        while np.shape(V)[0] != 0:
            VWeight = self.search_min(BetweenPoint - 1, V)
            Next = self.find_match_vex(BetweenPoint - 1, VWeight) + 1
            self.HamSolve.append(Next)
            V = np.setdiff1d(V, Next)
            self.HamLength = self.HamLength + VWeight
            BetweenPoint = Next
        self.HamSolve.append(start)
        self.HamLength = self.HamLength + self.graph[Next - 1][start - 1]

    def nearest_insertion(self):
        self.clear_stack()
        start = 1
        V = np.arange(1, self.point_num + 1, 1)
        self.HamSolve.append(start)
        V = np.setdiff1d(V, self.HamSolve)
        BetweenPoint = start
        VWeight = self.search_min(BetweenPoint - 1, V)
        Next = self.find_match_vex(BetweenPoint - 1, VWeight) + 1
        self.HamSolve.append(Next)
        self.HamSolve.append(start)
        V = np.setdiff1d(V, Next)
        self.HamLength = self.HamLength + VWeight + self.graph[Next - 1][start - 1]
        BetweenPoint = Next

        while np.shape(V)[0] != 0:
            HamPoint = list(set(self.HamSolve))
            NearestPoint = 0
            NearWeight = np.zeros((len(HamPoint),), dtype=float)
            NearPoint = np.zeros((len(HamPoint),), dtype=int)
            for i in range(len(HamPoint)):
                NearWeight[i] = self.search_min(HamPoint[i] - 1, V)
                NearPoint[i] = self.find_match_vex(HamPoint[i] - 1, NearWeight[i]) + 1
            NearestPoint = NearPoint[self.find_index(NearWeight, np.min(NearWeight))]
            HamIncrement = np.zeros((len(self.HamSolve) - 1,), dtype=float)
            for i in range(len(self.HamSolve) - 1):
                HamIncrement[i] = self.graph[self.HamSolve[i] - 1][NearestPoint - 1] + \
                                  self.graph[NearestPoint - 1][self.HamSolve[i + 1] - 1] - \
                                  self.graph[self.HamSolve[i] - 1][self.HamSolve[i + 1] - 1]
            MinHamIncrement = np.min(HamIncrement)
            InsertPoint = self.find_index(HamIncrement, MinHamIncrement) + 1
            self.HamSolve.insert(InsertPoint, NearestPoint)
            self.HamLength += MinHamIncrement
            V = np.setdiff1d(V, NearestPoint)
if __name__ == '__main__':
    # E = np.array([[float('inf'), 10, 6, 8, 7, 15],
    #               [10, float('inf'), 5, 20, 15, 16],
    #               [6, 5, float('inf'), 14, 7, 8],
    #               [8, 20, 14, float('inf'), 4, 12],
    #               [7, 15, 7, 4, float('inf'), 6],
    #               [15, 16, 8, 12, 6, float('inf')]], dtype=float)
    graph = np.array(read_dist(1), dtype=float)
    # neibor_point = HamiltonUtil(graph)
    # # 最邻近点法
    # neibor_point.neibor_point()
    # print(neibor_point.HamSolve)
    # print(neibor_point.HamLength)

    E = np.array([[float('inf'), 10, 6, 8, 7, 15],
                  [10, float('inf'), 5, 20, 15, 16],
                  [6, 5, float('inf'), 14, 7, 8],
                  [8, 20, 14, float('inf'), 4, 12],
                  [7, 15, 7, 4, float('inf'), 6],
                  [15, 16, 8, 12, 6, float('inf')]], dtype=float)
    nearest_insertion = HamiltonUtil(E)
    # 最近插值法
    nearest_insertion.nearest_insertion()
    print(nearest_insertion.HamSolve)
    print(nearest_insertion.HamLength)

