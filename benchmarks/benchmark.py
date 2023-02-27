import random
import string

import cutils
import fast_distance
import jellyfish

def build_string(min: int=1, max: int=1_000):
    k = random.randint(min, max)

    return "".join(random.choices(string.printable, k=k))

def my_hamming(lst1, lst2):
    for s1, s2 in zip(lst1, lst2):
        fast_distance.hamming_distance(s1, s2)

def jelly_hamming(lst1, lst2):
    for s1, s2 in zip(lst1, lst2):
        jellyfish.hamming_distance(s1, s2)

def my_damerau(lst1, lst2):
    for s1, s2 in zip(lst1, lst2):
        fast_distance.damerau_levenshtein_distance(s1, s2)

def jelly_damerau(lst1, lst2):
    for s1, s2 in zip(lst1, lst2):
        jellyfish.damerau_levenshtein_distance(s1, s2)

def main():
    lst1 = [build_string(1, 100) for _ in range(100_000)]
    lst2 = [build_string(1, 100) for _ in range(100_000)]

    cutils.time_func(lambda: my_hamming(lst1, lst2), func_name="fast_hamming", warmups=3, iterations=10)
    cutils.time_func(lambda: jelly_hamming(lst1, lst2), func_name="jellyfish.hamming_distance", warmups=3, iterations=10)
    cutils.time_func(lambda: my_damerau(lst1, lst2), func_name="fast_damerau", warmups=3, iterations=10)
    cutils.time_func(lambda: jelly_damerau(lst1, lst2), func_name="jellyfish.damerau", warmups=3, iterations=10)

if __name__ == "__main__":
    main()

