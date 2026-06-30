import pandas as pd
import numpy as np
import os

np.random.seed(42)

n_samples = 10000

data = {}

for i in range(1, 29):
    data[f'V{i}'] = np.random.normal(0, 1, n_samples)

data['Amount'] = np.random.uniform(1, 1000, n_samples)

fraud_ratio = 0.02
data['Class'] = np.random.choice([0, 1], size=n_samples, p=[0.98, 0.02])

df = pd.DataFrame(data)

fraud_indices = df[df['Class'] == 1].index
df.loc[fraud_indices, 'Amount'] *= 3
df.loc[fraud_indices, 'V1'] += 2
df.loc[fraud_indices, 'V2'] -= 2

# Ensure dataset folder exists
os.makedirs('dataset', exist_ok=True)

# Save file
file_path = os.path.join('dataset', 'creditcard.csv')
df.to_csv(file_path, index=False)

print(f"✅ Dataset saved at: {file_path}")