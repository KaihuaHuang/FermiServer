from Homework import Homework

if __name__ =='__main__':
	k1 = 900
	t1 = 1
	k2 = 1100
	t2 = 2

	ticker = 'AMZN'
	rf = 0.0
	vol = 0.210609
	div = 0
	pcFlag = 1

	sharpRatio = 0.23
	demo = Homework()
	result = demo.Homework3(ticker, t1, t2, k1, k2, rf, div, sharpRatio, steps=200)

	print('\nLiquid Asset Value:',result['Liquid Asset'])
	print('Illiquid Asset Value:',result['Illiquid Asset'])
	print('Illiquid Equity Value:',result['Illiquid Equity'])
	print('Market Cap:', result['Market Cap'])
