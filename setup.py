from setuptools import setup

setup(
    packages=find_packages()
    # for compatibility with CKAN namespaces
    namespace_packages=['ckanext']
)
