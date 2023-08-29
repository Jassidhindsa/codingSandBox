


def bestTimeToBuyAndSellStock(prices):
    maxProfit = 0
    lowest_price = prices[0]

    for price in prices:
        if price < lowest_price:
            lowest_price = price
        maxProfit = max(maxProfit, price - lowest_price)
    
    return maxProfit



if __name__ == "__main__":
    print(bestTimeToBuyAndSellStock([7,1,5,3,6,4]))