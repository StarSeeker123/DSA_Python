# Array of elements i

# Iterate through the array
# Pointer i for the price of current day
# Iterate the remaining array from i+1  to the end and select the largest element from the array
# Take the difference and print the array

def StockPricePrediction(arr):
    max_difference = 0
    for i in range(0, len(arr)-1):
        buy_price = arr[i]
        max_selling_price = 0
        selling_price_index = i+1
        while(selling_price_index < len(arr)):
            selling_price = arr[selling_price_index]
            if (selling_price >= max_selling_price):
                max_selling_price = selling_price
            selling_price_index += 1

        if (max_selling_price-buy_price) >= max_difference:
            max_difference = max_selling_price - buy_price

    return max_difference


# Driver code
stockArray = list(map(int, input().strip().split()))

print(StockPricePrediction(stockArray))
