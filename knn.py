import numpy as np
from kdtree import KdTree

class kNN:
   def __init__(self, training, test, k):
      self.kdtree = KdTree(training)
      self.k = k
      self.test_classification = self.__set_classification(test)
      self.confusion_matrix = self.__set_confusion_matrix(np.unique(training[:,0]))
      self.accuracy = self.__set_accuracy()
      self.precision = self.__set_precision()
      self.recall = self.__set_recall()
      
   def __set_classification(self, test):
      return np.apply_along_axis(self.__set_point_classification, axis=1, arr=test)

   def __set_point_classification(self, point):
      # print("start")
      labels = self.kdtree.k_nearest(self.k, point[1:])
      # print(labels)
      values, counts = np.unique(labels, return_counts=True)
      label = values[np.argmax(counts)]
      # print(label)
      return {
         "Point": point,
         "Label": label,
         "ActualLabel": point[0],
         "Correct": label == point[0],
      }

   def __set_accuracy(self):
      return np.sum(self.confusion_matrix.diagonal())/len(self.test_classification)
      # corrects = 0
      # for point in self.test_classification:
      #    if point["Correct"]:
      #       corrects += 1
      # return corrects/len(self.test_classification)

   def __set_confusion_matrix(self,labels):
      confusion_matrix = np.zeros([len(labels),len(labels)])
      for point in self.test_classification:
         if point["Correct"]:
            confusion_matrix[list(labels).index(point["Label"]),list(labels).index(point["Label"])] += 1
         else:
            confusion_matrix[list(labels).index(point["ActualLabel"]),list(labels).index(point["Label"])] += 1
            confusion_matrix[list(labels).index(point["Label"]),list(labels).index(point["ActualLabel"])] += 1
      return confusion_matrix
   
   # true positives / (true positives + false positives)
   def __set_precision(self):
      return np.diag(self.confusion_matrix)/np.sum(self.confusion_matrix,axis=0)

   # true positives / (true positives + false negatives)
   def __set_recall(self):
      return np.diag(self.confusion_matrix)/np.sum(self.confusion_matrix,axis=1)

   def get_classification(self):
      return self.test_classification

   def get_accuracy(self):
      return self.accuracy 

   def get_precision(self):
      return self.precision

   def get_recall(self):
      return self.recall