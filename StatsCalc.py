# This file is a collection of functions to help solve elementary statistics problems.

def pointGivenConf(cLow, cHigh): #Find point estimate when given confidence interval
	errorMargin = (cHigh - cLow)/2
	pEstimate = cLow + errorMargin
	print("The Error Margin is " + str(errorMargin)) #BUG: does not round, gives weird float
	print("The point estimate is " + str(pEstimate))

def zCrit(conf): #reminder to figure out scipy to use confidence intervals

def ciPopProp(x, n, z): #Find confidence interval for population proportion
	p = x/n
	q = 1-p
	errorMargin = z * ((p*q)/n)**(1/2)
	cLow = p - errorMargin
	cHigh = p + errorMargin
	print("p = " + str(p))
	print("q = " + str(q))
	print("The population proportion lies between " + str(cLow) + " and " + str(cHigh))
	print("The margin of error is " + str(errorMargin))

def ciPopPropP(p, n, z): #Find confidence interval for population proportion when given p
	q = 1-p
	errorMargin = z * ((p*q)/n)**(1/2)
	cLow = p - errorMargin
	cHigh = p + errorMargin
	print("The population proportion lies between " + str(cLow) + " and " + str(cHigh))
	print("The margin of error is " + str(errorMargin))

def ciSampleMean(xBar, n, stddev, z): #Find confidence interval for population mean
	errorMargin = z * (stddev/n**(1/2))
	cLow = xBar - errorMargin
	cHigh = xBar + errorMargin
	print("The sample mean lies between " + str(cLow) + " and " + str(cHigh))
	print("The margin of error is " + str(errorMargin))

def minSample(z, stddev, e): #Minimum sample size given sample mean
	n = ((z * stddev)/e)**2
	print("The minimum sample size is " + str(n))

def minSamplePop(p, z, e): #minimum sample size given population proportion
	n = p * (1-p) * (z/e)**2
	print("The minimum sample size is " + str(n))

#Testing Testing Testing Testing

def zTest(xBar, mean, stddev, n): #In Progress!
	z = (xBar - mean)/(stddev / n**(1/2))
	print("z = ")
	testType = input("Is this a left-tail (lt), right-tail (rt), or two-tailed (tt) test?")
	if test
