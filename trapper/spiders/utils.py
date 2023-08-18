
from urllib.parse import urlparse
import re

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



