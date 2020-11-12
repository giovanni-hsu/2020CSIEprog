def Highest_Price(W,H,whlist,pricedic):
	if pricedic.get((W,H)) != None:
		return pricedic[(W,H)]
	cannotfit = 0
	for w,h in whlist:
		if (W,H) == (w,h):
			return W*H
		if W < w or H < h:
			cannotfit += 1
	if cannotfit == 3: return 0
	maxprice = 0
	for w in range(1,W//2+1):
		price1 = Highest_Price(w,H,whlist,pricedic)
		price2 = Highest_Price(W-w,H,whlist,pricedic)
		price = price1+price2
		maxprice = max(price,maxprice)
	for h in range(1,H//2+1):
		price1 = Highest_Price(W,h,whlist,pricedic)
		price2 = Highest_Price(W,H-h,whlist,pricedic)
		price = price1+price2
		maxprice = max(price,maxprice)
	pricedic.update({(W,H):maxprice})
	return maxprice

W,H = map(int,input().split(' '))

whlist = []
for i in range(3):
	Input = input().split(' ')
	whlist.append([eval(Input[0]),eval(Input[1])])

print(Highest_Price(W,H,whlist,{}))