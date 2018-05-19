#initialize 0 as the number of ways to make change

#go throught the coins,
#the value of the coin is the smallest amount you can make change with for that coin
#for all values tmp_value that coin could be used to make change,
#we add the number of ways to make tmp_value - coin change to the current value.

#for example, if when we look to the C coin, we look at all the denominations d >= C
# and increase num_make_change[d] by num_make_change[d-C]
def count(coins,total):
    num_make_change = [0 for _ in range(total + 1)]
    num_make_change[0] = 1

    for coin in coins:
        for tmp_value in range(coin, total + 1):
            num_make_change[tmp_value] += num_make_change[tmp_value - coin]

    return num_make_change[total]


if __name__ == "__main__":
    total = int(input('total number of cents? '))
    num_of_coins = int(input('How many coins? '))
    coins = []
    for _ in range(num_of_coins):
        coins.append(int(input("next coin ")))
    print(count(coins, total))
