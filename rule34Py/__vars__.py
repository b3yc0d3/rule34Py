__version__tuple__ = ("1", "4", "3")
__author__ = ("b3yc0d3")
__email__ = ("mc25.studio@gmail.com")

__version__ = ".".join(__version__tuple__) # xx.xx.xx
__version_short__ = f"{__version__tuple__[0]}.{__version__tuple__[1]}" # xx.xx


# Variables
__base_url__ = "https://rule34.xxx/"
__useragent__ = f"Mozilla/5.0 (compatible; rule34Py/{__version__})"

__headers__ = {
    "User-Agent": __useragent__
}
