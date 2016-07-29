import numpy as np

def Bagofdevouring(weight, value):
	
	if len(value) == 0: #base case
		return 0
	else:
		total = []
	
		for a in range(len(value)):
                        pB =  np.array(sum([(weight[i]/float(sum(weight) + 100)) for i in range(len(value))]))
		        pnB =  (1 - (sum(weight)/float(sum(weight) + 100)))
		        bagDel = np.array([Bagofdevouring(np.delete(weight, [i,a]), np.delete(value, [i,a])) for i in range(len(value))])
			bagnDel = Bagofdevouring(np.delete(weight, a),np.delete(value, a))	
			total.append(value[a] + sum(pB * bagDel) + pnB * bagnDel)
		print pB, bagDel
		return max(total)

#each case remove one weight, value, multiply by the chance of that item breaking. one more case exists, where nothing breaks. This chance is 1 - sum(P(i breaks) for i in weight)

if __name__ == "__main__":
	a = [100,200,300]
	b = a
	print Bagofdevouring(a,b)
