import os
import numpy as np
from sklearn import svm
import joblib
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
def binary_svm_model_training(X_train,y_train,model_path):
    clf = svm.SVC(kernel='rbf', gamma=10, C=10).fit(X_train,y_train)
    joblib.dump(clf, model_path)

def binary_svm_model_testing(X_test,y_test,model_path):
    clf=joblib.load(model_path)
    print (clf.predict(X_test))
    print (clf.score(X_test, y_test))


x_path="training_data/x.npy"
y_path="training_data/y.npy"
X_train_path="training_data/X_train.npy"
X_test_path="training_data/X_test.npy"
y_train_path="training_data/y_train.npy"
y_test_path="training_data/y_test.npy"
model_path="training_data/svm_model"
X=np.load(x_path,allow_pickle=True)
y=np.load(y_path,allow_pickle=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
X_train.dump(X_train_path)
X_test.dump(X_test_path)
y_train.dump(y_train_path)
y_test.dump(y_test_path)


binary_svm_model_training(X_train,y_train,model_path)
binary_svm_model_testing(X_test,y_test,model_path)