#find the largest possible value stuff into a knapsack with a max capacity value

def Knapsack(maxweight, weight, value, n):
	"""
	the function which solves the knapsack
	"""
	if maxweight == 0 or n == 0: #to break recursion
		return 0
	if (weight[n - 1] > maxweight):
		Knapsack(maxweight, weight, value, n - 1) #remove objects heavier than max from the list
	else: #return the greater of the value of n - 1 + knapsack with weight maxweight - weight n - 1, or knapsack w/o n - 1, no need to remove from weight, value as the program wont touch those values beyond n - 1
		return max(value[n - 1] + Knapsack(maxweight - weight[n - 1], weight, value, n - 1), Knapsack(maxweight, weight, value, n - 1))


if __name__ == "__main__":
	
	#print Knapsack([100,200,300], [100,50,650], 3, 700)
	v = [201,300,200]
	w = [50,650,49]
	print Knapsack(700, w , v, len(v))

