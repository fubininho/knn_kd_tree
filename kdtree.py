import numpy as np
import heapq

class KdTree:
   def __init__(self, data):
      self.kdtree = self.constructor(data)

   #TODO : tratar quando divide a base em dois
   #TODO: colocar label como posição 0
   def constructor(self, data, current_dimension=0):
      if len(data) == 0:
         pass
      elif len(data) == 1:
         return {
            "division_value": None,
            "current_dimension": current_dimension,
            "label": data[0][0],
            "left": None,
            "right": None,
            # "visited": False,
            "point": data[0][1:]
         }
      else:
         np.argsort(data[:, current_dimension])
         division = (len(data) // 2) - 1
         return {
            "division_value": data[division][current_dimension],
            "current_dimension": current_dimension,
            "label": None,
            "left": self.constructor(data[:division], (current_dimension+1) % (data.shape[1]-1)),
            "right": self.constructor(data[division+1:], (current_dimension+1) % (data.shape[1]-1)),
            # "visited": False,
            "point": None
         }


   def k_nearest(self, k, point):
      priority_queue = []
      current_node = self.kdtree
      first_node = self.kdtree
      #set distance
      while current_node["division_value"] != None:
         if (point[current_node["current_dimension"]]) < current_node["division_value"]:
            if current_node["left"] != None:
               current_node = current_node["left"]
            else:
               current_node = current_node["right"]
         else:
            # right
            if current_node["right"] != None:
               current_node = current_node["right"]
            else:
               current_node = current_node["left"]

      distance = self.__distance(point,current_node["point"])
      heapq.heappush(priority_queue, (-distance,current_node["label"])) 
      
      range_wanted = np.array([point.astype(float)-distance,point.astype(float)+distance])
      all_leaves = self.get_all_leaves(k,self.search(self.kdtree, range_wanted),point,priority_queue)
      labels = [x[1] for x in all_leaves]
      return labels
      
   def search(self, root, range_wanted):
      if root["division_value"] == None:
         return root
      # se false true => intersepta -> retorna nó, se true true esquerda, se false false direita
      elif True in [True for x in range_wanted[:,root["left"]["current_dimension"]] if x < float(root["left"]["division_value"])]:
         if [True for x in range_wanted[:,root["left"]["current_dimension"]] if x < float(root["left"]["division_value"])] == [True, True]:
            return self.search(root["left"], range_wanted)
         else:
            return root  
      else:
         if [True for x in range_wanted[:,root["right"]["current_dimension"]] if x < float(root["right"]["division_value"])] == [True, True]:
            return self.search(root["right"], range_wanted)
         else:
            return root

   def get_all_leaves(self, k, root, point, priority_queue):
      if root["division_value"] == None:
         distance = self.__distance(point,root["point"])
         if len(priority_queue) < k:
            heapq.heappush(priority_queue, (-distance,root["label"]))
         elif distance < -priority_queue[0][0]:
            heapq.heappushpop(priority_queue, (-distance, root["label"]))
      else:
         if root["left"] != None:
            self.get_all_leaves(k, root["left"], point, priority_queue)
         if root["right"] != None:
            self.get_all_leaves(k, root["right"], point, priority_queue)
      return priority_queue


   def __distance(self,point_a,point_b):
      return np.linalg.norm(point_a.astype(float)-point_b.astype(float))
      
      
