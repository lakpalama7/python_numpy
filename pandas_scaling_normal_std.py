import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, RobustScaler

df = pd.read_csv("housingprice.csv")
df = df.select_dtypes(include=np.number)
df.drop(columns='HouseID', inplace=True)
print(df.columns)

# apply absolute maximum scaling
# divide each value by max value : scale between -1 and 1
max_abs = np.max(np.abs(df), axis=0)
print(max_abs)
scaled_df = df / max_abs
print("Original dataset")
print(df.head())
print("Max absolute scaling dataset")
print(scaled_df.head())


# MinMax Scaling
# (value - min) / (max - min)
# scale value between 0 to 1

scaler = MinMaxScaler()
df_scaler = scaler.fit_transform(df)

data_scaler = pd.DataFrame(df_scaler, columns=df.columns)
print(data_scaler.head())

#Normalization (vector Normalization)
# normalize each row so its vector length becomes 1.
scaler = Normalizer()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df.head())

# Standardization
# (value - mean) / std
# transform data has mean=0 and std=1

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df.head())

# Robust Scaling: use median and iqr
# (value - median) / iqr
scaler = RobustScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df.head())