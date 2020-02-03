"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dash-coronavirus',
    version='0.0.1',
    description='Dashboard for Coronavirus.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chunyeow/dash-coronavirus',
    author='Chun-Yeow Yeoh',
    author_email='yeohchunyeow@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Plotly Dash Flask',
    packages=find_packages(),
    install_requires=['flask',
                      'flask_assets',
                      'flask_apscheduler',
                      'requests',
                      'pandas',
                      'dash',
                      'dash_core_components',
                      'dash_html_components',
                      'dash_table',
                      'dash_renderer',
                      'pathlib'],
    entry_points={
        'console_scripts': [
            'run = wsgi:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/chunyeow/dash-coronavirus/issues',
        'Source': 'https://github.com/chunyeow/dash-coronavirus/',
    },
)
