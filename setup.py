from setuptools import setup, find_packages

setup(
    name="depth1",
    version="v0.0.1",
    package=find_packages,
    install_requires=["git+https//github.com/dongchangYoo/depth2.git#egg=depth2"],
    dependency_links=[]
)
