import pandas as pd
head = ["CBC: RED BLOOD CELL COUNT","METABOLIC: AST/SGOT","CBC: NEUTROPHILS","CBC: HEMOGLOBIN","CBC: BASOPHILS","METABOLIC: CALCIUM","CBC: RDW","METABOLIC: CHLORIDE","CBC: EOSINOPHILS","METABOLIC: TOTAL PROTEIN","METABOLIC: POTASSIUM","METABOLIC: ALT/SGPT","CBC: ABSOLUTE NEUTROPHILS","CBC: MEAN CORPUSCULAR VOLUME","CBC: MONOCYTES","URINALYSIS: WHITE BLOOD CELLS","CBC: LYMPHOCYTES","CBC: HEMATOCRIT","URINALYSIS: PH","METABOLIC: SODIUM","CBC: MCHC","CBC: PLATELET COUNT","URINALYSIS: RED BLOOD CELLS","CBC: WHITE BLOOD CELL COUNT","METABOLIC: CARBON DIOXIDE","CBC: MCH","METABOLIC: CREATININE","METABOLIC: BILI TOTAL","CBC: ABSOLUTE LYMPHOCYTES","METABOLIC: ALBUMIN","METABOLIC: BUN","METABOLIC: ANION GAP","METABOLIC: ALK PHOS","METABOLIC: GLUCOSE","URINALYSIS: SPECIFIC GRAVITY","PrimaryDiagnosisCode","PatientRace","PatientMaritalStatus","PatientGender","PatientLanguage","PatientPopulationPercentageBelowPoverty"]
df = pd.read_csv("db.csv", sep=',')
df = df[df.a.isnull()]
df.PatientRace.replace(['White', 'Unknown', 'Asian', 'African American'], [1, 0,2,3], inplace=True)
df.PatientLanguage.replace(['English', 'Icelandic', 'Spanish', 'Unknown'], [1, 2,3,0], inplace=True)
df.PatientMaritalStatus.replace(['Unknown', 'Married', 'Widowed', 'Single', 'Divorced', 'Separated'], [0, 1,2,3,4,5], inplace=True)
df.PatientGender.replace(['Female', 'Male'], [0,1], inplace=True)
df.to_csv('minified.csv', columns = head)
