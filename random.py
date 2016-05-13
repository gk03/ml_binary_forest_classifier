from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn import datasets

#Load the iris flower data set
iris = datasets.load_iris()
X, y = iris.data, iris.target

#spit data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

#Insert a Bayesian model into the data
classification_model = RandomForestClassifier()
classification_model.fit(X_train, y_train)
print(classification_model)

#Produce estimations
forecast = X_test 
estimate = classification_model.predict(y_test)

#Summarize the fit of the model
print(metrics.classification_report(forecast, estimate))
print(metrics.confusion_matrix(forecast, estimate))
