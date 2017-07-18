class Food(object):
	"""docstring for Food"""
	def __init__(self, n, v, w):
		super(Food, self).__init__()
		self.Name = n
		self.Value = v
		self.Calories = w

	def GetValue(self):
		return self.Value

	def GetName(self):
		return self.Name

	def GetCost(self):
		return self.Calories

	def Density(self):
		return self.GetValue() / self.GetCost()

	def __str__(self):
		return self.Name + ': <' + str(self.Value) + ', ' + str(self.Calories) + ' >'

def BiuldMenu(Names, Values, Calories):
	"""Names, Values, Calories List of same length
	Names a list strings
	Values, Calories list of numbers
	return list of Foods"""
	menu = []
	for i in xrange(len(Values)):
		menu.append(Food(Names[i], Values[i], Calories[i]))

	return menu

def Greendy(Items, MaxCost, KeyFunction):
	"""Assumes Items a list, MaxCost >= 0,
	KeyFunction maps elements of Items to numbers"""
	ItemsCopy = sorted(Items, key = KeyFunction, reverse = True)
	"""Arguments sorted Items a List need sorted, key = func compare, default reverse = false
	sorted Ascending reverse = True mean soterd Descending"""
	Result = []
	TotalValue, TotalCost = 0.0, 0.0
	for i in xrange(len(ItemsCopy)):
		if (TotalCost + ItemsCopy[i].GetCost()) <= MaxCost:
			Result.append(ItemsCopy[i])
			TotalCost += ItemsCopy[i].GetCost()
			TotalValue += ItemsCopy[i].GetValue()

	return (Result, TotalValue)

def TestGreendy(Items, Constraint, KeyFunction):
	Taken, val = Greendy(Items, Constraint, KeyFunction)
	print "Total Value of items taken =",val
	for Item in Taken:
		print '    ',Item

def TestGreendys(foods, MaxUnits):
	print "Use greendy by value to allocate ", MaxUnits, 'Calories'
	TestGreendy(foods, MaxUnits, lambda	x: x.GetValue())

	print "\nUse greendy by value to allocate ", MaxUnits, 'Calories'
	TestGreendy(foods, MaxUnits, lambda x: 1/x.GetCost())

	print "\nUse greendy by value to allocate ", MaxUnits, 'Calories'
	TestGreendy(foods, MaxUnits, lambda	x: x.Density())

Names = ['wine', 'beer', 'pizza', 'bugger', 'fries', 'cola', 'apple', 'donut', 'cake']
Values = [89, 90, 95, 100, 90, 79, 50, 10]
Calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = BiuldMenu(Names, Values, Calories)

TestGreendys(foods,750)
print '*' * 30
print '\n'
TestGreendys(foods,800)
print '*' * 30
print '\n'
TestGreendys(foods,1000)