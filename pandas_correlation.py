import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Math': [78, 85, 96, 80, 86],
    'Science': [88, 90, 94, 82, 89],
    'English': [72, 75, 78, 70, 74]
}
df =  pd.DataFrame(data)
print(df)

# Pearson correlation
# higher values indicate stronger correlation

""" pearson_corr = df.corr(method='pearson')
print(pearson_corr)

sns.heatmap(pearson_corr, annot=True, cmap='coolwarm')
plt.title("Pearson correlation Heatmap")
plt.show() """

# Spearman Correlation
# convert values to ranks before correlation
""" spearman_corr = df.corr(method='spearman')
print(spearman_corr)

sns.heatmap(spearman_corr, annot=True, cmap='viridis')
plt.title("Spearman correlation Heatmap")
plt.show() """

# Kendall Correlation
# measures agreement between ranking
""" kendall_corr = df.corr(method='kendall')
print(kendall_corr)

sns.heatmap(kendall_corr, annot=True, cmap='plasma')
plt.title("Kendall correlation Heatmap")
plt.show() """

# Correlation between two columns
""" corr_value = df['Math'].corr(df['Science'])
print("Correlation between math and science: ", corr_value)

two_col_df = df[['Math','Science']].corr()
sns.heatmap(two_col_df, annot=True, cmap='coolwarm')
plt.title("Correlation between Math  and science")
plt.show() """

# Correlation between Science and English
corr_value = df['Science'].corr(df['English'])
print("Correlation between Science and English: ", corr_value)

two_col_df = df[['Science','English']].corr()
sns.heatmap(two_col_df, annot=True, cmap='coolwarm')
plt.title("Correlation between Science and English")
plt.show()