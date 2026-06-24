import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
import seaborn as sns
from scipy import stats


diabetes = load_diabetes()
col_name = diabetes.feature_names
df_diabetes = pd.DataFrame(diabetes.data, columns=col_name)
print(df_diabetes.head())

""" sns.boxenplot(x=df_diabetes['bmi'])
plt.title("Boxplot of BMI")
plt.show() """

# Remove outliser
# threshold = 0.12

# 1. Remove outlier using BOXPLOT
""" def remove_outliers(df, column, threshold):
    filter_df = df[df[column] <= threshold]
    sns.boxplot(filter_df[column])
    plt.title("Boxplot BMI after outlier removed")
    plt.show()
    return filter_df 


threshold_value = 0.12
no_outliers = remove_outliers(df_diabetes, 'bmi', threshold_value)

print("with outliers: ",df_diabetes.shape)
print("without outliers:", no_outliers.shape) """

# 2. Remove outlier using SCATTER PLOTS
""" sns.scatterplot(x=df_diabetes['bmi'], y=df_diabetes['bp'])
plt.title("Scatter plot of BMI VS BP")
plt.xlabel('BMI')
plt.ylabel("Blood Pressure")
plt.show() """

# removing outliers

""" outlier_indices = np.where((df_diabetes['bmi'] > 0.12) & (df_diabetes['bp']<0.8))

no_outliers = df_diabetes.drop(outlier_indices[0])
sns.scatterplot(x=no_outliers['bmi'], y=no_outliers['bp'])
plt.title("Scatter plot BMI vs BP after removing outliers")
plt.xlabel("BMI")
plt.ylabel("bp of people")
plt.show() """

# 3. Z-score method for outlier detection
z = np.abs(stats.zscore(df_diabetes['age']))
print(z)

# removing outliers : Trimming or capping
# Trimming: removes the rows that contains outliers
# capping: keeps the rows but replaces extreme values

# Tremming Outliers

threshold_z = 2
outlier_indices = np.where(z > threshold_z)[0]
no_outliers = df_diabetes.drop(outlier_indices)
print("Original dataframe shape:", df_diabetes.shape)
print("Dataframe shape after removing outliers: ", no_outliers.shape)

# Capping Outliers

threshold_z = 2
df_capped = df_diabetes.copy()
df_capped['age'] = np.where(z > threshold_z, df_capped['age'].mean() + threshold_z *
                            df_capped['age'].std(), df_capped['age'])
print("Original DataFrame shape: ", df_diabetes.shape)
print("DataFrame shape after capping outliers: ", df_capped.shape)


# 4. Interquartile range (IQR) method

q1, q3 = np.percentile(df_diabetes['bmi'], [25,75])
iqr = q3 - q1
print(iqr)

upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr

df_iqr = df_diabetes[(df_diabetes['bmi'] >= lower) & (df_diabetes['bmi'] <= upper)]
print("Original dataframe shape: ", df_diabetes.shape)
print("IQR method outlier removed: ", df_iqr.shape)

# Removing Outliers: Trimming and CApping

# 1. Trimming Outlier

diabetes = load_diabetes()
col_name = diabetes.feature_names
df_diabetes = pd.DataFrame(diabetes.data, columns=col_name)
print(df_diabetes.head())
print("Original dataframe shape: ", df_diabetes.shape)

# Remove outlier with IQR method
df_diabetes_trim = df_diabetes.copy()
q1 = df_diabetes_trim['bmi'].quantile(0.25)
q3 = df_diabetes_trim['bmi'].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

upper_array = np.where(df_diabetes_trim['bmi'] >= upper)[0]
lower_array = np.where(df_diabetes_trim['bmi'] <= lower)[0]

df_diabetes_trim.drop(index=upper_array, inplace=True)
df_diabetes_trim.drop(index=lower_array, inplace=True)

print("New shaper after using Trimming OUtlier: ", df_diabetes_trim.shape)


# Capping Outliers
df_capped = df_diabetes.copy()
df_capped['bmi'] = np.where(df_capped['bmi'] >= upper, upper, df_capped['bmi'])
df_capped['bmi'] = np.where(df_capped['bmi'] <= lower, lower, df_capped['bmi'])

print("Dataframe shape after using capping outliers", df_capped.shape)