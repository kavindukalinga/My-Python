import random
import urllib.request


def downimg(url):
    name=random.randrange(1,1000) # Giving a random name to the file
    fullname=str(name)+".jpg"
    urllib.request.urlretrieve(url,fullname)

# Example
downimg("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg")


