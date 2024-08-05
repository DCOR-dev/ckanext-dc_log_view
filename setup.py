from setuptools import setup

setup(
    # for compatibility with ckanext namespace
    packages=find_packages(),
    namespace_packages=['ckanext'],
)
