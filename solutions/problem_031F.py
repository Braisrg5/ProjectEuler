'''https://projecteuler.net/problem=31
In the United Kingdom the currency is made up of pound (£) and pence (p). There
are eight coins in general circulation:
                1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
                1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?
'''


def recursive_coin_count(pence, coins, ways=0):
    '''Calculates the number of different ways that pence can be made using the
    coins in the list (which must be in decreasing order).
    Does so recursively, eliminating a coin in each step and calculating the
    number of ways with the remaining coins.'''
    coins = [coin for coin in coins if coin <= pence]
    new_coins = coins.copy()
    for coin in coins:
        # We subtract the biggest coin from the total money we have
        rest_pence = pence - coin
        # Exact calculation, no more space to add other coins
        if rest_pence == 0:
            ways += 1
        # If only the coin of value 1 remains, there is just one way
        elif coin == 1:
            ways += 1
        # Otherwise, we try to find a solution with the remaining coins
        else:
            ways = recursive_coin_count(rest_pence, new_coins, ways)
        # We remove the coin we used from the list for the next iteration
        new_coins.remove(coin)
    return ways


if __name__ == '__main__':
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    print(recursive_coin_count(200, coins))  # 73683, 0.039s
