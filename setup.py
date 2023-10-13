from setuptools import find_packages, setup

setup(
    name="skrimmage",
    packages=find_packages(exclude=["skrimmage_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-duckdb"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
