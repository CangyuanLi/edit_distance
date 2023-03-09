# fast_distance: fast C implementations of edit distance algorithms
![PyPI - Downloads](https://img.shields.io/pypi/dm/fast-distance)
![Tests](https://github.com/CangyuanLi/edit_distance/actions/workflows/tests.yml/badge.svg)

## What is it?

**fast_distance** is a collection of edit distance algorithms implemented as C extensions to Python.
Edit distance algorithms like Damerau-Levenshtein can be quite slow, especially for long strings (or
long lists of strings). Oftentimes, pure Python implementations are simply not viable for intensive
workloads. **fast_distance** intends to provide fast, optimized routines hidden behind a simple
Python API. All outputs are checked against [Jellyfish](https://github.com/jamesturk/jellyfish) to
verify correctness.

# Usage:

Warning- Currently only works on Mac and Linux due to C features not found in the Windows C
compiler

## Installing

The easiest way is to install **fast_distance** is from PyPI using pip:

```sh
pip install fast_distance
```

## Running

First, import the library.

```python
import fast_distance
```

Currently, fast_distance only implements Hamming and Damerau-Levenshtein.

```python
fast_distance.hamming_distance(s1, s2)
fast_distance.damerau_levenshtein_distance(s1, s2)
```

# TODO:

* Further performance improvements
* partial_ratio
* token_sort_ratio
* Fix compilation errors on Windows