from setuptools import find_packages, setup

setup(
    name="fpylib",
    packages=find_packages(include=["fpylib", "fpylib.irange", "fpylib.functors"]),
    version="0.1.0",
    description="This is a library to do functional programming in Python.",
    author="Fabián Vega",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
