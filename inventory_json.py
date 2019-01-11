import json

from object_oriented_utility.oops_util import Inventory


def inventory_runner():
    try:
        with open('../object_oriented_utility/Inventory.json', 'r') as jf:
            json_str = jf.read()
            jf.close()
            json_value = json.loads(json_str)

        i_obj = Inventory(json_value)
        i_obj.inventory_materials()
        i_obj.see_category()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    inventory_runner()