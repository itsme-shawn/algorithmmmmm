from math import sqrt

def distance(coord1, coord2):
  return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 )

def closest_pair(coords):
  min_result = distance(coords[0],coords[1])
  min_list = [coords[0], coords[1]]
  for i in range(len(coords)-1):
    for j in range(i+1, len(coords)):
      if(distance(coords[i],coords[j]) < min_result):
        min_result = distance(coords[i],coords[j])
        min_list = [coords[i], coords[j]]
  return min_list    
      

test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))