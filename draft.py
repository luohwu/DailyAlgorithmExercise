import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
# figure(figsize=(8, 6), dpi=180)
plt.rcParams["figure.figsize"] = (14,6)
# plt.scatter(x=range(1,11),y=[0.02,0.018,0.016,0.021,0.02,0.021,0.075,0.314,0.146,0.077])
# plt.scatter(x=range(1,11),y=[0.036,0.034,0.058,0.712,0.04,0.034,0.042,0.038,0.031,0.044])
plt.scatter(x=range(1,11),y=[0.096,0.096,0.095,0.092,0.09,0.089,0.089,0.09,0.091,0.081])
plt.xlabel('frame index',fontsize=16)
plt.ylabel('frame contribution',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()