# dictonary = A collection of {key:value} pirs

capitals = {"India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}        

#print(dir(capitals),end = " ")
#print(help(capitals))
#capitals.update({"Bangladesh":"Dhaka"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#print(capitals)

# keys=capitals.keys()
# values=capitals.values()

# for key in keys:
#     print(key)
   
# for value in values:
#     print(value)    

# items = capitals.items()
# for item in items:          
#      print(item )

for key , value in capitals.items():
    print(f"{key}:{value}")
