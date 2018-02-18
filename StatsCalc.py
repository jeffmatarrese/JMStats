# This file is a collection of functions to help solve elementary statistics problems.

def pointGivenConf(cLow, cHigh):
	errorMargin = (cHigh - cLow)/2
	pEstimate = cLow + errorMargin
	print("The Error Margin is " + str(errorMargin))
	print("The point estimate is " + str(pEstimate))