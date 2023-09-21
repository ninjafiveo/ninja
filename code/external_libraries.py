#pip install in the terminal
# Click Terminal (in VS Code) --> "New Terminal"
# In the terminal type "pip install name_of_library"
# External Libraries (Modules) @ https://pypi.org/
# Go to terminal and type in "pip install bs4"
# Go to terminal and type in "pip install requests"

import requests
from bs4 import BeautifulSoup

url = "https://chs.canfieldschools.net/quick-links/teacher-websites"
info = requests.get(url)
soup = BeautifulSoup(info.text, "html.parser")
# print(soup.prettify())

html_element = soup.find_all("a")

for item in html_element:
    print(item.text)

