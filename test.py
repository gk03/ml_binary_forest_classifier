from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

#Load the iris flower data set
extracted_data = datasets.load_iris()
figures = extracted_data

#Insert a Bayesian model into the data
classification_model = GaussianNB()
classification_model.fit(figures.data, figures.target)
print(classification_model)

#Produce estimations
forecast = figures.target
estimate = classification_model.predict(figures.data)

#Summarize the fit of the model
print(metrics.classification_report(forecast, estimate))
print(metrics.confusion_matrix(forecast, estimate))
