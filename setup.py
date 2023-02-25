import setuptools

with open("fast_hamming/_version.py") as f:
    lines = f.readlines()
    version = lines[0].strip("\n").split()[-1].strip("\"'")

setuptools.setup(
    name="fast_hamming",
    version=version,
    ext_modules=[setuptools.Extension("_hamming", ["c_hamming/hamming.c"])],
    packages=["fast_hamming"]
)
