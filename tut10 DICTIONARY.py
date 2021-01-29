# Dictionary is nothing but key value pairs.

d1 = ()
d2 = []
d3 = {}
print(type(d1))
print(type(d2))
print(type(d3))

d4 = {"Vinit": {"B": "Halwa", "L": "Fast food", "D": "patasi"},
      "Tommy": "Bread",
      "Mom": "Roti",
      "Dad": "Simple food"}

print(d4)
print(d4["Vinit"])
d4["Lanleo"] = "Fast food"
d4["123"] = "Donkey"
d4[123] = "Donkey"
print(d4)
del d4[123]
del d4["123"]
print(d4)
print(d4["Vinit"]["L"])
d4.update({"1C": "Chocolate"})  # yeh bhi ek tarika  hai kch item add karne ka
                                     # But ham direct method use "NHI" karenge.
                          #      Ⅹ••• i.e.   d4["123"] = "Donkey" •••Ⅹ
                         # Use '''.update''' instead.

# print(d4.copy())
print(d4)
# d5 = d4
d5 = d4.copy()
del d5["Vinit"]
print(d4)
print(d5)
print(d4.get("Tommy"))  # /  print(d4["Vinit"]["L"])
print(d4.get("Vinit"))  # nhi hoga toh "none" show kar dega.

print(d4.keys())
print(d4.items())
