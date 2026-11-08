def bank(x,y):
     for _ in range(y):
       x = x * 1.1
     return x 

profit = bank(100000,10)
print(round(profit,2))