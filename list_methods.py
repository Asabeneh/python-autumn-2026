'''

append
pop
insert
remove
extend
del
list_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
empty_lst = []
print(dir(empty_lst))
shopping_list = ['Milk', 'Potatoes','Tomatoes','Onion','Tea', 'Coffee', 'Sugar']
print(shopping_list, len(shopping_list))
shopping_list.append('Meat')
print(shopping_list)
shopping_list.append('Yoghurt')
print(shopping_list)
fruits = ['Mango','Apple','Avocado','Banana']
vegs = ['Cabbage','Beetroot','Horse raddish']
shopping_list.extend(fruits + vegs)
print(shopping_list)
shopping_list.insert(3, 'Garlic')
print(shopping_list)
shopping_list.insert(0, 'Meat')
print(shopping_list)
print('Milk' in shopping_list)
print(shopping_list.index('Milk'))
nums = [1, 1, 2, 2, 3, 4, 5, 5, 5]
print(nums.count(5))
# nums.pop()
print(nums.count(5))
print(nums)
nums.pop(0)
print(nums)
shopping_list.pop(0)
print(shopping_list)
shopping_list.remove('Sugar')
print(shopping_list)
nums.remove(5)
print(nums)
nums[6] = 6
print(nums)

countries = ['Finland','Sweden','Norway','Denmark', 'Iceland']
countries_copy = countries.copy()
# countries_copy.reverse()
# print(countries)
# print(countries_copy)
countries_copy.sort(reverse=True)
print(countries_copy)
