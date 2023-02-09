# Duplication is not allowed
# No index for elemnets

my_set_1 = {"Desai", "Dhruv", "OM", "Jenish"}
my_set_2 = {"Dhruv", "Manav"}

# intersection() & difference() methods
print(my_set_1.intersection(my_set_2))
print(my_set_1.difference(my_set_2))

# to convert the list into set use set class (To use some usefull methods of set like intersection in list too)
# set(list_name)

# remove(), clear(), copy(), union()

print(my_set_1.union(my_set_2))

my_set_1.remove("OM")
print(my_set_1)

my_set_1.clear()
print(my_set_1)

my_set_2.copy()
print(my_set_2)
