import numpy as np

memo = {}

def Bagofdevouring(weight, value):
	global memo
	
	if len(value) == 0: #base case
		return 0
	else:
		k = list(weight)
		k.extend(list(value))
		tupweight = tuple(k)
		total = []
	if tupweight in memo:
		return memo[tupweight]
	else:
		for a in range(len(value)):
		
                       	wsum = sum(np.delete(weight,a))
                        pB =  np.array([(weight[i]/float(wsum+100)) for i in range(a) + range(a + 1,len(value))])
		        pnB =  (1 - sum(pB))
			bagDel = np.array([Bagofdevouring(np.delete(weight, [i,a]), np.delete(value, [i,a])) for i in range(a) + range(a + 1,len(value))])
			bagnDel = Bagofdevouring(np.delete(weight, a),np.delete(value, a))
			total.append(value[a] + sum(pB * bagDel) + pnB * bagnDel)
		r = max(total)
		memo[tupweight] = r
		return r


#each case remove one weight, value, multiply by the chance of that item breaking. one more case exists, where nothing breaks. This chance is 1 - sum(P(i breaks) for i in weight)

if __name__ == "__main__":
	a = [100, 200, 300]
	b = a
	print Bagofdevouring(a,b)
	memo = {}

	a = [100,200,300]
	b = [300,200,100]
	print Bagofdevouring(a,b)
	memo = {}

	a = [100,100]
	b = a
	print Bagofdevouring(a,b)
	

