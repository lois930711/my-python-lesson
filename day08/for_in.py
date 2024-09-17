# for in 用来遍历可迭代对象
# 什么是可迭代对象？
# 简单说，就是可以通过 [数字] 索引来获取饿，并且数字还是连续的
# list tuple  -> 都是通过 [0]  [1]  [2]

my_list = ['a', 'b', 'c', 'd']
my_tuple = ('e', 'f', 'g', 'h')

for my_list_item in my_list:
    if my_list_item == 'b':
        print('bbbbbb')
        break
    else:
        print(my_list_item)

print('-----')

target_index = -1  # -1 or None
for my_list_item_index, my_list_item in list(enumerate(my_list)):
    if my_list_item == 'b':
        target_index = my_list_item_index
        break
print(target_index)
if target_index != -1:
    my_list[target_index] = 'bbbbbb'
print(my_list)


print('======')


current_index = 0
end_index = len(my_list)

while True:
    current_item = my_list[current_index]
    if current_item == 'b':
        print(current_item)

    current_index = current_index + 1
    if current_index == end_index:
        break
