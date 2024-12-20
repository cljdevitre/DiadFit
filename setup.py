
#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'src', 'DiadFit', '_version.py'), encoding='utf-8') as f:
    exec(f.read())

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="DiadFit",
    version=__version__,
    author="Penny Wieser",
    author_email="penny.wieser@gmail.com",
    description="DiadFit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PennyWieser/DiadFit",
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required

    package_data={
        # Include all pickle files
        "": ["*.pkl", "*.csv"],
    },


    install_requires=[
            'pandas',
            'numpy<2',
            'matplotlib',
            'scikit-learn',
            'scipy>1.6',
            'lmfit>=1.1.0',
            'tqdm',
            'python-docx'

            ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
