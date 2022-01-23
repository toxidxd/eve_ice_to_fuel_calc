import csv
import json
import requests
from fake_useragent import UserAgent

print("Hell")

# 4 x Enriched Uranium*
# 22 x Oxygen*
# 4 x Mechanical Parts*
# 9 x Coolant*
# 1 x Robotics*
# 170 x Heavy Water*
# 350 x Liquid Ozone*
# 20 x Strontium Clathrates*
# 450 x Helium Isotopes*

data = {"market_name": "jita", "items": [{"name": "Enriched Uranium"}, {"name": "Oxygen"}, {"name": "Mechanical Parts"},
                                         {"name": "Coolant"}, {"name": "Robotics"}, {"name": "Heavy Water"},
                                         {"name": "Liquid Ozone"}, {"name": "Strontium Clathrates"},
                                         {"name": "Helium Isotopes"}, {"name": "Nitrogen Fuel Block"}]
        }

jdata = requests.post("https://evepraisal.com/appraisal/structured.json", data=json.dumps(data),
                      headers={'User-Agent': UserAgent().chrome}).text

data = json.loads(jdata)
print(data)
print(type(data))
all_mats = []
for item in data["appraisal"]["items"]:
    print(item["name"], " ", item["prices"]["sell"]["percentile"])
    cur_item = [item["name"], item["prices"]["sell"]["percentile"]]
    all_mats.append(cur_item)

with open("prices.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["mat", "price"])
    for line in all_mats:
        writer.writerow(line)

print("File written!")
