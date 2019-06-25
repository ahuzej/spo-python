import pandas as pd
import matplotlib.pyplot as plt

mainDataFrame = pd.read_csv('agaricus-lepiota.data', sep=',')

print("State before normalization: ")
dfshape = mainDataFrame.shape
print("Rows: " + str(dfshape[0]))
print("Columns: " + str(dfshape[1]))
print()

print(mainDataFrame.info())

print()
print("*********** STATISTICS: *************")
print()

for col in mainDataFrame:
    print(mainDataFrame[col].describe())
    print()
    
print("*********** PLOTTING **************")
print("*********** SCATTER PLOT: **************")

#print(mainDataFrame.type.count_values())

#data = {'type': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
#names = list(data.keys())
#values = list(data.values())
#
#fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
#axs[0].bar(names, values)
#axs[1].scatter(names, values)
#axs[2].plot(names, values)
#fig.suptitle('Categorical Plotting')