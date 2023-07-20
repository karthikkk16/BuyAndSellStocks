def BuyAndSell(price):
    minPrice=float('inf')
    maxProfit=0

    for i in price:
        if i<minPrice:
            minPrice=i
    minPriceIndex= price.index(minPrice)

#traverse the array from the starting index(minPriceIndex)
    for i in range(minPriceIndex,len(price)-minPriceIndex):
        currentProfit= price[i] - minPrice
        maxProfit= max(currentProfit, maxProfit)
    return maxProfit

price=list(map(int,input().split()))
print(BuyAndSell(price))

'''
METHOD 2
     for i in price:
         minPrice= min(minPrice,i)
         currentProfit= i - minPrice
         maxProfit = max(currentProfit,maxProfit)
     return maxProfit
'''
