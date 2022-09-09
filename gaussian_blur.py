#### Gaussion Blur
def calc2DNormalDistPDF(x, y, sigma):
	gb_pdf = (1.0 / (2.0 * math.pi * sigma * sigma)) * math.exp(-(x**2 + y**2)/(2.0 * sigma * sigma))
	return gb_pdf

## test for std 2d normal distribution pdf.
#coords = [(-1, 1), (0, 1), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
#for i in range(len(coords)):
#	print(calc2DNormalDistPDF(coords[i][0], coords[i][1], 1.5))

### gen nxn grid via radius
def genNxN_GridByRadius(center_x, center_y, radius):
	start_index = -radius
	end_index = radius
	cell_indices = []
	for x in range(start_index, end_index + 1):
		for y in range(start_index, end_index + 1):
			cell_indices.append((center_x + x, center_y + y))
	return cell_indices

#print(genNxN_GridByRadius(0, 0, 1))

def genNxN_GridCellWeight(center_x, center_y, radius, sigma):
	cell_indices = genNxN_GridByRadius(center_x, center_y, radius)
	cell_weights = []
#	print(center_x, center_y, cell_indices)
	for i in range(len(cell_indices)):
		x = cell_indices[i][0]
		y = cell_indices[i][1]
		pdf = calc2DNormalDistPDF(x, y, sigma)
		cell_weights.append({'x':x, 'y':y, 'weight':pdf})

	total_weight = 0.0
	for i in range(len(cell_weights)):
		total_weight += cell_weights[i]['weight']
	for i in range(len(cell_weights)):
		cell_weights[i]['weight'] /= total_weight

	return cell_weights

def doGaussionBlur(img_src, img_dest, width, height, radius, sigma):
	cell_weights = genNxN_GridCellWeight(0, 0, radius, sigma)

	for x in range(radius, width - radius):
		for y in range(radius, height - radius):
			sum_r = 0.0
			sum_g = 0.0
			sum_b = 0.0
		#	sum_a = 0
			for i in range(len(cell_weights)):
				pixel = img_src.getpixel((x + cell_weights[i]['x'], y + cell_weights[i]['y']))
				sum_r += pixel[0]/255.0 * cell_weights[i]['weight']
				sum_g += pixel[1]/255.0 * cell_weights[i]['weight']
				sum_b += pixel[2]/255.0 * cell_weights[i]['weight']
			#	sum_a += int(pixel[3] * cell_weights[i]['weight'])
			img_dest.putpixel((x - radius , y - radius), (int(sum_r*255.0), int(sum_g*255.0), int(sum_b*255.0)))

	img_dest.save('test_img_gaussion_blur.jpg')

doGaussionBlur(img, img2, width, height, 8, 80)
#img2.save('test_img_gaussion_blur.png')
