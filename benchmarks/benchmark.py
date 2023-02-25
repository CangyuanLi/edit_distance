import _hamming
import jellyfish
import cutils
import random
import string

def build_string(min: int=1, max: int=1_000):
    k = random.randint(min, max)

    return "".join(random.choices(string.printable, k=k))

def my_hamming(lst1, lst2):
    for s1, s2 in zip(lst1, lst2):
        _hamming.distance(s1, s2)

def jelly_hamming(lst1, lst2):
    for s1, s2 in zip(lst1, lst2):
        jellyfish.hamming_distance(s1, s2)

def main():
    lst1 = [build_string() for _ in range(300_000)]
    lst2 = [build_string() for _ in range(300_000)]

    cutils.time_func(lambda: my_hamming(lst1, lst2), warmups=3, iterations=10)
    cutils.time_func(lambda: jelly_hamming(lst1, lst2), warmups=3, iterations=10)

if __name__ == "__main__":
    main()

