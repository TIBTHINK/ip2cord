from setuptools import find_packages, setup
setup(
    name='ip2cord',
    packages=find_packages(include=['ip2cord']),
    version='0.1.0',
    description='A python3 libray for converting your internet ip address to coordinates',
    author='TIBTHINK',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)