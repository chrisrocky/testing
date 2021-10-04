import numpy as np, pandas as pd
from openpyxl.reader.excel import load_workbook 
import matplotlib.pyplot as plt 
# import seaborn as sns 
#import statsmodels.api as sm
import math 
#from scipy import optimize
# model = sm.OLS(y,sm.add_constant(x)).fit(cov_type = "HC3")
# resid = y - model.predict()
# model2 = sm.OLS(model.predict(),sm.add_constant(resid)).fit(cov_type = "HC3")
# print(model2.summary())
# print(model.summary())
# b = 1250
# df = np.zeros(b)
# for i in range(0,b):
#     a = 50000
#     df[i] = 10 + 20**2 + np.sum(np.random.chisquare(100,a))/a
# sns.distplot(df,bins = 15)
# plt.show()
# Create list areas
p1 = np.random.randint(0,10)
p2 = np.random.randint(0,10)
if (p1 + p2 <= 5):
    p3 = np.random.randint(0,10)
else:
    p3 = 0
b1 = np.random.randint(0,10)
b2 = np.random.randint(0,10)
if (p1 + p2 == 8) or (p1 + p2 == 9):
    b3 = 0
elif (b1 + b2 == 8) or (b1 + b2 == 9):
    b3 = 0
elif (b1 + b2 == 3) and (p3 == 8):
    b3 = 0
elif (b1 + b2 == 4) and ((p3 == 0) or (p3 == 1) or (p3 == 8) or (p3 == 9)):
    b3 = 0 
elif (b1 + b2 == 5) and ((p3 == 0) or (p3 == 1) or (p3 == 2) or (p3 == 3) or(p3 == 8) or (p3 == 9)):
    b3 = 0 
elif (b1 + b2 == 6) and not ((p3 == 6) or (p3 == 7)):
    b3 = 0 
elif (b1 + b2 == 7):
    b3 = 0 
else:
    b3 = np.random.randint(0,10)
if p1 + p2 + p3 >= 10:
    p123 = p1 + p2 + p3 - 10
else:
    p123 = p1 + p2 + p3
if b1 + b2 + b3 >= 10:
    b123 = b1 + b2 + b3 -10
else:
    b123 = b1 + b2 + b3
if p123 > b123:
    print("Player wins",(p123),"vs",(b123))
elif p123 < b123:
    print("Banker wins", (p123),"vs",(b123))
else:
    print("tie")