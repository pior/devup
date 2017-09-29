import os
from setuptools import setup, find_packages

install_requires = ['PyYAML']


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='devup',
    version='0.1.dev0',
    author='Pior Bastida',
    author_email='pior@pbastida.net',
    description='Command to manage your projects',
    license='BSD',
    keywords='project management github invoke makefile task',
    url='https://github.com/pior/devup',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
    packages=find_packages(),
    package_data={
        'devup': ['files/*'],
    },
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'de = devup.app:cli',
        ],
    },
)
