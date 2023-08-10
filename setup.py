# -*- coding: utf-8 -*-
""" Setup for pytrafik """

from distutils.core import setup

setup(
    name='pytrafik',
    version='0.0.1',
    description='PyVasttrafik',
    long_description='Wrapper for Västtrafik public APIs.',
    url='https://github.com/janahlin/PyVasttrafik',
    download_url='https://github.com/janahlin/PyVasttrafiktarball/0.2',
    author='Jan Ahlin',
    author_email='jan.ahlin@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.11.4',
    ],
    keywords='vasttrafik västtrafik',
    install_requires=['requests>=2.28.2'],
    packages=['pyvasttrafik'],
    zip_safe=True)
