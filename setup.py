from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='backreading_bot',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements,
    author='Joe Spaniac',
    author_email='jspaniac@yahoo.com',
    description='This script library allows anyone to create a discord bot!',
    url='https://github.com/jspaniac/BlankDiscordBot',
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
