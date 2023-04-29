import numpy as np
import scipy.stats as stats
x = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
x_mean = np.mean(x)
print(f'Выборочная средняя результатов М =', x_mean)
s = np.sqrt(np.var(x, ddof=1))
print(f'Sigma =',s)
t = stats.t.ppf(0.975, 9)
print(f't наблюдаемое =', t)
print(f'Доверительный интервал:[{x_mean - t * s/np.sqrt(len(x))}; {x_mean + t * s/np.sqrt(len(x))}]')