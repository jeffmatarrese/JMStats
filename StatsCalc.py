# This file is a collection of functions to help solve elementary statistics problems.

def pointGivenConf(cLow, cHigh): #Find point estimate when given confidence interval
	errorMargin = (cHigh - cLow)/2
	pEstimate = cLow + errorMargin
	print("The Error Margin is " + str(errorMargin))
	print("The point estimate is " + str(pEstimate))

def zCrit(conf): #reminder to figure out scipy to use confidence intervals

def confIntForPopProp(x, n, z): #figure out a more elegant way to just enter the confidence interval instead of z-crit!
	p = x/n
	q = 1-p
	errorMargin = z * ((p*q)/n)**(1/2)
	cLow = p - errorMargin
	cHigh = p + errorMargin
	print("p = " + str(p))
	print("q = " + str(q))
	print("The population proportion lies between " + str(cLow) + " and " + str(cHigh))
	print("The margin of error is " + str(errorMargin))