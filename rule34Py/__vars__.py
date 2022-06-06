__version__tuple__ = ("1", "4", "6")
__author__ = ("b3yc0d3")
__email__ = ("b3yc0d3@gmail.com")

__version__ = ".".join(__version__tuple__) # xx.xx.xx


# Variables
__base_url__ = "https://rule34.xxx/"
__api_url__ = "https://api.rule34.xxx/"
__useragent__ = f"Mozilla/5.0 (compatible; rule34Py/{__version__})"

__headers__ = {
    "User-Agent": __useragent__
}
