from mock_data import product_price_list


# # 练习：
# # 计算商品的总价
# # 传入参数示例：[('苹果', 10), ('香蕉', 5), ('橙子', 8)]，表示：10份苹果，5份香蕉，8份橙子
# # 返回结果为以上商品的总价，例如：120
# def calc_total_price(list: list[tuple[str, int]]) -> int:
#     pass


# # 调用
# purchase_list = [('苹果', 10), ('香蕉', 5), ('橙子', 8)]
# total_price = calc_total_price(purchase_list)
# print("total_price", total_price)

# 方法一
def calc_total_price(purchase_list, product_price_list):
    price_cost_list = []
    for purchase_list_item in purchase_list:
        for product_price_list_item in product_price_list:
            if purchase_list_item[0] == product_price_list_item[0]:
                price_cost = purchase_list_item[1] * product_price_list_item[1]
                price_cost_list.append(price_cost)
                break
    total = sum(price_cost_list)
    return total

# 方法二


def calc_total_price2(purchase_list, product_price_list):
    price_cost_list = []
    for purchase_list_item in purchase_list:
        unit_price = list(
            filter(lambda item: item[0] == purchase_list_item[0], product_price_list))
        if len(unit_price) > 0:
            price_cost = purchase_list_item[1] * unit_price[0][1]
            price_cost_list.append(price_cost)
            total = sum(price_cost_list)
    return total

# 方法二（教学）


# def calc_total_price(purchase_list: list[tuple[str, int]], product_price_list: list[tuple[str, int]]):
#     pass


purchase_list = [('苹果', 10), ('香蕉', 5), ('橙子', 8)]
total_price = calc_total_price2(purchase_list, product_price_list)
print("total_price", total_price)
