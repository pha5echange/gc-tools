# ajw_plot_a05.py
# Version a03
# by jmg - jmg*AT*phasechange*DOT*co*DOT*uk
# Aug 13th 2015

# Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/

# Processes file 'data/..'
# Plots results and writes PNG to 'graphs/..'

# CHANGES IN THIS VERSION: 
# (1) Reads multiple 'batch' files, and labels graphs accordingly
# (2) Only has to deal with 1 flask per data file

# import packages
import os
import matplotlib
import matplotlib.pyplot as plt

versionNumber = ("a05")

fileNames = os.listdir("data")

# create 'graphs' subdirectory if necessary
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# ..and begin..
print ('\n' + 'AJW: Plotter-Thingy | ' + 'Version: ' + versionNumber + ' | Starting' + '\n' +'\n')

# open files for reading
for index in range(len(fileNames)):

	# look for file in 'data' subfolder
	pathname = os.path.join("data", fileNames[index])

	# define naming variables
	batchFile = str(fileNames[index])
	batchName, fileExtension = batchFile.split(".")

	# define lists to store the data
	xAxis = []
	yAxis = []

	# define path for graphs
	graphPath = os.path.join("graphs", batchName + "_ajw_plot.jpg")

	# read data
	dataInput = open(pathname, "r")

	# read lines from the file
	for line in dataInput:

		# split line and update lists
		hours, tube01 = line.split("^")
		xAxis.append (float(hours))
		yAxis.append(float(tube01))

	# close input file
	dataInput.close()

	# set axes values
	x_low = 0
	x_high = (max(xAxis) + 1)
	y_low = 0
	y_high = (max(yAxis) + 0.05)

	# plot graph
	width = 1 
	plt.plot(xAxis, yAxis, marker='o', linestyle='-', color='b', label=batchName)

	# label, plot and save image of graph
	plt.grid(zorder=0)
	plt.suptitle(batchName, fontsize=12)
	plt.xlabel('Hours', fontsize=12)
	plt.ylabel('Results', fontsize=12)
	plt.legend(loc='upper left')
	plt.xlim(x_low, x_high)
	plt.ylim(y_low, y_high)
	plt.savefig(graphPath, format = 'jpg')

	# display 'live' graph on screen
	plt.show()

	# clear plot
	plt.clf()

# write to screen
print ('\n' + 'Run Information' + '\n')
print ('AJW: Plotter-Thingy' + '\n')
print ('Version: ' + versionNumber + '\n')
print ('Graphs are saved to graphs/..' + '\n')
