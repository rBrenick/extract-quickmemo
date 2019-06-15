import setuptools

setuptools.setup(
    name="extract-quickmemo",
    version="0.0.1",
    author="Richard Brenick",
    author_email="RichardBrenick@gmail.com",
    description="A small example package",
    url="https://github.com/rBrenick/extract-quickmemo",
    packages=setuptools.find_packages(),
    package_data={'': ['*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

