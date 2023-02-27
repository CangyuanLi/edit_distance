import _damerau_levenshtein
import _hamming

def damerau_levenshtein_distance(s1: str, s2: str) -> int:
    return _damerau_levenshtein.distance(s1, s2)

def hamming_distance(s1: str, s2: str) -> int:
    return _hamming.distance(s1, s2)
