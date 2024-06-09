#Lists
shopping_list = ["milk", "pasta", "eggs", "poha", "bread", "rice"]
print(shopping_list)
print(shopping_list[0])
print(shopping_list[1])
print(len(shopping_list))


shopping_list.append("biscuits")
print(shopping_list)

shopping_list.insert(2, "chips")
print(shopping_list)


shopping_list.extend(["cake", "cookies"])
print(shopping_list)

shopping_list.remove("eggs")
print(shopping_list)
print(shopping_list.pop())

my_list = [1, 2, 3, 3.142, "Hello"]
print(my_list)