from bs4 import BeautifulSoup
import requests
import re


print("Exploiting a Directory Listing vulnerability in a web server.")

url=input("Enter the url of the web site:> ")

try:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    for link in soup.find_all('a'):
        name=link.get('href')
        if(name[0] !='?' or name[-1]=='/'):
            print(name)
    
except:
    print("An error occur please check url or internet connection")
