import re

# Delete https and return domain
def delete_https(url):
    url = re.findall('^https://[^/]*', url)[0]
    return url.replace('https://', '')

# Delete https and return domain
def delete_http(url):
    url = re.findall('^http://[^/]*', url)[0]
    return url.replace('http://', '')

# Check url http
def isHttp(url):
    url = re.search('^http://', url)
    if url:
        return True
    else:
        return False

# Check url https
def isHttps(url):
    url = re.search('^https://', url)
    if url:
        return True
    else:
        return False
    

