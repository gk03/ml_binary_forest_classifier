import pandas as pd
df = pd.read_csv("minified.csv", sep=',')
for index, row in df.iterrows():
     #df[row]['PrimaryDiagnosisCode'] = df[row]['PrimaryDiagnosisCode'].split(".",1)[0]
     #print 'index',index,'row',row
     df.loc[index,'PrimaryDiagnosisCode']  = row['PrimaryDiagnosisCode'].split(".",1)[0] 
     #row = row.split(".",1)[0]	
	 #print row[i]	        

df.to_csv('minified_1.csv') 

