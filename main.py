import numpy as np
from knn import kNN

################ BANANA DATASET ################

# # Opening file
# print("################ BANANA DATASET ################")
# banana_dataset = []
# with open("databases/banana.dat", "r") as file:
#    for line in file:
#       banana_dataset.append(line.split("\n")[0].split(","))

# banana_dataset = np.array(banana_dataset[7:])

# # Moving label to first column
# banana_dataset = banana_dataset[:,[2,0,1]]

# # Dividing dataset
# indices = np.random.permutation(banana_dataset.shape[0])
# training_idx, test_idx = indices[:int(banana_dataset.shape[0]*0.7)], indices[int(banana_dataset.shape[0]*0.7):]
# training_data, test_data = banana_dataset[training_idx,:], banana_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# banana_knn = kNN(training_data,test_data,3)
# print(banana_knn.get_classification())
# print("Accuracy:",banana_knn.get_accuracy())
# # print("Precision:",banana_knn.get_precision())
# # print("Recall:",banana_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# banana_knn = kNN(training_data,test_data,5)
# print(banana_knn.get_classification())
# print("Accuracy:",banana_knn.get_accuracy())
# # print("Precision:",banana_knn.get_precision())
# # print("Recall:",banana_knn.get_recall())

################################################

################ AUSTRALIAN DATASET ################

# # Opening file
# print("################ AUSTRALIAN DATASET ################")
# australian_dataset = []
# with open("databases/australian.dat", "r") as file:
#    for line in file:
#       australian_dataset.append(line.split("\n")[0].split(","))

# australian_dataset = np.array(australian_dataset[19:])

# # Moving label to first column
# labels = [14] + [x for x in range(0,14)]
# australian_dataset = australian_dataset[:,labels]
# # Dividing dataset
# indices = np.random.permutation(australian_dataset.shape[0])
# training_idx, test_idx = indices[:int(australian_dataset.shape[0]*0.7)], indices[int(australian_dataset.shape[0]*0.7):]
# training_data, test_data = australian_dataset[training_idx,:], australian_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# australian_knn = kNN(training_data,test_data,3)
# print(australian_knn.get_classification())
# print("Accuracy:",australian_knn.get_accuracy())
# # print("Precision:",australian_knn.get_precision())
# # print("Recall:",australian_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# australian_knn = kNN(training_data,test_data,5)
# print(australian_knn.get_classification())
# print("Accuracy:",australian_knn.get_accuracy())
# # print("Precision:",australian_knn.get_precision())
# # print("Recall:",australian_knn.get_recall())

################################################

################ IRIS DATASET ################
# # Opening file
# print("################ IRIS DATASET ################")
# iris_dataset = []
# with open("databases/iris.dat", "r") as file:
#    for line in file:
#       iris_dataset.append(line.split("\n")[0].split(","))
# iris_dataset = np.array(iris_dataset[9:])

# # Moving label to first column
# labels = [3] + [x for x in range(0,3)]
# iris_dataset = iris_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(iris_dataset.shape[0])
# training_idx, test_idx = indices[:int(iris_dataset.shape[0]*0.7)], indices[int(iris_dataset.shape[0]*0.7):]
# training_data, test_data = iris_dataset[training_idx,:], iris_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# iris_knn = kNN(training_data,test_data,3)
# print(iris_knn.get_classification())
# print("Accuracy:",iris_knn.get_accuracy())
# # print("Precision:",iris_knn.get_precision())
# # print("Recall:",iris_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# iris_knn = kNN(training_data,test_data,5)
# print(iris_knn.get_classification())
# print("Accuracy:",iris_knn.get_accuracy())
# # print("Precision:",iris_knn.get_precision())
# # print("Recall:",iris_knn.get_recall())

################################################

################ BANDS DATASET ################

# # Opening file
# print("################ BANDS DATASET ################")
# bands_dataset = []
# with open("databases/bands.dat", "r") as file:
#    for line in file:
#       bands_dataset.append(line.split("\n")[0].split(","))
# print(bands_dataset[:25])
# bands_dataset = np.array(bands_dataset[24:])

# # Moving label to first column
# labels = [19] + [x for x in range(0,19)]
# bands_dataset = bands_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(bands_dataset.shape[0])
# training_idx, test_idx = indices[:int(bands_dataset.shape[0]*0.7)], indices[int(bands_dataset.shape[0]*0.7):]
# training_data, test_data = bands_dataset[training_idx,:], bands_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# bands_knn = kNN(training_data,test_data,3)
# print(bands_knn.get_classification())
# print("Accuracy:",bands_knn.get_accuracy())
# # print("Precision:",bands_knn.get_precision())
# # print("Recall:",bands_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# bands_knn = kNN(training_data,test_data,5)
# print(bands_knn.get_classification())
# print("Accuracy:",bands_knn.get_accuracy())
# # print("Precision:",bands_knn.get_precision())
# # print("Recall:",bands_knn.get_recall())

################################################

################ HEART DATASET ################

# # Opening file
# print("################ HEART DATASET ################")
# heart_dataset = []
# with open("databases/heart.dat", "r") as file:
#    for line in file:
#       heart_dataset.append(line.split("\n")[0].split(","))
# heart_dataset = np.array(heart_dataset[18:])

# # Moving label to first column
# labels = [13] + [x for x in range(0,13)]
# heart_dataset = heart_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(heart_dataset.shape[0])
# training_idx, test_idx = indices[:int(heart_dataset.shape[0]*0.7)], indices[int(heart_dataset.shape[0]*0.7):]
# training_data, test_data = heart_dataset[training_idx,:], heart_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# heart_knn = kNN(training_data,test_data,3)
# print(heart_knn.get_classification())
# print("Accuracy:",heart_knn.get_accuracy())
# # print("Precision:",heart_knn.get_precision())
# # print("Recall:",heart_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# heart_knn = kNN(training_data,test_data,5)
# print(heart_knn.get_classification())
# print("Accuracy:",heart_knn.get_accuracy())
# # print("Precision:",heart_knn.get_precision())
# # print("Recall:",heart_knn.get_recall())

################################################

################ HABERMAN DATASET ################
# # Opening file
# print("################ HABERMAN DATASET ################")
# haberman_dataset = []
# with open("databases/haberman.dat", "r") as file:
#    for line in file:
#       haberman_dataset.append(line.split("\n")[0].split(","))
# haberman_dataset = np.array(haberman_dataset[8:])

# # Moving label to first column
# labels = [3] + [x for x in range(0,3)]
# haberman_dataset = haberman_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(haberman_dataset.shape[0])
# training_idx, test_idx = indices[:int(haberman_dataset.shape[0]*0.7)], indices[int(haberman_dataset.shape[0]*0.7):]
# training_data, test_data = haberman_dataset[training_idx,:], haberman_dataset[test_idx,:]
# print(test_data.size)
# # KNN 3
# print("KNN, K=3")
# haberman_knn = kNN(training_data,test_data,3)
# print(haberman_knn.get_classification())
# print("Accuracy:",haberman_knn.get_accuracy())
# # print("Precision:",haberman_knn.get_precision())
# # print("Recall:",haberman_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# haberman_knn = kNN(training_data,test_data,5)
# print(haberman_knn.get_classification())
# print("Accuracy:",haberman_knn.get_accuracy())
# # print("Precision:",haberman_knn.get_precision())
# # print("Recall:",haberman_knn.get_recall())

################################################

################ THYROID DATASET ################
# # Opening file
# print("################ THYROID DATASET ################")
# thyroid_dataset = []
# with open("databases/thyroid.dat", "r") as file:
#    for line in file:
#       thyroid_dataset.append(line.split("\n")[0].split(","))
# thyroid_dataset = np.array(thyroid_dataset[27:])

# # Moving label to first column
# labels = [21] + [x for x in range(0,21)]
# thyroid_dataset = thyroid_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(thyroid_dataset.shape[0])
# training_idx, test_idx = indices[:int(thyroid_dataset.shape[0]*0.7)], indices[int(thyroid_dataset.shape[0]*0.7):]
# training_data, test_data = thyroid_dataset[training_idx,:], thyroid_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# thyroid_knn = kNN(training_data,test_data,3)
# print(thyroid_knn.get_classification())
# print("Accuracy:",thyroid_knn.get_accuracy())
# # print("Precision:",thyroid_knn.get_precision())
# # print("Recall:",thyroid_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# thyroid_knn = kNN(training_data,test_data,5)
# print(thyroid_knn.get_classification())
# print("Accuracy:",thyroid_knn.get_accuracy())
# # print("Precision:",thyroid_knn.get_precision())
# # print("Recall:",thyroid_knn.get_recall())

################################################

################ appendicitis DATASET ################
# Opening file
# print("################ appendicitis DATASET ################")
# appendicitis_dataset = []
# with open("databases/appendicitis.dat", "r") as file:
#    for line in file:
#       appendicitis_dataset.append(line.split("\n")[0].split(","))
# appendicitis_dataset = np.array(appendicitis_dataset[12:])

# # Moving label to first column
# labels = [7] + [x for x in range(0,7)]
# appendicitis_dataset = appendicitis_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(appendicitis_dataset.shape[0])
# training_idx, test_idx = indices[:int(appendicitis_dataset.shape[0]*0.7)], indices[int(appendicitis_dataset.shape[0]*0.7):]
# training_data, test_data = appendicitis_dataset[training_idx,:], appendicitis_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# appendicitis_knn = kNN(training_data,test_data,3)
# print(appendicitis_knn.get_classification())
# print("Accuracy:",appendicitis_knn.get_accuracy())
# print("Precision:",appendicitis_knn.get_precision())
# print("Recall:",appendicitis_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# appendicitis_knn = kNN(training_data,test_data,5)
# print(appendicitis_knn.get_classification())
# print("Accuracy:",appendicitis_knn.get_accuracy())
# print("Precision:",appendicitis_knn.get_precision())
# print("Recall:",appendicitis_knn.get_recall())

################################################

################ titanic DATASET ################
# # Opening file
# print("################ titanic DATASET ################")
# titanic_dataset = []
# with open("databases/titanic.dat", "r") as file:
#    for line in file:
#       titanic_dataset.append(line.split("\n")[0].split(","))
# titanic_dataset = np.array(titanic_dataset[8:])

# # Moving label to first column
# labels = [3] + [x for x in range(0,3)]
# titanic_dataset = titanic_dataset[:,labels]

# # Dividing dataset
# indices = np.random.permutation(titanic_dataset.shape[0])
# training_idx, test_idx = indices[:int(titanic_dataset.shape[0]*0.7)], indices[int(titanic_dataset.shape[0]*0.7):]
# training_data, test_data = titanic_dataset[training_idx,:], titanic_dataset[test_idx,:]

# # KNN 3
# print("KNN, K=3")
# titanic_knn = kNN(training_data,test_data,3)
# print(titanic_knn.get_classification())
# print("Accuracy:",titanic_knn.get_accuracy())
# # print("Precision:",titanic_knn.get_precision())
# # print("Recall:",titanic_knn.get_recall())

# # KNN 5
# print("KNN, K=5")
# titanic_knn = kNN(training_data,test_data,5)
# print(titanic_knn.get_classification())
# print("Accuracy:",titanic_knn.get_accuracy())
# # print("Precision:",titanic_knn.get_precision())
# # print("Recall:",titanic_knn.get_recall())

################################################

################ winequality_red DATASET ################

# Opening file
print("################ winequality_red DATASET ################")
winequality_red_dataset = []
with open("databases/winequality-red.dat", "r") as file:
   for line in file:
      winequality_red_dataset.append(line.split("\n")[0].split(","))
winequality_red_dataset = np.array(winequality_red_dataset[16:])

# Moving label to first column
labels = [11] + [x for x in range(0,11)]
winequality_red_dataset = winequality_red_dataset[:,labels]

# Dividing dataset
indices = np.random.permutation(winequality_red_dataset.shape[0])
training_idx, test_idx = indices[:int(winequality_red_dataset.shape[0]*0.7)], indices[int(winequality_red_dataset.shape[0]*0.7):]
training_data, test_data = winequality_red_dataset[training_idx,:], winequality_red_dataset[test_idx,:]

# KNN 3
print("KNN, K=3")
winequality_red_knn = kNN(training_data,test_data,3)
print(winequality_red_knn.get_classification())
print("Accuracy:",winequality_red_knn.get_accuracy())
print("Precision:",winequality_red_knn.get_precision())
print("Recall:",winequality_red_knn.get_recall())

# KNN 5
print("KNN, K=5")
winequality_red_knn = kNN(training_data,test_data,5)
print(winequality_red_knn.get_classification())
print("Accuracy:",winequality_red_knn.get_accuracy())
print("Precision:",winequality_red_knn.get_precision())
print("Recall:",winequality_red_knn.get_recall())

################################################


