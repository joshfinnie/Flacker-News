import os
from setuptools import setup, find_packages

from news import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='flacker-news',
    version=".".join(map(str, VERSION)),
    description='Hacker News clone written in python.',
    long_description=readme,
    author='Josh Finnie',
    author_email='josh.finnie@gmail.com',
    url='https://github.com/joshfinnie/Flacker-News',
    packages=find_packages(),
    package_data = {
        'flaker-news': [
            'templates/*.html',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
    ],
)
