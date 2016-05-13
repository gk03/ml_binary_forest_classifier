import pandas as pd
from sklearn import metrics
#from sklearn.linear_model import LogisticRegression
#from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
#from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn import datasets

#Load the iris flower data set
#iris = datasets.load_iris()
#X, y = iris.data, iris.target

head = ["CBC: RED BLOOD CELL COUNT","METABOLIC: AST/SGOT","CBC: NEUTROPHILS","CBC: HEMOGLOBIN","CBC: BASOPHILS","METABOLIC: CALCIUM","CBC: RDW","METABOLIC: CHLORIDE","CBC: EOSINOPHILS","METABOLIC: TOTAL PROTEIN","METABOLIC: POTASSIUM","METABOLIC: ALT/SGPT","CBC: ABSOLUTE NEUTROPHILS","CBC: MEAN CORPUSCULAR VOLUME","CBC: MONOCYTES","URINALYSIS: WHITE BLOOD CELLS","CBC: LYMPHOCYTES","CBC: HEMATOCRIT","URINALYSIS: PH","METABOLIC: SODIUM","CBC: MCHC","CBC: PLATELET COUNT","URINALYSIS: RED BLOOD CELLS","CBC: WHITE BLOOD CELL COUNT","METABOLIC: CARBON DIOXIDE","CBC: MCH","METABOLIC: CREATININE","METABOLIC: BILI TOTAL","CBC: ABSOLUTE LYMPHOCYTES","METABOLIC: ALBUMIN","METABOLIC: BUN","METABOLIC: ANION GAP","METABOLIC: ALK PHOS","METABOLIC: GLUCOSE","URINALYSIS: SPECIFIC GRAVITY","PatientRace","PatientMaritalStatus","PatientGender","PatientLanguage","PatientPopulationPercentageBelowPoverty"]

df = pd.read_csv("minified_1.csv", sep=',')

X = df[head]
y = df['PrimaryDiagnosisCode']

#spit data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

#Insert a Bayesian model into the data
classification_model = DecisionTreeClassifier()
#classification_model = GaussianNB()
#classification_model = LogisticRegression()
#classification_model = RandomForestClassifier(max_depth=50, min_samples_leaf=2, min_samples_split=3, n_estimators=50)

classification_model.fit(X_train, y_train)
print(classification_model)

#Produce estimations
forecast = y_test
estimate = classification_model.predict(X_test)

#Summarize the fit of the model
print(metrics.classification_report(forecast, estimate))
print(metrics.confusion_matrix(forecast, estimate))
