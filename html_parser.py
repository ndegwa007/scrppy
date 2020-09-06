from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup

url = "http://olympus.realpython.org/profiles/dionysus"

page =  urlopen(url) #returns a HTTPResponse object
html = page.read().decode("utf-8") # reads the html as a string and  decodes in utf format
soup = BeautifulSoup(html, "html.parser")  #Beautifulsoup object arguments string tells the object which parser to use.

print(soup.get_text()) #gets the text and remove all the html tags

soup.find_all("img") #returns all the img html_tags from the BeautifulSoup obj. in a list 


browser = mechanicalsoup.Browser() #headless browser

url = "http://olympus.realpython.org/login"
login_page = browser.get(url) #gets the url
login_html = login_page.soup #parses the html

form = login_html.select("form")[0] #select all forms in the html
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profile_page = browser.submit(form, login_page.url)

links = profile_page.soup.select("a") #selects links with <a> ancor element in profile page html

for link in links:
    address = url + link["href"]
    text = link.text 
    print(f"{text}:{address}")