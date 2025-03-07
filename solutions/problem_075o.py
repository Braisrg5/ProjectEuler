'''https://projecteuler.net/problem=75'''
# It turns out that 12 cn is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there are
# many more examples
#             12cm: (3, 4, 5)
#             24cm: (6, 8, 10)
#             30cm: (5, 12, 13)
#             36cm: (9, 12, 15)
#             40cm: (8, 15, 17)
#             48cm: (12, 16, 20)

# In contrast, some lengths of wire, like 20cm, cannot be bent to form an
# integer sided right triangle, and other lengths allow more than one solution
# to be found; for example, using 120cm it is possible to form exactly three
# different integer sided right angle triangles.
#             120cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)

# Given that L is the length of the wire, for how many values of L <= 1500000
# can exactly one integer sided right angle triangle be formed?
from time import perf_counter
from resources.useful_functions import count_pyth_triples


if __name__ == '__main__':
    start = perf_counter()
    ways = count_pyth_triples(1500000)
    print(sum(1 for way in ways.values() if way == 1))  # 161667, 2.5s
    print(perf_counter() - start)
