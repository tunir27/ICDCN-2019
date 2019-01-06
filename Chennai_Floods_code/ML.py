from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import pandas

#names=['Total no of questions','Average time to solve each questions','No of questions marked for review','No of questions right','Average no of clicks in each page']
dataset = pandas.read_csv("dataset.csv")
#dataset = dataset.apply(pandas.to_numeric,errors='ignore')
##cols.remove('Index')
##cols = dataset.columns
##for col in cols:
##    try:
##        dataset[col] = float(dataset[col])
##    except:
##        pass
array = dataset.values
array=array[1:]
X = array[:,0:5]
Y = array[:,5]
print(X)
print(Y)
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
print("X_train",X_train)
print("Y_train",Y_train)
print("X_validation",X_validation)
print("Y_validation",Y_validation)
seed = 7
scoring = 'accuracy'
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print("Actual Validators",Y_validation)
print("predictions",predictions)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
# make predictions
predictions = model.predict(X_validation)
#prediction = model.predict([[2.8,15,18,180]])
#print("prediction",prediction)
# summarize the fit of the model
print("predictions",predictions)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
