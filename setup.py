from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="parseltongue",
    version="0.3.0",
    description="List of dragonfly grammars to write programs in python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sauravmishra1017/Parseltongue",
    author="Saurav Mishra",
    author_email="sauravmishra1017@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
    ],
    packages=["parseltongue"],
    include_package_data=True,
    install_requires=["dragonfly2"],
)