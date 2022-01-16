from setuptools import setup
from rule34Py.__vars__ import __version__, __author__, __email__

with open('README.md', 'r') as rmdf:
    long_description = rmdf.read()

setup(
    name='rule34Py',
    version=__version__,
    description='API wraper for rule34.xxx',
    url="https://github.com/b3yc0d3/rule34Py",
    author=__author__,
    author_email=__email__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['rule34Py'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires = [
        "beautifulsoup4 >= 4.9.3",
        "requests >= 2.25.1",
        "lxml >= 4.6.4"
    ],
    project_urls={
        "Issue tracker": "https://github.com/b3yc0d3/rule34Py/issues"
    }
)
