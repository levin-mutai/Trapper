from datetime import datetime
from urllib.parse import urlparse
import re
from enum import Enum, auto


class NewSite(Enum):
    cnn = auto()
    reuters = auto()


def get_baeurl(url) -> str:
    """
    Given a URL, return the base URL.

    @param url: The URL to parse.
    @return: The base URL.
    @rtype: str

    For example, given "http://www.cnn.com/some/path/here",
    return "http://www.cnn.com"

    """
    return urlparse(url).scheme + "://" + urlparse(url).netloc


def get_category(url: str) -> str:
    """
    function to get category of article from response

    @param url: url of the article
    @return: category of the article

    For example, given "http://www.cnn.com/category/path/here",
    return "category"

    """
    base_url = get_baeurl(url)
    url1 = base_url.replace(".", "\.")
    reg = "([^/]+)"
    pattern = rf"{url1}/{reg}"

    match = re.search(pattern, url)
    if match:
        segment = match.group(1)
        return segment
    else:
        return "general"


def get_date_from_url(url: str, newsite: str) -> str:
    """
    function to get date of the post from the url path

    @param url: url of the article
    @return: date of the article

    For example, given "http://www.cnn.com/category/path/here/2020/01/01",
    return "2020-01-01"

    """
    pattern = ""
    date_format = ""

    if newsite == "reuters":
        pattern = r"(\d{4}-\d{2}-\d{2})"
        date_format = "%Y-%m-%d"
    elif newsite == "cnn" or newsite == "aljazeera":
        pattern = r"\d{4}/\d{1,2}/\d{1,2}"
        date_format = "%Y/%m/%d"

    match = re.search(pattern, url)
    if match:
        extracted_date = match.group(0)

        parsed_date = datetime.strptime(extracted_date, date_format)

        return parsed_date.strftime("%Y-%m-%d")
    else:
        return None  # type: ignore
