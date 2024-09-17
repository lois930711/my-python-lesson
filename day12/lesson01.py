from mock_data02 import fruit_price_list


# 找出 fruit_price_list 列表中，所有价格小于10的水果
# list(filter(lambda item: item["unit_price"] < 10, fruit_price_list))


# filtered_list = []
# for fruit_price_list_item in fruit_price_list:
#     if fruit_price_list_item["unit_price"] < 10:
#         filtered_list.append(fruit_price_list_item)
# print(filtered_list)


# 列表解析
filtered_list = [
    fruit_price_list_item for fruit_price_list_item in fruit_price_list if fruit_price_list_item["unit_price"] < 10]
print(filtered_list)
print("----- divider -----")

# 三元表达式
gender = 0  # 0 ： 女， 1 ： 男
gender_text = ''
if gender == 0:
    gender_text = "女"
else:
    gender_text = "男"

gender_text = "女" if gender == 0 else "男"
