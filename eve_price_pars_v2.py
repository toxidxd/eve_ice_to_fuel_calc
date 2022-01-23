import csv
import json
import requests

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

jdata = requests.post("https://evepraisal.com/appraisal/structured.json", data=json.dumps(data)).text

data = json.loads(jdata)
print(data)
print(type(data))
all_prices = {}
for item in data["appraisal"]["items"]:
    print(f'{item["name"]}')
    print(f'Buy {item["prices"]["buy"]["max"]}')
    print(f'Sell {item["prices"]["sell"]["min"]}\n')

    # cur_item = [item["name"], item["prices"]["sell"]["percentile"]]

    all_prices.update({item["name"]: {"Buy": item["prices"]["buy"]["max"],
                                      "Sell": item["prices"]["sell"]["min"]},
                       }
                      )

print(all_prices.items())
print(all_prices.get("Coolant").get("Sell"))

# with open("prices.csv", "w", newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(["mat", "price"])
#     for line in all_mats:
#         writer.writerow(line)

print("File written!")
