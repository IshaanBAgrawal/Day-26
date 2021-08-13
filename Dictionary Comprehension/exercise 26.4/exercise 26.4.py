sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split()
swallow = [char for char in words[-1][0:len(words[-1]) - 1]]
result = {word: len(word) for word in words}

print(result)
