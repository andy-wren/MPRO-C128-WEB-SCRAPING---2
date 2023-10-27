from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = ("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
stars = requests.get(START_URL, verify = False)
headers = ["Star Name", "Distance", "Mass", "Radius"]
soup = BeautifulSoup(stars.text, "html.parser")
tables = soup.find_all('table', attrs = {"class" : "wikitable sortable"})
table = tables[2]
table_rows = table.find_all('tr')
star_lists = []

for rows in table_rows:
    table_data = rows.find_all('td')
    row = [data.text.strip() for data in table_data]
    star_lists.append(row)

name = []
distance = []
mass = []
radius = []

for table_data in range(1, len(star_lists)):
    data = star_lists[table_data]
    name.append(star_lists[0])
    distance.append(star_lists[5])
    mass.append(star_lists[7])
    radius.append(star_lists[8])

data = zip(name, distance, mass, radius)

star_list = pd.DataFrame(data, columns = headers)

star_list.to_csv("field_brown_dwarfs.csv", index = False)

print("Data scraped!")
