bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit["lime"])
print fruit["orange"]
print fruit
while True:
    dict_key = raw_input("Please enter a fruit:")
    print dict_key
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print description
    else:
        print "Please enter a valid fruit"
        continue
