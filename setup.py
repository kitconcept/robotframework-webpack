from setuptools import setup, find_packages

version = '1.0a2'

long_description = (
    open('README.rst').read() +
    '\n' +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')

setup(
    name='robotframework-webpack',
    version=version,
    description="A robot framework library for Webpack.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Web Environment',
        'Framework :: Robot Framework',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='robotframework django test',
    author='Timo Stollenwerk',
    author_email='stollenwerk@kitconcept.com',
    url='https://kitconcept.com',
    license='Apache License 2.0',
    packages=find_packages(
        exclude=['ez_setup', 'examples', 'tests']
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'robotframework',
        'robotframework-selenium2library',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
