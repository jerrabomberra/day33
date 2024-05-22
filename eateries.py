import json
from collections import defaultdict


def read_nyc_parks_eateries_data(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    json_file = "DPR_eateries_001.json"
    eateries_data = read_nyc_parks_eateries_data(json_file)
    # print("NYC Parks Eateries Data:")
    # print(eateries_data)

x = eateries_data[0]
print(x)
