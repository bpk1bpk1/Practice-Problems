N = 13
coins = [3,7,6,9]

coins_required = []
which_coins = []

for i in range(0,N+1):
    coins_required.append(100)
    which_coins.append(-1)

count = -1
coins_required[0] = 0 #basecase

for c in coins:
    count += 1
    for amount in range(0,N+1):
        if(amount >= c):
            cost_left = amount - c
            min_number = min(coins_required[amount], 1 + (coins_required[cost_left]))
            #print(amount,coins_required[amount], coins_required[cost_left])
            coins_required[amount] = min_number
            if(min_number < 100 and which_coins[amount] == -1):
                which_coins[amount] = count


print("The minimum coins required is", coins_required[N])
coins_used = []
value = which_coins[N]
print(value)
print(which_coins)
print("The coins used are:")
print(''.join(coins_used))



