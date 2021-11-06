__version__tuple__ = ("1", "4", "0")
__authors__tuple__ = ("b3yc0d3")
__emails_tuples__ = ("<mc25.studio[at]gmail.com>")

__version__ = ".".join(__version__tuple__) # xx.xx.xx
__version_short__ = f"{__version__tuple__[0]}.{__version__tuple__[1]}" # xx.xx
__authors__ = ", ".join(__authors__tuple__)
__emails__ = ", ".join(__emails_tuples__)


# Variables
__base_url__ = "https://rule34.xxx/"
__useragent__ = f"Mozilla/5.0 (compatible; rule34Py/{__version__})"

__headers__ = {
    "User-Agent": __useragent__
}
