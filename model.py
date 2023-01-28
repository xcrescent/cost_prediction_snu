import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

df1 = pd.read_excel('Dataset_Hackathon.xlsx')
df1.head()

# Features
X = df1.drop(['Country', 'Commodity','Flow','Category','Frieght Cost (USD)'], axis = 1)
X.head()

y = df1['Frieght Cost (USD)']

rf=RandomForestRegressor()
rf.fit(X,y)
pred=rf.predict(X)

print('Mean Absolute Error:', metrics.mean_absolute_error(y, pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y, pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y, pred)))
print('R2:', np.sqrt(metrics.r2_score(y, pred)))

def predict(q,v,d):
    features = [[q,v,d]]
    return rf.predict(features)[0]