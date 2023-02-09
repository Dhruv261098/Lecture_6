# key value format (Same as JSON)
my_dic = {"a":1, "ab":1}

# key value never be same in dict
# value of dif key may be same

print(my_dic["a"])

# In JSON you must use "" for key but in python you can use '' also (But "" recommonded)

print(my_dic["ab"])
my_dic["ab"] = "Dhruv" # To change the value of any key
print(my_dic["ab"])

my_dic = {"a":1, "ab":[1,2,3]}
print(my_dic["ab"])
print(type(my_dic["ab"]))

