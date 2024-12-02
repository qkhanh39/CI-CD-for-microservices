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


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train[: , columns_to_encode] = encoder.fit_transform(X_train[:, columns_to_encode])

model = RandomForestClassifier(n_estimators=3, random_state=42)
model.fit(X_train, y_train)

X_test[:, columns_to_encode] = encoder.transform(X_test[:, columns_to_encode])
y_pred = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, y_pred))

with open("./Results/metrics.txt", "w") as f:
    f.write(str(accuracy_score(y_test, y_pred)))


with open('./Model/model.pkl', 'wb') as f:
    joblib.dump(model, './Model/model.pkl')
    joblib.dump(encoder, './Model/encoder.pkl')


