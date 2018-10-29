from Homework import Homework

if __name__ =='__main__':
	ticker = 'AMZN'
	rf = 0.05
	ttm = [1, 2]
	Debt = [6000, 20]
	demo = Homework()

	result = demo.Homework2(ticker, ttm, Debt)
	print('\nAsset Value:', result['Asset Price'])
	print('Default Prob:', result['Default Prob'])