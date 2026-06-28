import numpy as np
import scipy.stats as stats

b = np.array([120, 122, 118, 130, 125, 128, 115, 121, 123, 119])
a = np.array([115, 120, 112, 128, 122, 125, 110, 117, 119, 114])

alpha = 0.05

t_stat, p_val = stats.ttest_rel(a,b)

m = np.mean(a -b)
s = np.std(a - b)
n = len(b)
t_manual = m / (s / np.sqrt(n))

decision = "Reject" if p_val <= alpha else "Fail to reject"
concl = "Significant difference" if decision =="Reject" else "NO significant difference"

print("T-test:", t_stat)
print("P-value:",p_val)
print("T test manual: ", t_manual)
print(f"Decision: , {decision} H0 at alphavalue = {alpha}")
print("Conclusion: ", concl)