import bod2

if __name__ == "__main__":
	a = [100, 200, 300]
	b = a
	assert bod2.Bagofdevouring(a,b) == 462.5
	memo = {}

	a = [300,200,100]
	assert bod2.Bagofdevouring(a,b) == 470.8333333333333
	memo = {}

	a = [100,100]
	b = a
	assert bod2.Bagofdevouring(a,b) == 150
	memo = {}

	a = [10,100,150,250,500,750,1000,2500,5000,7500,10000]
	b = [100,200,300,400,500,1000,2000,1500,3000,6000,4000]
	print bod2.Bagofdevouring(a,b)

	
	
