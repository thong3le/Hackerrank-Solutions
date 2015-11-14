# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    prices.sort()
    for i in range(len(prices)):
        rupees -= prices[i]
        if rupees < 0:
            return i
    return len(prices)

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)