
from typing import List, Tuple

# This algorithm is written for K means algorithm static K = 2

class Point:
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val 
        self.min_distance = 0
        self.group = None

    def __str__(self):
        return "Point (" + str(self.x) + ", " + str(self.y) + ")"

def convert_dataset_to_points(dataset: List[List]) -> List[Point]:  # static code for K means where k = 2
    index = 0
    total_records = len(dataset[0])

    # Points list
    points = []

    while index < total_records:
        x = dataset[0][index]
        y = dataset[1][index]
        point = Point(x, y)
        points.append(point)
        index += 1
    
    return points

def get_initial_centroid(datapoints: List[Point]) -> tuple:
    first = datapoints[0]
    last = datapoints[len(datapoints)-1]
    return (first, last)

def get_distance_of_all_points(centroid : Tuple[Point], datapoints : List[Point]) -> Tuple :
    A = centroid[0]
    B = centroid[1]

    for each_point in datapoints:
        dx = each_point.x
        dy = each_point.y

        acx = A.x
        acy = A.y

        bcx = B.x
        bcy = B.y

        # finding the distance from A
        d_A = ( (acy - dy)**2 + (acx - dx)**2 ) ** 0.5

        # finding the distance from B
        d_B = ( (bcy - dy)**2 + (bcx - dx)**2 ) ** 0.5

        if d_A < d_B:
            each_point.min_distance = d_A
            each_point.group = "A"
        else:
            each_point.min_distance = d_B
            each_point.group = "B"

    # Finding the new centroid:
    A_new_c_x = 0
    A_new_c_y = 0
    at = 0

    B_new_c_x = 0
    B_new_c_y = 0
    bt = 0

    for each_point in datapoints:
        if each_point.group == "A":
            A_new_c_x += each_point.x
            A_new_c_y += each_point.y
            at += 1
        else:
            B_new_c_x += each_point.x
            B_new_c_y += each_point.y
            bt += 1
    
    A_new_c_x = A_new_c_x / at
    A_new_c_y = A_new_c_y / at

    B_new_c_x = B_new_c_x / bt
    B_new_c_y = B_new_c_y / bt

    print("New centroid detected : Points(" + str(A_new_c_x) + ", " 
          + str(A_new_c_y) + "), Points(" + str(B_new_c_x) + ", " + str(B_new_c_y) + ")")

    return (Point(A_new_c_x, A_new_c_y), Point(B_new_c_x, B_new_c_y))


def display_groups(dataset : List[Point]) -> None:
    A = []
    B = []
    for each in dataset:
        if each.group == "A": 
            A.append(each)
        else:
            B.append(each)
    
    print("A GROUP : " + "*"*10)
    for each in A:
        print(each)
    
    print("-" * 20)

    print("B GROUP : " + "*"*10)
    for each in B:
        print(each) 
    


if __name__ == "__main__":

    age = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
           33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
           53, 55, 57, 59, 60, 61, 62, 63, 64, 65]
    salary = [18000, 19000, 20500, 22000, 25000, 27000, 30000, 33000, 45000, 47000,
              50000, 55000, 60000, 65000, 70000, 76000, 82000, 88000, 92000, 98000,
              102000, 108000, 114000, 100000, 120000, 130000, 145000, 160000, 175000, 200000]

    dataset = [age, salary]

    centroid : tuple = None

    # Step 0 - Getting all the datasets into a data points
    points = convert_dataset_to_points(dataset=dataset)

    # Step 1 - getting the initial centroid value
    centroid = get_initial_centroid(points)
    
    index = 50
    while index > 0:
        # Step 2 - Find ther distance of all the other points
        new_centroid = get_distance_of_all_points(centroid=centroid, datapoints=points)

        # Step 3: Display the groups:
        display_groups(dataset=points)

        index -= 1