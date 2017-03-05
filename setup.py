import os

from setuptools import (
    find_packages,
    setup,
)


def read(path):
    with open(path, 'r') as fd:
        return fd.read()


HERE = os.path.abspath(os.path.dirname(__file__))
README = read(os.path.join(HERE, 'README.rst'))
CHANGES = read(os.path.join(HERE, 'CHANGES.rst'))
ENTRY_POINTS = read(os.path.join(HERE, 'entry_points.cfg'))

requirements = [
]

testing_requirements = [
    'mypy',
    'flake8',
]

develop_requirements = [
    'coverage',
    'isort',
    'watchdog',
]

setup(
    name='chordchart_notation',
    version='0.1.0',
    description='Chordchart Notation',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Antoine Cezar',
    author_email='antoine@cezar.fr',
    url='https://github.com/AntoineCezar/chordchart-notation',
    keywords='music chord chordchart',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': testing_requirements,
        'develop': develop_requirements,
    },
    install_requires=requirements,
    entry_points=ENTRY_POINTS,
)
