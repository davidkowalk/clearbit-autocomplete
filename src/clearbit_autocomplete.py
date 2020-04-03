from json import loads as parse
from urllib.parse import quote_plus as url

def autocomplete(name: str):
    try:
        http_name = url(name)
        content = __load__(f"https://autocomplete.clearbit.com/v1/companies/suggest?query={http_name}")
        json = parse(content)
        return json
    except:
        print("Error")
        return None

# Http Request
from urllib.request import urlopen as ureq

def __load__(url):
    client = ureq(url)
    content = client.read()
    client.close()
    return content
