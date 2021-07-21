from setuptools import setup

with open('README.md', 'r') as rmdf:
    long_description = rmdf.read()

setup(
    name='rule34Py',
    version='1.2.10',
    description='API wraper for rule34.xxx',
    url="https://github.com/b3yc0d3/rule34Py",
    author="b3yc0d3",
    author_email="mc25.studio@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['rule34Py'],
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires = [
        "beautifulsoup4 ~= 4.9.3",
        "requests ~= 2.25.1"
    ]
)
