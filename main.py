%pip install seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("online_shoppers_intention.csv")

df.info()

from sklearn.compose import make_column_selector
df["Weekend"]=df["Weekend"].astype(int)
df["Revenue"]=df["Revenue"].astype(int)
string_cols=make_column_selector(dtype_include=["str","object","category"])(df)
encoded=pd.get_dummies(df,columns=string_cols,dtype=int)

encoded.info()

X=encoded.drop("Revenue",axis=1)
y=encoded["Revenue"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
log.fit(X_train_scaled,y_train)
y_pred_log=log.predict(X_test_scaled)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
accuracy_log=accuracy_score(y_test,y_pred_log)
print("Accuracy Score:",accuracy_log)
confusion_log=confusion_matrix(y_test,y_pred_log)
print("Confusion Matrix:\n",confusion_log)
classification_log=classification_report(y_test,y_pred_log)
print("Classification Report:\n",classification_log)

from sklearn.ensemble import RandomForestClassifier
rand=RandomForestClassifier()
rand.fit(X_train_scaled,y_train)
y_pred_rand=rand.predict(X_test_scaled)

from sklearn.metrics import precision_score,recall_score,f1_score,confusion_matrix
precision=precision_score(y_test,y_pred_rand)
recall=recall_score(y_test,y_pred_rand)
f1=f1_score(y_test,y_pred_rand)
confusion=confusion_matrix(y_test,y_pred_rand)
print("Precision:",precision)
print("Recall:",recall)
print("F1-score:",f1)
print("Confusion Matrix:",confusion)

from sklearn.ensemble import GradientBoostingClassifier
grad=GradientBoostingClassifier()
grad.fit(X_train_scaled,y_train)
y_pred_grad=grad.predict(X_test_scaled)

accuracy_grad=accuracy_score(y_test,y_pred_grad)
print("Accuracy Score:",accuracy_grad)
confusion_grad=confusion_matrix(y_test,y_pred_grad)
print("Confusion Matrix:\n",confusion_grad)
classification_grad=classification_report(y_test,y_pred_grad)
print("Classification Report:\n",classification_grad)
