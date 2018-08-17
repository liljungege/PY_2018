
l1_value = 0.75
l1_value_diamond = 8


l1_to_l3 = 12
l1_to_l3_gold = 0.39
l1_to_l3_vit = 10


l3_to_l4 = 16
l3_to_l4_gold = 0.897 
l3_to_l4_vit = 10
l3_to_l4_rate = 0.4878 


l4_to_l6 = 12
l4_to_l6_gold = 19.75
l4_to_l6_vit = 10



l1_value_diamond *= 0.05
l1_all = l1_value + l1_value_diamond
l2_all = l3_to_l4_gold + l3_to_l4_vit

def l1_to_l3_func():
    global l1_to_l3_value
    l1_to_l3_value = l1_to_l3 * l1_all + l1_to_l3_vit
    print(l1_to_l3_value)

def l3_to_l4_func():
    global l3_to_l4_value
    l3_to_l4_value = l3_to_l4 * l1_to_l3_value + l2_all
    print(l3_to_l4_value)

def l4_to_l6_func():
    l4_to_l6_value = l4_to_l6 * l3_to_l4_value + l4_to_l6_gold + l4_to_l6_vit
    print(l4_to_l6_value)

l1_to_l3_func()
l3_to_l4_func()
l4_to_l6_func()