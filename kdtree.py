import numpy as np

class KdTree:
   def __init__(self, data):
      self.kdtree = self.constructor(data)

   def constructor(self, data, current_dimension=1):
      if len(data) == 0:
         pass
      elif len(data) == 1:
         return {
            "division_value": None,
            "current_dimension": int(current_dimension),
            "label": data[0][0],
            "left": None,
            "right": None,
            # "visited": False,
            "point": data[0][1:]
         }
      else:
         np.argsort(data[:, current_dimension])
         division = (len(data) // 2) - 1
         if current_dimension % data.shape[1] == 0:
            current_dimension += 1
         return {
            "division_value": float(data[division][current_dimension]),
            "current_dimension": int(current_dimension),
            "label": None,
            "left": self.constructor(data[:division], (current_dimension) % (data.shape[1])),
            "right": self.constructor(data[division+1:], (current_dimension) % (data.shape[1])),
            # "visited": False,
            "point": None
         }

   def k_nearest(self, k, point,current_node,priority_queue=[]):
      if current_node["division_value"] == None:
         distance = self.__distance(point,current_node["point"])
         if len(priority_queue) < k:
            priority_queue.append((-distance,(current_node["point"],current_node["label"])))
            priority_queue = sorted(priority_queue, key=getKey)
         elif abs(distance) < abs(priority_queue[0][0]):
            priority_queue.pop()
            priority_queue.append((-distance,(current_node["point"],current_node["label"])))
            priority_queue = sorted(priority_queue, key=getKey)

         return priority_queue
      
      next_node = None
      opposite_node = None
      if float(point[current_node["current_dimension"]]) > current_node["division_value"]:
         next_node = current_node["right"]
         opposite_node = current_node["left"]
      else:
         next_node = current_node["left"]
         opposite_node = current_node["right"]

      no_next_node = False
      if next_node == None:
         no_next_node = True
         next_node = opposite_node
      if opposite_node == None:
         no_next_node = True

      priority_queue = self.k_nearest(k,point,next_node,priority_queue)
      if not no_next_node and (
         len(priority_queue) < k or (
            float(priority_queue[0][1][0][current_node["current_dimension"]]) < abs(float(point[current_node["current_dimension"]]) - current_node["division_value"])
         )
      ):
         priority_queue = self.k_nearest(k,point,opposite_node,priority_queue)
      return priority_queue

   def __distance(self,point_a,point_b):
      return abs(np.linalg.norm(point_a.astype(float)-point_b.astype(float)))
   
   def get_tree(self):
      return self.kdtree
      
      
def getKey(item):
   return item[0]