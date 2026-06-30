import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
import pickle

# Load dataset
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, '..', 'dataset', 'creditcard.csv')

df = pd.read_csv(file_path)

X = df.drop('Class', axis=1)
y = df['Class']

# Scaling
scaler = StandardScaler()
X['Amount'] = scaler.fit_transform(X[['Amount']])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Handle imbalance
sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

# Model
model = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1)
model.fit(X_train_res, y_train_res)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
pickle.dump(model, open('fraud_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))