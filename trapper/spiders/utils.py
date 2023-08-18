
from datetime import datetime
from urllib.parse import urlparse
import re
from enum import Enum, auto

class NewSite(Enum):
    cnn = auto()
    reuters = auto()
    

def get_baeurl(url):
    """
    Given a URL, return the base URL.
    """
    return urlparse(url).scheme + "://" + urlparse(url).netloc

def get_category(url:str) -> str:
    '''
    function to get category of article from response

    '''
    base_url = get_baeurl(url)
    url1 = base_url.replace(".", "\.")
    reg = "([^/]+)"
    pattern = fr"{url1}/{reg}"

    match = re.search(pattern, url)
    if match:
        segment = match.group(1)
        return segment
    else:
        return "general"
    

# TODO: add a function to get date of the post from the url path    

def get_date_from_url(url:str, newsite:str) -> str:
    """
    function to get date of the post from the url path
    """
    pattern = ""
    date_format = ""
    website_name = "reuters"

    if website_name == "reuters":
        pattern = r"(\d{4}-\d{2}-\d{2})"
        date_format = "%Y-%m-%d"
    elif website_name == "cnn":
        pattern = r"/(\d{4}/\d{2}/\d{2})/"
        date_format = "%Y/%m/%d"


    match = re.search(pattern, url)
    if match:
        extracted_date = match.group(1)

        parsed_date = datetime.strptime(extracted_date, date_format)
    
        return parsed_date.strftime("%Y-%m-%d")
    else:
        return None
