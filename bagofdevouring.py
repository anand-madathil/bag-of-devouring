import numpy as np
import itertools

#methods required:
#pull out of bag
#destroy items
#expected yield
choice = np.array(["yes", "no"])

class bagofdevouring(object):

	def __init__(self, values, weight):
		self.storevalues = values
		self.values = values
		self.weight = weight
		self.valuepulled = int(0)
		self.atebefore = int(0)

	def pullout(self, slotno):
		self.valuepulled = self.valuepulled + self.values[slotno]
		self.values = np.delete(self.values, slotno)
		i = 0		
		while self.atebefore == 0 and i < len(self.values):
			self.destroy(i)
			i = i + 1
		self.atebefore = 0

	def destroy(self, slotno):
		#destroy chance = weight of object / weight of bag + 100
		if np.random.choice(choice, p = [float(self.weight[slotno]) / (np.sum(self.weight) + 100), 1 - float(self.weight[slotno]) / (np.sum(self.weight) + 100)]) == "yes":
			self.values = np.delete(self.values, slotno)
			self.weight = np.delete(self.weight, slotno)
			self.atebefore = 1

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
			print self.values
			self.values = self.storevalues
			print self.values
		print "expectation obtained is:", (float(weightpull) / iterations), "with", iterations, "tries", weightpull

	#EXPERIMENTAL
	#def expectedYield(self):
		#self.expectedYiel(len(self.values))
	#def expectedYieldd(self, length):
		#yieldExpect = np.argmax(self.values)
		#self.values = np.delete(self.values, np.argmax(self.values))
		#xlist = np.array([])
		#for x in range (1, length + 1):
			#for i in range (0, length - x):
				#xlist = np.append(xlist, 0)
			#xlist = np.append(xlist, 1)		
			#for i in range (0, length - (length - x + 1)):
				#xlist = np.append(xlist, 0)		
			#print xlist
			#if length > 0:
				#self.expectedYieldd(length - 1)
			#xlist = np.array([])
		#only one object can get eaten at a time
		#yield is 1st + P(2nd doesnt get eaten)*2nd*P(3rd doesnt get eaten)*3
		#this creates a binary count, which creates each outcome
if __name__ == "__main__":
	bag = bagofdevouring(np.array([100,200,300]), np.array([100,200,300]))
	bag.findExpectation(input("input how many iterations you want: "))
	#bag.expectedYield()

