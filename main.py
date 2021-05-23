from extractor import *
import json
from model import profile
from model.profile import *

#Enter the number below as string, example +91 12345 67899 
NUMBER = "+91 ***** *****" 

while(True):

    with open("info.json","r") as f:
        if len(f.read())!=0:
            f.seek(0)
            old_data_dict = json.load(f)
        else:
            old_data_dict = None
    if old_data_dict is None:#first time load
        new_data_dict = json.loads(get_data(NUMBER))
        profile_obj_old = Profile(**new_data_dict)
        with open("info.json","w") as f:
            f.write(json.dumps(profile_obj_old.get_json()))
        continue
        

    profile_obj_old = Profile(**old_data_dict)
    new_data_dict = json.loads(get_data(NUMBER))
    profile_obj_new  = Profile(**new_data_dict)
    old_orders = profile_obj_old.random_orders
    new_orders = profile_obj_new.random_orders
    order_dates = [order["order_time_gmt"] for order in old_orders]
    for order_dict in new_orders:
        if order_dict["order_time_gmt"] not in order_dates:
            old_orders.append(order_dict)
    profile_obj_old.random_orders = old_orders

    with open("info.json","w") as f:
        f.write(json.dumps(profile_obj_old.get_json(),indent=4))
        print(profile_obj_old.total_num_orders- len(profile_obj_old.random_orders))
    
    if len(profile_obj_old.random_orders) == profile_obj_old.total_num_orders:
        break
