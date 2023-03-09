import math
from pathlib import Path
import random
import string

import cutils
import fast_distance
import jellyfish
import matplotlib.pyplot as plt

BENCHMARK_PATH = Path(__file__).resolve().parents[0]

def build_string(min: int=1, max: int=1_000):
    k = random.randint(min, max)

    return "".join(random.choices(string.printable, k=k))

def my_hamming(lst1: list[str], lst2: list[str]):
    for s1, s2 in zip(lst1, lst2):
        fast_distance.hamming_distance(s1, s2)

def jelly_hamming(lst1: list[str], lst2: list[str]):
    for s1, s2 in zip(lst1, lst2):
        jellyfish.hamming_distance(s1, s2)

def my_damerau(lst1: list[str], lst2: list[str]):
    for s1, s2 in zip(lst1, lst2):
        fast_distance.damerau_levenshtein_distance(s1, s2)

def jelly_damerau(lst1: list[str], lst2: list[str]):
    for s1, s2 in zip(lst1, lst2):
        jellyfish.damerau_levenshtein_distance(s1, s2)

def build_string_list(min_str_len: int=1, max_str_len: int=100, list_len: int=10_000):
    return [build_string(min_str_len, max_str_len) for _ in range(list_len)]

def plot_time(funclist: list[callable], plotname: Path | str, **kwargs):
    res = {func.__name__: [] for func in funclist}
    x_axis = []
    for list_len in range(7):
        lst1 = build_string_list(1, 100, 10 ** list_len)
        lst2 = build_string_list(1, 100, 10 ** list_len)

        for func in funclist:
            times = cutils.time_func(
                lambda: func(lst1, lst2), 
                warmups=kwargs["warmups"], 
                iterations=kwargs["iterations"],
                quiet=True
            )
            res[func.__name__].append(math.log(times.min + 1))
        
        x_axis.append(list_len)

    plt.close()
    for k, v in res.items():
        plt.plot(x_axis, v, label=k)
        plt.xticks(x_axis, [f"10^{i}" for i in range(7)])

    num_iters = kwargs["iterations"]
    plt.ylabel("Log min time")
    plt.xlabel("List length")
    plt.legend(loc="upper left")
    plt.savefig(plotname)
    plt.close()

def main():
    funclist = [my_hamming, jelly_hamming]
    plot_time(funclist, plotname=BENCHMARK_PATH / "hamming.png", warmups=3, iterations=10)

    funclist = [my_damerau, jelly_damerau]
    plot_time(funclist, plotname=BENCHMARK_PATH / "damerau_levenshtein.png", warmups=3, iterations=10)

if __name__ == "__main__":
    main()
