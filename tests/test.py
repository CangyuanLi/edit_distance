import fast_distance
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

def test_hamming(lst1: list[str], lst2: list[str]):
    for s1, s2 in zip(lst1, lst2):
        res1 = fast_distance.hamming_distance(s1, s2)
        res2 = jellyfish.hamming_distance(s1, s2)

        assert res1 == res2

def test_damerau_levenshtein(lst1: list[str], lst2: list[str]):
    for s1, s2 in zip(lst1, lst2):
        res1 = fast_distance.damerau_levenshtein_distance(s1, s2)
        res2 = jellyfish.damerau_levenshtein_distance(s1, s2)

        assert res1 == res2

def main():
    lst1 = [build_string() for _ in range(1000)]
    lst2 = [build_string() for _ in range(1000)]

    test_hamming(lst1, lst2)
    test_damerau_levenshtein(lst1, lst2)


if __name__ == "__main__":
    main()
