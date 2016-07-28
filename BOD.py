import numpy as np

def Bagofdevouring(weight, value):
	
	if len(value) == 0: #base case
		return 0
	else:
		total = []
		for a in range(len(value)):
			for i in range(a) + range(a + 1, len(value)):
				total.append(value[a] + (weight[i]/float((sum(weight) + 100))) * Bagofdevouring(np.delete(weight, i), np.delete(value,i)))

		return max(total)

		
#each case remove one weight, value, multiply by the chance of that item breaking. one more case exists, where nothing breaks. This chance is 1 - sum(P(i breaks) for i in weight)

if __name__ == "__main__":
	print Bagofdevouring([100,100],[100,100])

