import pandas as pd
df = pd.read_csv("minified.csv", sep=',')
#print df.count()
#print df.head(1).to_string()
#df = df[df.a.isnull()]
print pd.unique(df['CBC: RED BLOOD CELL COUNT'].values.ravel())
#print df.describe()
df.info()
