# DBSCAN algothirm
from typing import List, Dict

class DataPoint:
    def __init__(self, dp: List, dim : int, datapointname: str):
        self.point: List = dp
        self.dimension : int = dim
        self.name : str = datapointname
        self.type = ""

    def __str__(self):
        return str(self.name)

class EpsilonDataSet(DataPoint):
    def __init__(self, datapoint: DataPoint, minpts : int):
        self.dp = datapoint
        self.group : List = []
        self.type = ""
        self.minpoint = minpts
        print("Created Epsilon Group for " + str(self.dp))

    def __str__(self):
        return str(self.dp)
    
    def add(self, pts : DataPoint, show : bool = False) -> bool:
        self.group.append(pts)
        if show:
            print("Added " + str(pts) + " into " + str(self.dp))
        return True
    
    def finish(self):
        count = len(self.group)
        if count >= self.minpoint:
            self.type = "CORE"
        else:
            self.type = "NOISE"
    
    def showall(self):
        output_string = ""
        for each in self.group:
            output_string += str(each) + "  "
        return output_string
    
    def getall(self):
        return self.group
    
    def showtype(self):
        return str(self.type)

def euclidean_formula(p1 : DataPoint, p2 : DataPoint, dimension: int):
    sum = 0
    for i in range(dimension):
        a = p1.point[i]
        b = p2.point[i]
        c = (a - b)**2
        sum += c
    return sum ** 0.5

# 12 Data points
p1 = DataPoint([3, 7], 2, "P1")
p2 = DataPoint([4, 6], 2, "P2")
p3 = DataPoint([5, 5], 2, "P3")
p4 = DataPoint([6, 4], 2, "P4")
p5 = DataPoint([7, 3], 2, "P5")
p6 = DataPoint([6, 2], 2, "P6")
p7 = DataPoint([7, 2], 2, "P7")
p8 = DataPoint([8, 4], 2, "P8")
p9 = DataPoint([3, 3], 2, "P9")
p10 = DataPoint([2, 6], 2, "P10")
p11 = DataPoint([3, 5], 2, "P11")
p12 = DataPoint([2, 4], 2, "P12")

# step2 : Load it into a list of DP
datapoints: List[DataPoint] = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

epsilon_table: List[EpsilonDataSet] = []
core_dataset : Dict[EpsilonDataSet] = dict()
noise_dataset : Dict[EpsilonDataSet] = dict()

if __name__=="__main__":
    min_points = int(input("Enter the min points : "))
    epsilon    = float(input("Enter the Epsilon Value : "))

    total_dps  = len(datapoints)
    dimension  = datapoints[0].dimension
    matrix = [ [0] * total_dps for _ in range(total_dps)]
    
    for i in range(total_dps):
        for j in range(total_dps):
            matrix[i][j] = euclidean_formula(datapoints[i], datapoints[j], dimension)
    
    # after getting the matrix, check for the core and noise
    for i in range(total_dps):
        eps_group = EpsilonDataSet(datapoints[i], min_points)
        for j in range(total_dps):
            val = matrix[i][j]
            if val < epsilon:
                eps_group.add(datapoints[j])
        eps_group.finish()
        epsilon_table.append(eps_group)
        if eps_group.type == "CORE":
            eps_group.dp.type = "CORE"
            core_dataset[str(eps_group.dp)] = {
                "obj" : eps_group,
                "points" : set(str(obj) for obj in eps_group.getall())
            }
        else:
            eps_group.dp.type = "NOISE"
            noise_dataset[str(eps_group.dp)] = {
                "obj" : eps_group,
                "points" : set(str(obj) for obj in eps_group.getall())
            }


    print("\n" + "-"* 50 + "\nListing all the groups\n" + "-"* 50)
    for each in epsilon_table:
        print(str(each.dp) + " -->  " + str(each.showall()) + "(" + str(each.showtype()) + ")")

    print("\n" + "-"* 50 + "\nGetting the border values loaded into the Core DPs\n" + "-"* 50)
    # core points extraction
    for each in noise_dataset:
        for dp in core_dataset.values():
            if each in dp['points']:
                print(str(each) + " exist in " + str(dp['obj']))
                dp['obj'].add(noise_dataset[each]['obj'], show = True)
                noise_dataset[each]['obj'].type = "BORDER"

    # Final core table 
    print("\n" + "-"* 50 + "\nListing the final clusters\n" + "-"* 50)
    for each in core_dataset:
        print(str(each) + "  -->  " + str(core_dataset[each]['points']))

    print("\n" + "-"* 50 + "\nFinal Dataset\n" + "-"* 50)
    for each in noise_dataset:
        print("Datapoint : " + str(each) + "  --> Type : " + str(noise_dataset[each]['obj'].type))
