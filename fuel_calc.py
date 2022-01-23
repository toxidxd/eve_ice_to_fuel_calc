import csv
import json
import requests
import setup
from fake_useragent import UserAgent


def main():
    print("Fuel calculating script!")
    helium_f_b = {
        "Enriched Uranium": 4,
        "Oxygen": 22,
        "Mechanical Parts": 4,
        "Coolant": 9,
        "Robotics": 1,
        "Heavy Water": 170,
        "Liquid Ozone": 350,
        "Strontium Clathrates": 20,
        "Helium Isotopes": 450,
    }

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
        # print(ice)
        h_water_cnt += value.get("Heavy Water") * value.get("cnt") * ore_efficiency
        l_ozone_cnt += value.get("Liquid Ozone") * value.get("cnt") * ore_efficiency
        s_clathrates_cnt += value.get("Strontium Clathrates") * value.get("cnt") * ore_efficiency
    h_isotopes_cnt += ice_types.get("Enriched Clear Icicle").get("Helium Isotopes") * ice_types.get("Enriched Clear Icicle").get("cnt") * ore_efficiency

    print("We have:")
    print("Heavy Water:", h_water_cnt)
    print("Liquid Ozone:", l_ozone_cnt)
    print("Strontium Clathrates:", s_clathrates_cnt)
    print("Helium Isotopes:", h_isotopes_cnt)
    print()
    runs_h_water = h_water_cnt // helium_f_b.get("Heavy Water")
    print(f"Enough Heavy Water for {runs_h_water} runs")
    runs_l_ozone = l_ozone_cnt // helium_f_b.get("Liquid Ozone")
    print(f"Enough Liquid Ozone for {runs_l_ozone} runs")
    runs_s_clathrates = s_clathrates_cnt // helium_f_b.get("Strontium Clathrates")
    print(f"Enough Strontium Clathrates for {runs_s_clathrates} runs")
    runs_h_isotopes = h_isotopes_cnt // helium_f_b.get("Helium Isotopes")
    print(f"Enough Helium Isotopes for {runs_h_isotopes} runs")
    runs = [runs_h_water, runs_l_ozone, runs_s_clathrates, runs_h_isotopes]
    runs.sort()
    print()
    print(f"Enough materials for {int(runs[0])} runs.")

    print("\nPlanetary what we need:")

# print(type(ice_types))
# print(ice_types.get("Gelidus").get("Heavy Water"))

if __name__ == "__main__":
    main()
