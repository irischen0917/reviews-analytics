#reviews
data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		print(len(data))
		
print(len(data))
print(data[0])

