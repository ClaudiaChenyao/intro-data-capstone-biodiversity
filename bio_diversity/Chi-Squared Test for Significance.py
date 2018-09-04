import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

contingency = [[30, 146],[75, 413]]
chi2, pval, dof, expected = chi2_contingency(contingency)

print('p value is ')
print(pval)
#mammal and bird
#no significant difference


contingency2 = [[30, 146],[5, 73]]
chi22, pval2, dof2, expected2 = chi2_contingency(contingency2)
print('the p value is ')
print(pval2)
#reptile and mammal
#significant difference




