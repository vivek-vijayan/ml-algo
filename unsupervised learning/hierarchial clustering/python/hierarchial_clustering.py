
# Heirachial clustering algorithm

from typing import List
from abc import abstractmethod

class Grouping:
    @abstractmethod
    def getGroup(self):
        pass

    @abstractmethod
    def setGroup(self):
        print("Group set success")

# Class
class DataPoint(Grouping):
    def __init__(self, dp: List, dim : int):
        self.point: List = dp
        self.dimension : int = dim
    
    def getGroup(self):
        return [self]
    
class GroupDataPoint(Grouping):
    def __init__(self, dp: List, dim : int):
        self.point : List = dp
        self.dimension : int = dim
        self.groups = []

    def setGroup(self, p: DataPoint):
        self.groups.append(p)
        return super().setGroup()
    
    def getGroup(self):
        return self.groups


def euclidean_formula(p1 : DataPoint, p2 : DataPoint, dimension: int):
    sum = 0
    for i in range(dimension):
        a = p1.point[i]
        b = p2.point[i]
        c = (a - b)**2
        sum += c
    return sum ** 0.5


# Step 1: Get the datapoints
p1 = DataPoint([10, 20], 2)
p2 = DataPoint([21, 51], 2)
p3 = DataPoint([32, 56], 2)
p4 = DataPoint([42, 10], 2)
p5 = DataPoint([15, 23], 2)

# step2 : Load it into a list of DP
datapoints = [p1, p2, p3, p4, p5]

# create a agglomerative matrix in 2D
total_dp = len(datapoints)

while total_dp:
    matrix = [[0] * total_dp for _ in range(total_dp)]

    min_val_found = float('inf')

    for i in range(total_dp):
        for j in range(total_dp):
            p1 = datapoints[i] 
            p2 = datapoints[j]
            diff = euclidean_formula(p1, p2, p1.dimension)
            matrix[i][j] = diff
            if diff > 0:
                min_val_found = min(min_val_found, diff)
    print(matrix)
    total_dp -= 1
    

print("Lowest value found : " , str(min_val_found))
