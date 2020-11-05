import os
import numpy as np
from sklearn import svm
import joblib
from sklearn.model_selection import cross_val_score
def binary_svm_model_training(X_train,y_train,model_path):
    clf = svm.SVC(kernel='rbf').fit(X_train,y_train)
    joblib.dump(clf, model_path)


x_path="training_data/x.npy"
y_path="training_data/y.npy"
normal_data_set_path="training_data/normal.npy"
abnormal_data_set_path="training_data/abnormal.npy"

X=np.load(x_path,allow_pickle=True)
y=np.load(y_path,allow_pickle=True)
normal=np.load(normal_data_set_path,allow_pickle=True).tolist()
abnormal=np.load(abnormal_data_set_path,allow_pickle=True).tolist()

print (abnormal)