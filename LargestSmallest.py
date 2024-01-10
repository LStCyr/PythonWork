#Finding the Largest or Smallest N Items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, nums)) #Prints the largest 3 values
print(heapq.nsmallest(3, nums)) #Prints the smallest 3 values

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 890, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.98},
    {'name': 'YHOO', 'shares': 45, 'prince': 16.35}]
cheap = heapq.nsmallest(1, portfolio, key=lambda s:['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: ['price'])

print(cheap, expensive)

