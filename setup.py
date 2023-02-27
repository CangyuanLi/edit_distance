import setuptools

with open("fast_distance/_version.py") as f:
    lines = f.readlines()
    version = lines[0].strip("\n").split()[-1].strip("\"'")

setuptools.setup(
    name="fast_distance",
    version=version,
    ext_modules=[
        setuptools.Extension("_hamming", ["c_distance/hamming.c"]),
        setuptools.Extension("_damerau_levenshtein", ["c_distance/damerau_levenshtein.c"])
    ],
    packages=["fast_distance"]
)
