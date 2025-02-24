'''https://projecteuler.net/problem=38
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9
and (1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1, 2, ..., n) where n > 1?
'''
from resources.useful_functions import is_pandigital


def pandigital_multiples_2():
    '''Finds all 1 to 9 pandigital 9-digit number that can be formed as the
    concatenated products of an integer with n = 2.
    The bounds are explained in (1*).'''
    pandigital_multiples = {}
    # for x in range(6173, 9877):
    # We can even start with 9183, because any number smaller than that will
    # have a concatenated product less than 918273645
    for x in range(9183, 9877):
        concatenate = str(x) + str(2*x)
        if is_pandigital(concatenate):
            pandigital_multiples[x] = concatenate
    return pandigital_multiples


# No need to check for n = 3, with x = 329 the number is less than 918273645
'''def pandigital_multiples_3():
    """Finds all 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated products of an integer with n = 3.
    """
    pandigital_multiples = {}
    for x in range(123, 330):
        concatenate = str(x) + str(2*x) + str(3*x)
        if is_pandigital(concatenate):
            pandigital_multiples[x] = concatenate
    return pandigital_multiples'''


if __name__ == '__main__':
    # print(pandigital_multiples_2())
    # print(pandigital_multiples_3())
    # print(max(pandigital_multiples_3().values()))  # 327654981
    print(max(pandigital_multiples_2().values()))  # 932718654, 0.0007s


'''
#-------#
# Notes #
#-------#

(1*)
For n = 2, since we need to obtain 9 digits, the digits of x and 2x must sum to
9. Since x < 2x and we can only increase by one digit each time we multiply, we
have the following conditions:
            4 digits: x * 1 ∈ [1234, 9876]
            5 digits: x * 2 ∈ [12345, 98765] => x ∈ [6173, 49382]
            The intersection of the two intervals gives us x ∈ [6173, 9876]

For n = 3, we need:
            3 digits: x * 1 ∈ [123, 987]
            3 digits: x * 2 ∈ [123, 987] => x ∈ [62, 493]
            3 digits: x * 3 ∈ [123, 987] => x ∈ [41, 329]
            The intersection of the three intervals gives us x ∈ [123, 329]
            The concatenated product with 329 would be less than 918273645.

For n = 4, we need:
            2 digits: x * 1 ∈ [12, 98]
            2 digits: x * 2 ∈ [12, 98] => x ∈ [6, 49]
            2 digits: x * 3 ∈ [12, 98] => x ∈ [4, 32]
            3 digits: x * 4 ∈ [123, 987] => x ∈ [31, 246]
            The intersection of the four intervals gives us x ∈ [31, 32]
            31*1 = 31, 31*2 = 62, 31*3 = 93, not pandigital.
            32*1 = 32, 32*2 = 64, 32*3 = 96, not pandigital.

For n = 5, we need:
            1 digit: x * 1 ∈ [1, 9]
            2 digits: x * 2 ∈ [12, 98] => x ∈ [6, 49]
            2 digits: x * 3 ∈ [12, 98] => x ∈ [4, 32]
            2 digits: x * 4 ∈ [12, 98] => x ∈ [3, 24]
            2 digits: x * 5 ∈ [12, 98] => x ∈ [3, 19]
            The intersection of the five intervals gives us x ∈ [6, 9]
            6*1 = 6, 6*2 = 12, 6*3 = 18, not pandigital.
            7*1 = 7, 7*2 = 14, 7*3 = 21, not pandigital.
            8*1 = 8, 8*2 = 16, 8*3 = 24, 8*4 = 32, not pandigital.
            For 9, we already know it is pandigital.

For n > 5, it is impossible.

The algorithm will iterate over the case for n = 2 and return the largest
pandigital number found.
'''
