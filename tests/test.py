import fast_hamming
import jellyfish
import cutils
import random
import string

def build_string(min: int=1, max: int=1_000):
    k = random.randint(min, max)

    return "".join(random.choices(string.printable, k=k))

def build_ascii_string(min: int=1, max: int=1_000):
    k = random.randint(min, max)

    return "".join(random.choices(string.ascii_letters, k=k))

def main():
    lst1 = [build_string() for _ in range(500_000)]
    lst2 = [build_string() for _ in range(500_000)]

    for s1, s2 in zip(lst1, lst2):
        res1 = fast_hamming.distance(s1, s2)
        res2 = jellyfish.hamming_distance(s1, s2)

        assert res1 == res2

if __name__ == "__main__":
    main()
