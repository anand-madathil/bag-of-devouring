import numpy as np

#methods required:
#pull out of bag
#destroy items
#expected yield
choice = np.array(["yes", "no"])

class bagofdevouring(object):

	def __init__(self, values, weight):
		self.values = values
		self.weight = weight
		self.valuepulled = int(0)

	def pullout(self, slotno):
		self.valuepulled = self.valuepulled + self.values[slotno]
		self.values = np.delete(self.values, slotno)
		for i in range(0,len(self.values - 1)):
			self.destroy(i)

	def destroy(self, slotno):
		#destroy chance = weight of object / weight of bag + 100
		if np.random.choice(choice, p = [float(self.weight[slotno]) / (np.sum(self.weight) + 100), 1 - float(self.weight[slotno]) / (np.sum(self.weight) + 100)]) == "yes":
			self.values[slotno] = 0
			self.weight[slotno] = 0

	def bagstatus(self):
		location = str()
		newbag = []
		for i in range (0, len(self.values - 1)):
			if self.values[i] != 0:
				location += str(i)
			newbag = [self.values[int(i)] for i in location]
		self.values = newbag
		print self.values

	def smartpull(self):
		while len(self.values) > 0:
			self.pullout(np.argmax(self.values))
		return self.valuepulled

	def findExpectation(self, iterations):
		weightpull = int(0)
		for i in range (0, iterations):
			weightpull = weightpull + self.smartpull()
		print "expectation obtained is:", (float(weightpull) / iterations), "with", iterations, "tries"
			
if __name__ == "__main__":
	bag = bagofdevouring(np.array([100,200,300,400,500,600,700,800,900,1000]), np.array([100,200,300,400,500,600,700,800,900,1000]))
	bag.findExpectation(input("input how many iterations you want: "))

