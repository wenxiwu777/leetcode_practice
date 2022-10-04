import csv
import math
import random
import sys
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# read all records from earthquake CSV file on https://www.usgs.gov/
def readEarthquakeDataFile(filename):
	with open(filename) as data_file:
		data_samples = csv.reader(data_file)
		titles = next(data_samples)
		seq = 0
		data = {}

		for line in data_samples:
			lat = float(line[1])
			lon = float(line[2])
			mag = float(line[4])
			data[seq] = [lat, lon, mag]
			seq = seq + 1
	return data

# calculate Euclid distance
def calcEuclidDistance(xi, xj):
	d = len(xi)
	square_sum = 0.0
	for l in range(d):
		square_sum += (xj[l] - xi[l]) ** 2
	return math.sqrt(square_sum)

# calculate the average value from the samples within one cluster
def calcAverageDistance(clusterData):
	dist_x = 0.0
	dist_y = 0.0
	for i in range(len(clusterData)):
		dist_x += clusterData[i][0]
		dist_y += clusterData[i][1]
	return [dist_x/len(clusterData), dist_y/len(clusterData)]

# randomly generate k cluster centers from the samples
def createIntialClusterCenter(k, data):
	seqs = [x for x in data.keys()]
	initCenters = []
	for i in range(k):
		seq = random.choice(seqs)
		initCenters.append([data[seq][0], data[seq][1]])
	return initCenters

# Iterate and progressively form the k clusters
def performKMeansCluster(k, clusterCenters, data):
	eachClusterData = defaultdict(list)
	# add the current sample to target cluster
	for i in range(len(data)):
		min_dist = sys.maxsize
		min_k = 0
		for j in range(k):
			dist = calcEuclidDistance([data[i][0], data[i][1]], 
				[clusterCenters[j][0], clusterCenters[j][1]])
			if dist <= min_dist:
				min_dist = dist
				min_k = j
		eachClusterData[min_k].append(data[i])
	# update the cluster center with the average value in one cluster.
	clusterCenters.clear()
	for k in eachClusterData.keys():
		dist_center = calcAverageDistance(eachClusterData[k])
		clusterCenters.append(dist_center)
	return eachClusterData

# visualize the cluster via matplotlib's scatter graph
def visualizeEarthquakeClusters(eachClusterData):
	# draw the global map as the background
	img = mpimg.imread('./worldmap.jpeg')
	plt.imshow(img)
	# draw the bubble scatter graph
	wfac = 780.0 / 2.0 / 180.0
	hfac = 388.0 / 2.0 / 90.0
	xx = []
	yy = []
	sz = []
	col = []
	col_map = ['red', 'blue', 'green', 'yellow', 'cyan', 'black']
	for key in eachClusterData.keys():
		clusterData = eachClusterData[key]
		for i in range(len(clusterData)):
			xx.append(clusterData[i][1] * wfac + 780.0/2)
			yy.append(clusterData[i][0] * hfac + 388.0/2)
			sz.append(clusterData[i][2] * 3.0)
			col.append(col_map[key])
	plt.scatter(x=xx, y=yy, s=sz, c=col)
	plt.show()

# test entry
if __name__ == "__main__":
	data = readEarthquakeDataFile('./dataset/earthquakes_past_day.csv')
	# generate 6 cluster centers at the beginning
	clusterCenters = createIntialClusterCenter(6, data)
	for i in range(7): # perform 7 iterations to form the final clusters
		eachClusterData = performKMeansCluster(6, clusterCenters, data)
	visualizeEarthquakeClusters(eachClusterData)
