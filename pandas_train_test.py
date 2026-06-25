import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    'Age': [22, 25, 47, 52, 46],
    'Salary': [25000, 32000, 48000, 52000, 50000],
    'Purchased': [0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

# Method 1: Splitting Dataset Using train_test_split()

X = df[['Age','Salary']]
y = df['Purchased']

X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)

print(X_train, '\n', X_test)
print("------------")
print(y_train,'\n', y_test)

# check model accuracy using logistic regression model

# creating and traiing the model
model = LogisticRegression()
model.fit(X_train,y_train)

# Making predictions on test data
y_pred = model.predict(X_test)

#Evaluating model performance
acc = accuracy_score(y_test, y_pred)
print("Accuracy: ", acc)
#We can see our model is performing well after train and test split.

# Method 2: manual splitting using indexing
# means: diving the dataset into traiing and test with out using ML functions

data = {
    'Age': [22, 25, 47, 52, 46],
    'Salary': [25000, 32000, 48000, 52000, 50000],
    'Purchased': [0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)
print(df)
split = int(0.8 * len(df))
train=df[: split]
test = df[split:]
print(train)
print(test)

# Method: 3 Splitting using NUmpy

arr = np.arange(20)
print("Original array:", arr)

train, test = np.split(arr,[16])
print("Train: ", train)
print("Test: ", test)