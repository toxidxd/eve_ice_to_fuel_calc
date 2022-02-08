import json
import requests
import setup


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

ice_types = {
    "Dark Glitter": {"Heavy Water": 691,
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


def prices_request():
    print("Requesting prices from evepraisal")

    data = {"market_name": "jita",
            "items": [{"name": "Enriched Uranium"}, {"name": "Oxygen"}, {"name": "Mechanical Parts"},
                      {"name": "Coolant"}, {"name": "Robotics"}, {"name": "Heavy Water"},
                      {"name": "Liquid Ozone"}, {"name": "Strontium Clathrates"},
                      {"name": "Helium Isotopes"}, {"name": "Helium Fuel Block"}]
            }

    jdata = requests.post("https://evepraisal.com/appraisal/structured.json", data=json.dumps(data)).text
    data = json.loads(jdata)

    all_prices = {}
    for item in data["appraisal"]["items"]:
        all_prices.update({item["name"]: {"Buy": int(item["prices"]["buy"]["max"]),
                                          "Sell": int(item["prices"]["sell"]["min"])}, })

    print("Request done!")
    return all_prices


def reprocess(ice_have, raw_mat_have):
    ore_efficiency = setup.ore_efficiency
    h_water_cnt = 0
    l_ozone_cnt = 0
    s_clathrates_cnt = 0
    h_isotopes_cnt = 0

    for ice, value in ice_types.items():
        h_water_cnt += int(value.get('Heavy Water') * ice_have.get(ice) * ore_efficiency)
        l_ozone_cnt += int(value.get('Liquid Ozone') * ice_have.get(ice) * ore_efficiency)
        s_clathrates_cnt += int(value.get('Strontium Clathrates') * ice_have.get(ice) * ore_efficiency)
    h_isotopes_cnt += int(ice_types.get('Enriched Clear Icicle').get('Helium Isotopes') *
                          ice_have.get('Enriched Clear Icicle') * ore_efficiency)

    raw_mat_count = {
        'Heavy Water': h_water_cnt + raw_mat_have.get('Heavy Water'),
        'Liquid Ozone': l_ozone_cnt + raw_mat_have.get('Liquid Ozone'),
        'Strontium Clathrates': s_clathrates_cnt + raw_mat_have.get('Strontium Clathrates'),
        'Helium Isotopes': h_isotopes_cnt + raw_mat_have.get('Helium Isotopes'),
    }

    return raw_mat_count


def runs_cnt(raw_mat_count):
    runs_h_water = raw_mat_count.get("Heavy Water") // helium_f_b.get("Heavy Water")
    print(f"Enough Heavy Water for {runs_h_water} runs")
    runs_l_ozone = raw_mat_count.get("Liquid Ozone") // helium_f_b.get("Liquid Ozone")
    print(f"Enough Liquid Ozone for {runs_l_ozone} runs")
    runs_s_clathrates = raw_mat_count.get("Strontium Clathrates") // helium_f_b.get("Strontium Clathrates")
    print(f"Enough Strontium Clathrates for {runs_s_clathrates} runs")
    runs_h_isotopes = raw_mat_count.get("Helium Isotopes") // helium_f_b.get("Helium Isotopes")
    print(f"Enough Helium Isotopes for {runs_h_isotopes} runs")
    runs = [runs_h_water, runs_l_ozone, runs_s_clathrates, runs_h_isotopes]
    runs.sort()
    runs = int(runs[0])

    return runs


def cost_calc(commo_dict, prices, s_b):
    commo_cost = 0
    for item, value in commo_dict.items():
        commo_cost += prices.get(item).get(s_b) * value

    return commo_cost


def main():
    print("Fuel calculating script!")

    all_prices = prices_request()

    # count of ice available
    ice_have = {
        'Dark Glitter': setup.d_glitter,
        'Enriched Clear Icicle': setup.icicle,
        'Glare Crust': setup.g_crust,
        'Gelidus': setup.gledius,
    }

    raw_mat_have = {
        'Heavy Water': setup.h_water,
        'Liquid Ozone': setup.l_ozone,
        'Strontium Clathrates': setup.s_clathrates,
        'Helium Isotopes': setup.h_isotopes,
    }

    planet_prod_have = {
        'Enriched Uranium': setup.enr_uranium,
        'Oxygen': setup.oxygen,
        'Mechanical Parts': setup.mech_parts,
        'Coolant': setup.coolant,
        'Robotics': setup.robotics,
    }

    raw_mat_count = reprocess(ice_have, raw_mat_have)

    runs = runs_cnt(raw_mat_count)

    raw_mat_need = {
        'Heavy Water': helium_f_b.get('Heavy Water') * runs,
        'Liquid Ozone': helium_f_b.get('Liquid Ozone') * runs,
        'Strontium Clathrates': helium_f_b.get('Strontium Clathrates') * runs,
        'Helium Isotopes': helium_f_b.get('Helium Isotopes') * runs,
    }

    planet_prod_need = {
        'Enriched Uranium': helium_f_b.get('Enriched Uranium') * runs,
        'Oxygen': helium_f_b.get('Oxygen') * runs,
        'Mechanical Parts': helium_f_b.get('Mechanical Parts') * runs,
        'Coolant': helium_f_b.get('Coolant') * runs,
        'Robotics': helium_f_b.get('Robotics') * runs,
    }

    planet_prod_need_buy = {
        'Enriched Uranium': helium_f_b.get('Enriched Uranium') * runs - planet_prod_have.get('Enriched Uranium'),
        'Oxygen': helium_f_b.get('Oxygen') * runs - planet_prod_have.get('Oxygen'),
        'Mechanical Parts': helium_f_b.get('Mechanical Parts') * runs - planet_prod_have.get('Mechanical Parts'),
        'Coolant': helium_f_b.get('Coolant') * runs - planet_prod_have.get('Coolant'),
        'Robotics': helium_f_b.get('Robotics') * runs - planet_prod_have.get('Robotics'),
    }

    raw_mat_need_cost = cost_calc(raw_mat_need, all_prices, 'Buy')
    planet_prod_need_cost = cost_calc(planet_prod_need, all_prices, 'Sell')
    planet_prod_need_buy_cost = cost_calc(planet_prod_need_buy, all_prices, 'Sell')
    all_mat_cost = raw_mat_need_cost + planet_prod_need_cost
    fuel_cost = all_prices.get('Helium Fuel Block').get('Sell') * runs * 40
    profit = fuel_cost - all_mat_cost

    print(f'\nRaw mats cost (Jita Buy) {"{:,}".format(raw_mat_need_cost)} ISK')
    print(f'Planetary products cost (Jita Sell) {"{:,}".format(planet_prod_need_cost)} ISK '
          f'(Need buy {"{:,}".format(planet_prod_need_buy_cost)} ISK)')
    print(f'All mats cost {"{:,}".format(all_mat_cost)} ISK')
    print(f'Produced Fuel cost (Jita Sell) {fuel_cost} ISK')
    print(f'Profit - {"{:,}".format(profit)}')


if __name__ == "__main__":
    main()
