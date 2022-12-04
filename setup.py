from setuptools import setup, find_packages

setup(
    name="depth1",
    version="v0.0.1",
    package=find_packages,
    install_requires=[
        "depth2 @ git+https://github.com/dongchangYoo/depth2.git"
    ],
    dependency_links=[

    ]
)
