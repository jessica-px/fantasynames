import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fantasynames",
    version="0.0.1",
    author="Jessica Peck",
    author_email="jessypeck@gmail.com",
    description="A fantasy themed random name generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jessypeck/fantasynames",
    license="GPLv3+",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
