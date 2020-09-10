import json
from os import listdir
import os.path as osp
import cv2 as cv
import random
import numpy as np

def load_zone_anno(json_filename):
  """
  Load the json with ROI and MOI annotation.

  """
  with open(json_filename) as jsonfile:
    dd = json.load(jsonfile)
    polygon = [(int(x), int(y)) for x, y in dd['shapes'][0]['points']]
    paths = {}
    for it in dd['shapes'][1:]:
      kk = str(int(it['label'][-2:]))
      paths[kk] = [(int(x), int(y)) for x, y
              in it['points']]
  return polygon, paths

# Idea:  
# 1) Draw a horizontal line to the right of each point and extend it to infinity

# 2) Count the number of times the line intersects with polygon edges.

# 3) A point is inside the polygon if either count of intersections is odd or
#    point lies on an edge of polygon.  If none of the conditions is true, then 
#    point lies outside.

# Given three colinear points p, q, r, the function checks if 
# point q lies on line segment 'pr' 
def onSegment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True 
    return False 


# To find orientation of ordered triplet (p, q, r). 
# The function returns following values 
# 0 --> p, q and r are colinear 
# 1 --> Clockwise 
# 2 --> Counterclockwise 
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
  
    # colinear 
    if (val == 0):
      return 0        

    # clock or counterclock wise 
    if (val > 0):
      return 1
    else:
      return 2

def is_intersect(p1, q1, p2, q2):
  # Find the four orientations needed for general and special cases 
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    # General case 
    if (o1 != o2 and o3 != o4):
        return True 
  
    # Special Cases 
    # p1, q1 and p2 are colinear and p2 lies on segment p1q1 
    if (o1 == 0 and onSegment(p1, p2, q1)):
      return True
  
    # p1, q1 and p2 are colinear and q2 lies on segment p1q1 
    if (o2 == 0 and onSegment(p1, q2, q1)):
      return True
  
    # p2, q2 and p1 are colinear and p1 lies on segment p2q2 
    if (o3 == 0 and onSegment(p2, p1, q2)):
      return True 
  
    # p2, q2 and q1 are colinear and q1 lies on segment p2q2 
    if (o4 == 0 and onSegment(p2, q1, q2)):
      return True
  
    return False # Doesn't fall in any of the above cases

def is_point_in_polygon(polygon, point):
  # Create a point for line segment from p to infinite 
  extreme = [point[0], 1e9]

  # Count intersections of the above line with sides of polygon 
  count = 0
  i = 0

  while True:
    j = (i+1) % len(polygon)

    # Check if the line segment from 'p' to 'extreme' intersects 
        # with the line segment from 'polygon[i]' to 'polygon[j]'
    if is_intersect(polygon[i], polygon[j], point, extreme):
      # If the point 'p' is colinear with line segment 'i-j', 
      # then check if it lies on segment. If it lies, return true, 
      # otherwise false 
      if orientation(polygon[i], point, polygon[j])==0:
        return onSegment(polygon[i], point, polygon[j])
      count = count + 1

    i = j
    if i==0:
      break
  
  return count % 2 == 1

# use this function to check if a bounding box is inside the polygon 
def is_bounding_box_intersect(bounding_box, polygon):
  for i in range(len(bounding_box)):
    if is_point_in_polygon(polygon, bounding_box[i]):
      return True
  return False


def check_bbox_intersect_polygon(polygon, bbox):
  """
  
  Args:
    polygon: List of points (x,y)
    bbox: A tuple (xmin, ymin, xmax, ymax)
  
  Returns:
    True if the bbox intersect the polygon
  """
  x1, y1, x2, y2 = bbox
  bb = [(x1,y1), (x2, y1), (x2,y2), (x1,y2)]
  return is_bounding_box_intersect(bb, polygon)

def cosin_similarity(a2d, b2d):
  
  a = np.array((a2d[1][0] - a2d[0][0], a2d[1][1] - a2d[0][1]))
  b = np.array((b2d[1][0] - b2d[0][1], b2d[1][1] - b2d[1][0]))
  return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

def counting_moi(paths, moto_vector_list):
  """
  Args:
    paths: List of MOI - (first_point, last_point)
    moto_vector_list: List of tuples (first_point, last_point, last_frame_id) 
  
  Returns:
    A list of tuples (frame_id, movement_id, vehicle_class_id)
  """
  moi_detection_list = []
  for moto_vector in moto_vector_list:
    max_cosin = -2
    movement_id = ''
    last_frame = 0
    for movement_label, movement_vector in paths.items(): 
      cosin = cosin_similarity(movement_vector, moto_vector)
      if cosin > max_cosin:
        max_cosin = cosin
        movement_id = int(movement_label)
        last_frame = moto_vector[2]
    
    if not movement_id in moto_vector[4]:
      continue 

    moi_detection_list.append((last_frame, movement_id, moto_vector[3]))
  return moi_detection_list

class_type = {}
class_type[1] = 1 
class_type[2] = 1 
class_type[3] = 1
class_type[5] = 2
class_type[6] = 2
class_type[7] = 2
class_type[8] = 2
class_type[9] = 3
class_type[10] = 3
class_type[11] = 4
class_type[12] = 4
class_type[13] = 4      

def extend(x):
  while len(x) < 2:
    x = '0' + x
  return x

def load_json_region():
  ret = []
  for i in range(1,26):
    path = '../../DATA/ROI_info/cam_{}.json'.format(extend(str(i)))
    file = open(path,'r')
    data = json.load(file)
    ls = []
    for data_instance in data['shapes']:
      dir = data_instance['label']
      point = data_instance['points']
      for j in range(len(point)):
        point[j] = [int(x) for x in point[j]]
      dir = [int(x) for x in dir.split(',')]
      ls.append((point, dir))
    ret.append(ls)
  return ret

polygon_info = load_json_region()
result_filename = '/data/submission_output/submission.txt'
for cam in (1,26):
  index = cam
  cam = str(cam)
  json_path = '/data/test_data/cam_' + extend(str(cam)) + '.json'
  polygon, paths = load_zone_anno(json_path)
  path = '/home/aic_team082/DATA/hypothesis/cam_' + extend(str(cam)) + '.txt' 
  tracker_id = []
  with open(path,'r') as f:
    hypotheses = []
    for line in f.readlines():
      a = line.split(",")
      obj_id = a[1]
      hypotheses.append(a)
      tracker_id.append(obj_id)
  tracker_id = list(set(tracker_id))
  tracker_id.sort()
  
  tracks = []
  for item in tracker_id:
    temp = []
    class_tmp = []
    for det in hypotheses:
      if det[1] == item:
        temp.append(tuple(det[2:6]+[det[0]]))
        class_tmp.append(int(det[7]))
    temp.append(max(set(class_tmp),key = class_tmp.count))
    for i in range(len(temp)-1):
      temp[i] = [int(float(x)) for x in temp[i]]
    temp[-1] = int(temp[-1])
    tracks.append(temp)

  vehicle_vector_list = []
  
  cnt = 0
  for track in tracks:
    satisfied_direction = set()
    class_id = track[-1]
    if int(class_id) == 0 or int(class_id) == 4:
      continue
    will_add = False
    for i in range(len(track)-1):
      for polygon, dir in polygon_info[index - 1]:
        if check_bbox_intersect_polygon(polygon, (track[i][0], track[i][1], track[i][0] + track[i][2], track[i][1] + track[i][2])):
          will_add = True
          for dir_id in dir:
            satisfied_direction.add(dir_id)
    
    if will_add == False:
        continue
    
    if len(track) <= 2:
      continue
    
    
    first = track[0]
    last = track[-2]
    first = [float(item) for item in first]
    last = [float(item) for item in last]
    first_point = (first[0] + first[2]/2, first[1] + first[3]/2)
    last_point = (last[0] + last[2]/2, last[1] + last[3]/2)
  
    vehicle_vector_list.append((first_point, last_point, last[4], class_type[int(class_id)],satisfied_direction))

  moi_detections = counting_moi(paths, vehicle_vector_list)
  video_id = 'cam_' + extend(str(cam))
  final_res = []
  for frame_id, movement_id, vehicle_class_id in moi_detections:
    final_res.append(' '.join([video_id, int(frame_id), movement_id, vehicle_class_id]))
  if cam == '17':
    for fr in range(1,13480,4):
      final_res.append('cam_17 {} 2 1'.format(str(fr)))
  with open(result_filename, 'w') as result_file:
    result_file.write('\n'.join(final_res))
    # for frame_id, movement_id, vehicle_class_id in moi_detections:
    #   #result_file.write('{} {}\n'.format(movement_id, vehicle_class_id))
    #   result_file.write('{} {} {} {}\n'.format(video_id, int(frame_id), movement_id, vehicle_class_id))