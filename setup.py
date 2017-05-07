import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='devup',
    version='0.0.1',
    author='Pior Bastida',
    author_email='pior@pbastida.net',
    description='Command to manage your projects',
    license='BSD',
    keywords='development github',
    url='https://github.com/pior/devup',
    packages=['devup'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'console_scripts': [
            'de = devup.main:cli',
        ],
    },
)
