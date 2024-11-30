import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

data_raw = pd.read_csv('Data/drug.csv')


X = data_raw.drop('Drug', axis=1).values
y = data_raw.Drug.values

columns_to_encode = [1, 2, 3]

encoder = OrdinalEncoder()
X[:, columns_to_encode] = encoder.fit_transform(X[:, columns_to_encode])
y = encoder.fit_transform(y.reshape(-1, 1)).reshape(-1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=3, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))

with open("./Results/metrics.txt", "w") as f:
    f.write(str(accuracy_score(y_test, y_pred)))


with open('./Model/model.pkl', 'wb') as f:
    joblib.dump(model, './Model/model.pkl')
    joblib.dump(encoder, './Model/encoder.pkl')


