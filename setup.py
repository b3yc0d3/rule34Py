from setuptools import setup

setup(
    name='rule34Py',
    version='0.0.1',
    description='API wraper for rule34.xxx',
    py_modules=['rule34Py'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires = [
        "beautifulsoup4 ~= 4.9.3"
    ]
)
