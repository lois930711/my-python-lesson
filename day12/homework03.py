from mock_data02 import fruit_price_list

# a = "bob"
# b = 123
# print(a+" "+str(b))
# 计算客户需需要的商品的总价，
# 并且给出详细的报价单
# 输入示例：
# [
#     {
#         'fruit_name': '苹果',
#         'weight': 2
#     },
#     {
#         'fruit_name': '香蕉',
#         'weight': 1
#     },
#     ...
# ]
# 返回购物清单，格式如下：
# {
#     'total_price': 120,
#     'details': [
#         '苹果 | 2份 | 总价：10元',
#         '香蕉 | 1份 | 总价：3元',
#     ]
# }


# def get_total_price():
#     pass


# # 测试
# # 顾客要购买的商品列表和重量
# shopping_list = [
#     {
#         'fruit_name': '苹果',
#         'weight': 2
#     },
#     {
#         'fruit_name': '香蕉',
#         'weight': 1
#     }
# ]
# purchase_details = get_total_price(shopping_list)
# print('purchase_details')
# print(purchase_details)
# print('----- divider -----')

# 方法一
def get_total_price(shopping_list, fruit_price_list):
    detail_list = []
    unit_total_price_list = []

    for shopping_list_item in shopping_list:
        for fruit_price_list_item in fruit_price_list:
            if shopping_list_item["fruit_name"] == fruit_price_list_item["fruit_name"]:
                unit_total_price = shopping_list_item["weight"] * \
                    fruit_price_list_item["unit_price"]
                break
        unit_total_price_list.append(unit_total_price)
        total_price = sum(unit_total_price_list)
        detail_list_item = shopping_list_item["fruit_name"] + \
            "|"+str(shopping_list_item["weight"]) + \
            "份"+"|"+"总价："+str(unit_total_price)+"元"
        detail_list.append(detail_list_item)

    purchase_details_dic = {
        "total_price": total_price,
        "details": detail_list
    }

    return purchase_details_dic

# 方法二


def get_total_price2(shopping_list, fruit_price_list):
    detail_list = []
    unit_total_price_list = []

    for shopping_list_item in shopping_list:
        unit_price_list = list(filter(
            lambda item: item['fruit_name'] == shopping_list_item['fruit_name'], fruit_price_list))

        if len(unit_price_list) > 0:
            unit_price = unit_price_list[0]["unit_price"]
            unit_total_price = unit_price * shopping_list_item['weight']
            unit_total_price_list.append(unit_total_price)
            total_price = sum(unit_total_price_list)
            detail_list_item = shopping_list_item["fruit_name"] + \
                "|"+str(shopping_list_item["weight"]) + \
                "份"+"|"+"总价："+str(unit_total_price)+"元"
            detail_list.append(detail_list_item)

    purchase_details_dic = {
        "total_price": total_price,
        "details": detail_list
    }

    return purchase_details_dic


# # 测试
# # 顾客要购买的商品列表和重量
shopping_list = [
    {
        'fruit_name': '苹果',
        'weight': 2
    },
    {
        'fruit_name': '香蕉',
        'weight': 1
    }
]
purchase_details = get_total_price2(shopping_list, fruit_price_list)
print('purchase_details')
print(purchase_details)
print('----- divider -----')
