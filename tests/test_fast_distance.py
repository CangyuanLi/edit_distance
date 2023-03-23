import concurrent.futures
import random
import string

import jellyfish
import pytest

import fast_distance

def build_ascii_string(min: int=1, max: int=1_000):
    k = random.randint(min, max)

    return "".join(random.choices(string.printable, k=k))

@pytest.fixture
def lst1():
    return [build_ascii_string() for _ in range(100_000)]

@pytest.fixture
def lst2():
    return [build_ascii_string() for _ in range(100_000)]

def test_hamming(lst1, lst2):
    def compare(strs: tuple[str, str]):
        s1, s2 = strs
        res1 = fast_distance.hamming_distance(s1, s2)
        res2 = jellyfish.hamming_distance(s1, s2)

        assert res1 == res2

    with concurrent.futures.ProcessPoolExecutor() as pool:
        pool.map(compare, zip(*lst1, *lst2))

def test_damerau_levenshtein(lst1, lst2):
    def compare(strs: tuple[str, str]):
        s1, s2 = strs
        res1 = fast_distance.damerau_levenshtein_distance(s1, s2)
        res2 = jellyfish.damerau_levenshtein_distance(s1, s2)

        assert res1 == res2

    with concurrent.futures.ProcessPoolExecutor() as pool:
        pool.map(compare, zip(*lst1, *lst2))
