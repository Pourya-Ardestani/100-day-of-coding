sentence = "What is the Airspeed Velocity of an Unladen Swallow"

str_list = sentence.split()
print(str_list)

result = {word: len(word) for word in str_list}

#
print(result)