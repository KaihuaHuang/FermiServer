from Homework import Homework

if __name__ =='__main__':
	tickerList = ['AMZN', 'MSFT', 'GOOG']
	weight = [0.5, 0.3, 0.2]
	startDate = '2017-8-10'
	endDate = '2018-9-11'
	notional = 100000
	# Look back window for historical VaR
	historicalWindow = 100

	demo = Homework()
	result = demo.Homework1(tickerList, weight, notional, historicalWindow=historicalWindow)
	print('Parametric', result['Parametric'])
	print('\nHistorical', result['Historical'])
	print('\nCov-Var Matrix')
	print(result['Cov-Var Matrix'])