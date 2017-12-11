import urllib.request
import random

def download_image(url):
    name = random.randrange(1, 1000)
    F_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, F_name)



