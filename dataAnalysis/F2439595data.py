import numpy as np
from scipy import stats

entry1 = {1: [5,5,5,5,5,5,5,5,5,4], 2: [5,5,5,5,5,5,5,4,4,3],3: [5,5,5,5,5,5,4,4,4,3],4: [5,4,4,4,4,4,4,3,3,3], 5:[5,4,4,4,4,4,4,3,3,3], 6:[5,5,5,4,4,3,3,2,2,1],7:[5,4,4,4,3,3,3,3,2,2]}
exit1 = {1:[5,5,5,5,5,4], 2: [5,5,5,5,5,4],3: [4,4,4,5,5,4],4: [5,4,5,4,4,3], 5:[5,4,5,5,4,4], 6:[5,4,5,4,5,4],7:[4,4,5,4,5,3]}
entry = {1:[5,5,5,5,4,4], 2: [5,5,5,4,4,3],3: [5,5,4,4,4,3],4: [4,4,4,3,3,3], 5:[4,4,4,3,3,3], 6:[5,4,4,2,2,1],7:[5,3,3,3,2,2]}
exit = {1: [5,5,5,5,5,4], 2: [5,5,5,5,5,4],3: [4,4,4,5,5,4],4: [5,4,5,4,4,3], 5:[5,4,5,5,4,4], 6:[5,4,5,4,5,4],7:[4,4,5,4,5,3]}
eme=[0,0,0,0,0,0]


for i in range(1,8):
   # print(entry[i])
    t_statistic, p_value = stats.ttest_ind(np.array(entry1[i]), np.array(exit1[i]),equal_var = False)
    print(f"Q{i} ind. stat: {t_statistic:,.3f}\t p={p_value:,.4f}")

    t_statistic, p_value = stats.ttest_rel(np.array(entry[i]), np.array(exit[i]))
    print(f"Q{i} paired. stat: {t_statistic:,.3f}\t p={p_value:,.4f}")
    
    eme=[0,0,0,0,0,0]
    for j in range(0,6):
        eme[j] = entry[i][j]-exit[i][j]

    t_statistic, p_value = stats.ttest_1samp(np.array(eme),popmean=np.average(entry[i]))
    print(f"Q{i} Enter-Exit. stat: {t_statistic:,.3f}\t p={p_value:,.4f}\n")