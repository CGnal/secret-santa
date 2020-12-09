from setuptools import setup, find_packages

version = '1.0.0dev'

with open("requirements.txt", 'r') as fid:
    reqs = [line.replace("\n", "") for line in fid.readlines()]


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='secret-santa',
    version=version,
    description='Secret Santa Game',
    long_description=readme(),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=reqs,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Topic :: Scientific/Engineering :: Game'
      ],
    url='https://github.com/CGnal/python-analytics-external-contrib/prophet',
    author='CGnal',
    author_email='datascience@cgnal.com',
    package_data={"tests": ['../resources/tests/data']},
    include_package_data=True,
)
