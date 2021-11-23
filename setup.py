from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    README = fh.read()

setup(
    name="fpylib",
    packages=find_packages(include=["fpylib", "fpylib.irange", "fpylib.functors"]),
    version="0.1.1",
    description="This is a library to do functional programming in Python.",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/FabianVegaA/fpy_lib",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    author="Fabián Vega",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
