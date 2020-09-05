from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"

page =  urlopen(url) #returns a HTTPResponse object
html = page.read().decode("utf-8") # reads the html as a string and  decodes in utf format
soup = BeautifulSoup(html, "html.parser")  #Beautifulsoup object arguments string tells the object which parser to use.

print(soup.get_text()) #gets the text and remove all the html tags

soup.find_all("img") #returns all the img html_tags from the BeautifulSoup obj. in a list 
