'''
Lists are indexed,ordered,muttable or modifible
- index
- order
- modified

'''

empty_lst = []
print(empty_lst, len(empty_lst))



countries = ['Finland','Sweden','Norway','Denmark', 'Iceland']
names = ['Donald J. Trump', 'Elon Mosk', 'Bill Gates']
fruits = ['Mango','Apple','Avocado','Banana']
nums = [1, 2, 3, 4]
# print(nums, len(nums), type(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[0] == nums[-4])
last_index = len(nums) - 1
print(nums[last_index])
print(nums[0:2])
print(nums[1:3])
print(nums[2:])
print(nums[-3:-1])
