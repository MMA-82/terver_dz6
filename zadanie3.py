import numpy as np
import scipy.stats as stats

d = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
m = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

delta = np.mean(d) - np.mean(m)

D = (np.var(d, ddof=1) + np.var(m, ddof=1))/ 2

S = np.sqrt(D/ len(d) + D/ len(m))

k = 2*(len(d) - 1)
t = stats.t.ppf(0.975, k)

print(f'Доверительный интервал для разности среднего роста родителей и детей: [{delta - t*S}; {delta + t*S}]')