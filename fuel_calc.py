import csv
import json
import requests
from fake_useragent import UserAgent


def main():
    ice_types = {"Dark Glitter": {"Heavy Water": 691,
                                  "Liquid Ozone": 1381,
                                  "Strontium Clathrates": 69},
                 "Enriched Clear Icicle": {"Heavy Water": 104,
                                           "Liquid Ozone": 55,
                                           "Strontium Clathrates": 1,
                                           "Helium Isotopes": 483},
                 "Glare Crust": {"Heavy Water": 1381,
                                 "Liquid Ozone": 691,
                                 "Strontium Clathrates": 35},
                 "Gelidus": {"Heavy Water": 345,
                             "Liquid Ozone": 691,
                             "Strontium Clathrates": 104},
                 }
    h_water_cnt = 0
    l_ozone = 0
    s_clathrates = 0
    h_isotopes = 0

    print("Hi!")
    print("Enter initial data :")
    ore_efficiency = float(input("Ore efficiency (ex. 0.83) = "))

    d_glitter_cnt = int(input("Dark Glitter count = "))
    icicle_cnt = int(input("Enriched Clear Icicle count = "))
    g_crust_cnt = int(input("Glare Crust count = "))
    gledius_cnt = int(input("Gelidus count = "))

    ice_types.get("Dark Glitter").update({"cnt": d_glitter_cnt})
    ice_types.get("Enriched Clear Icicle").update({"cnt": icicle_cnt})
    ice_types.get("Glare Crust").update({"cnt": g_crust_cnt})
    ice_types.get("Gelidus").update({"cnt": gledius_cnt})

    for ice, value in ice_types.items():
        print(ice)
        h_water_cnt += value.get("Heavy Water") * value.get("cnt") * ore_efficiency
        l_ozone += value.get("Liquid Ozone") * value.get("cnt") * ore_efficiency
        s_clathrates += value.get("Strontium Clathrates") * value.get("cnt") * ore_efficiency
    h_isotopes = ice_types.get("Enriched Clear Icicle").get("Helium Isotopes") * ice_types.get("Enriched Clear Icicle").get("cnt") * ore_efficiency

    print("We have:")
    print("Heavy Water:", h_water_cnt)
    print("Liquid Ozone:", l_ozone)
    print("Strontium Clathrates:", s_clathrates)
    print("Helium Isotopes:", h_isotopes)








# print(type(ice_types))
# print(ice_types.get("Gelidus").get("Heavy Water"))

if __name__ == "__main__":
    main()
