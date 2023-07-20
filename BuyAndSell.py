def BuyAndSell(price):
     minPrice=float('inf')
     maxProfit=0

     for i in price:
         minPrice= min(minPrice,i)
         currentProfit= i - minPrice
         maxProfit = max(currentProfit,maxProfit)
     return maxProfit

price=list(map(int,input().split()))
print(BuyAndSell(price))