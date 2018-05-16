from setuptools import setup

setup(
    name='travelblog',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
