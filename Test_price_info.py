import price_info

def test_total_cost_shopping():
    price_arr=price_info.price_list
    quantity_arr=price_info.quantity_list
    test_total_cost= sum(price_arr[item]*quantity_arr[item] for item in price_arr if item in quantity_arr)
    result =price_info.total_cost_shopping()
    assert result== test_total_cost

def test_cost_of_fruit():
    price_arr=price_info.price_list
    quantity_arr=price_info.quantity_list
    test_item='orange'
    test_item_quantity=5
    test_item_price=1.4
    test_cost_of_fruit=test_item_quantity*test_item_price
    result=price_info.cost_of_fruits(test_item,test_item_quantity)
    assert result==test_cost_of_fruit
