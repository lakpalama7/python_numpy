import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# collecting data
titanic = sns.load_dataset('titanic')
print(titanic.head())

# cleaning data
print(titanic.info())
print(titanic.isna().sum())

titanic['age']=titanic['age'].fillna(titanic['age'].median(), inplace=True)
titanic['embarked']=titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)
titanic.drop(['deck','embark_town','alive','class','who','adult_male'], axis=1, inplace=True)

titanic['sex'] = titanic['sex'].map({'male':0, 'female':1})
titanic['embarked'] = titanic['embarked'].map({'C':0,'Q':1, 'S':2})
print(titanic.head())
print(titanic.isna().sum())

# Analyze the data
""" plt.figure(figsize=(8,6))
sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation matrix")
plt.show()

sns.barplot(x='pclass',y='survived', data=titanic)
plt.title("Survival rate by passenger class")
plt.show() """

# Visualize the Results

""" sns.countplot(x='survived', data=titanic)
plt.title("survival count")
plt.show()

sns.histplot(titanic['age'], kde=True)
plt.title("Age distribution")
plt.show()

sns.scatterplot(x='age',y='fare', hue='survived', data=titanic)
plt.title("Fare vs Age by survival")
plt.show() """

# Interpret and make decision
print(titanic.head())
X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print(f"Model Accuracy: {acc:.4f}")
