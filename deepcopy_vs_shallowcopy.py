import copy

class fruit:
    def __init__(self, color, height, width, list1=None):
        self.color = color
        self.height = height
        self.width = width
        self.list1 = list1

print()
print("######### Testing classes #######")
apple_1 = fruit("red", 2, 3)
orange_1 = apple_1
apple_1.color = "orange"
print(apple_1.color, orange_1.color)


# test shallow copy
apple_2 = fruit("red", 2, 3)
orange_2 = copy.copy(apple_2)
apple_2.color = "orange"
print("After shallow copy: ", apple_2.color, orange_2.color)


# test deep copy
apple_3 = fruit("red", 2, 3)
orange_3 = copy.deepcopy(apple_3)
apple_3.color = "orange"
print("After deep copy: ", apple_3.color, orange_3.color)


# test for list
print()
print("######### Testing lists #######")
list1 = [1,2,3,4]
list2 = list1

list1[1] = 5
print(list1, list2)

list1 = [1,2,3,4]
list2 = copy.copy(list1)
list1[1] = 5
print("After shallow copy: ", list1, list2)

list1 = [1,2,3,4]
list2 = copy.deepcopy(list1)
list1[1] = 5
print("After deep copy: ", list1, list2)


# test for list of list
print()
print("######### Testing list of lists #######")
list1 = [[1,2,3,4]]
list2 = list1

list1[0][1] = 5
print(list1, list2)

list1 = [[1,2,3,4]]
list2 = copy.copy(list1)
list1[0][1] = 5
print("After shallow copy: ", list1, list2)

list1 = [[1,2,3,4]]
list2 = copy.deepcopy(list1)
list1[0][1] = 5
print("After deep copy: ", list1, list2)



print()
print("######### Testing lists inside classes #######")
apple_1 = fruit("red", 2, 3, [1,2,3,4])
orange_1 = apple_1
apple_1.list1[1] = 5
print(apple_1.list1, orange_1.list1)


# test shallow copy
apple_2 = fruit("red", 2, 3, [1,2,3,4])
orange_2 = copy.copy(apple_2)
apple_2.list1[1] = 5
print("After shallow copy: ", apple_2.list1, orange_2.list1)


# test deep copy
apple_3 = fruit("red", 2, 3, [1,2,3,4])
orange_3 = copy.deepcopy(apple_3)
apple_3.list1[1] = 5
print("After deep copy: ", apple_3.list1, orange_3.list1)

