import webbrowser
import testing
from testing import parse_data
from testing import execute_data
from testing import find_born_year
import requests
from bs4 import BeautifulSoup
import time

name = (str(input("masukkan nama yang mau kamu cari tahu ... "))).title()
start_url = "https://en.wikipedia.org/wiki/" + name 
response = requests.get(start_url)
time.sleep(10)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all(class_="infobox-label")

#find notable works
notable_works = execute_data(result)

#find year of birth
year_born = find_born_year(result)

#find complete data
complete_data = f"{name} was born on {year_born}\n\nSome notable works of {name} are:\n\n{notable_works}"

with open("output.txt", "w") as file:
    file.write(complete_data)   

webbrowser.open("output.txt")


