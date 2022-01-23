import csv
import json
import requests
import setup
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
    h_water_cnt = setup.h_water_have
    l_ozone_cnt = setup.l_ozone_have
    s_clathrates_cnt = setup.s_clathrates_have
    h_isotopes_cnt = setup.h_isotopes_have

    print("Hi!")
    ore_efficiency = setup.ore_efficiency

    d_glitter_cnt = setup.d_glitter_have
    icicle_cnt = setup.icicle_have
    g_crust_cnt = setup.g_crust_have
    gledius_cnt = setup.gledius_have

    ice_types.get("Dark Glitter").update({"cnt": d_glitter_cnt})
    ice_types.get("Enriched Clear Icicle").update({"cnt": icicle_cnt})
    ice_types.get("Glare Crust").update({"cnt": g_crust_cnt})
    ice_types.get("Gelidus").update({"cnt": gledius_cnt})

    for ice, value in ice_types.items():
        print(ice)
        h_water_cnt += value.get("Heavy Water") * value.get("cnt") * ore_efficiency
        l_ozone_cnt += value.get("Liquid Ozone") * value.get("cnt") * ore_efficiency
        s_clathrates_cnt += value.get("Strontium Clathrates") * value.get("cnt") * ore_efficiency
    h_isotopes_cnt += ice_types.get("Enriched Clear Icicle").get("Helium Isotopes") * ice_types.get("Enriched Clear Icicle").get("cnt") * ore_efficiency

    print("We have:")
    print("Heavy Water:", h_water_cnt)
    print("Liquid Ozone:", l_ozone_cnt)
    print("Strontium Clathrates:", s_clathrates_cnt)
    print("Helium Isotopes:", h_isotopes_cnt)


# print(type(ice_types))
# print(ice_types.get("Gelidus").get("Heavy Water"))

if __name__ == "__main__":
    main()
