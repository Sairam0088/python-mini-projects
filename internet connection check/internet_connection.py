#internet connection checker

import requests
from requests.exceptions import ConnectionError

def internet_connection_test():
    url = "htps://www.google.com/"
    print(f"Attempting to connect to {url} to check connection.")
    try:
        resp = requests.get(url, timeout=10)
        resp.text
        resp.status_code
        print("Connection is good")
        return True
    except ConnectionError as e:
        requests.ConnectionError
        print(f"Failed to connect to {url}")
        return False
    except:
        print("Failed with unparsed reason.")
        return False

internet_connection_test()