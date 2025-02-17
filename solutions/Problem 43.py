"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Lo que creo que será más fácil será primero hacerme una lista con todos los
pandigitales de 0 a 3 que son divisibles entre 17, 13, 11, 7, 5, 3 y 2.
Después, empezar con los de 17 y recorrerme la lista de los de 13, mirando que
se cumpla la propiedad, y así sucesivamente.
"""
global dict_3
global list_property
global primes


def pandigitals_l3(n):
    """
    Generates all pandigital numbers of length 3 that are divisible by n,
    including those starting with 0.
    """
    pd = []
    # Only numbers less than 4 digits, we start at n and the step`is also
    # n to consider all multiples of the prime`
    for i in range(n, 1000, n):
        str_i = str(i)
        if i < 10:
            # No numbers less than 10 are pandigital 0-9, the 0 repeats
            # (003 wouldn't be valid)
            pass
        elif i < 100:
            # If the number has 2 digits, first and second digit must be
            # different and second digit mustn't be 0
            # (020 and 022 aren't valid)
            if str_i[0] != str_i[1] and str_i[1] != "0":
                pd.append("0" + str_i)
        else:
            # If the number has 3 digits, all digits must be different
            if (
                str_i[0] != str_i[1] and str_i[0] != str_i[2]
                and str_i[1] != str_i[2]
            ):
                pd.append(str_i)
    return pd


def recurring_property(num, i):
    """Finds recursively the pandigital numbers that satisfy the property.
    primes = [2, 3, 5, 7, 11, 13]
    We start with a number that is divisible by 17, go through the pandigitals
    of three digits that are divisible by 13 checking if the property is
    satisfied. If it is, we do the same thing with 11, and so on. This is done
    recursively to simplify the code (the alternative was to make an if tower).
    """
    if i >= 0:
        # i is the index of the prime number we are checking,
        # so i = 5 => p = 13; i = 4 => p = 11, and so on.
        for triad in dict_3[primes[i]]:
            if num[:2] == triad[1:] and triad[0] not in num:
                recurring_property(triad[0] + num, i - 1)
    else:
        # The property has been satisfied! But there is a digit missing, we
        # have to add it and then append the number to the list.
        missing = set("0123456789") - set(num)
        list_property.append(int(missing.pop() + num))


if __name__ == "__main__":
    dict_3 = {i: pandigitals_l3(i) for i in [17, 13, 11, 7, 5, 3, 2]}
    primes = [2, 3, 5, 7, 11, 13]
    list_property = []
    for t17 in dict_3[17]:
        recurring_property(t17, 5)
    print(sum(list_property))  # 16695334890, 0.001s
