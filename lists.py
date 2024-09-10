sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)
# Indexing Lists
# Each item in a list corresponds to an index number, which is an integer value, starting with the index number 0.

print(sea_creatures[2])
# The index numbers for this list range from 0-4, as shown in the table above. So to call any of the items individually, we would refer to the index numbers like this:
print(sea_creatures[2:5])

# If we call the list sea_creatures with an index number of any that is greater than 4, it will be out of range as it will not be valid:
# print(sea_creatures[19])
# We can concatenate string items in a list with other strings using the + operator:
print('Sammy is a ' + sea_creatures[0])
# Modifying Items in Lists
# We can use indexing to change items within the list, by setting an index number equal to a different value. This gives us greater control over lists as we are able to modify and update the items that they contain.

# If we want to change the string value of the item at index 1 from 'cuttlefish' to 'octopus', we can do so like this:
sea_creatures[1]='octopus'

print(sea_creatures)
# We can also change the value of an item by using a negative index number instead:
sea_creatures[-3] = 'blobfish'
print(sea_creatures)

# Slicing Lists
# We can also call out a few items from the list. Let’s say we would like to only print the middle items of sea_creatures, we can do so by creating a slice. With slices, we can call multiple values by creating a range of index numbers separated by a colon [x:y]:
print(sea_creatures[1:4])
# When creating a slice, as in [1:4], the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), which is why in our example above the items at position, 1, 2, and 3 are the items that print out.

# If we want to include either end of the list, we can omit one of the numbers in the list[x:y] syntax. For example, if we want to print the first 3 items of the list sea_creatures — which would be 'shark', 'octopus', 'blobfish' — we can do so by typing:
print(sea_creatures[:3])
# One last parameter that we can use with slicing is called stride, which refers to how many items to move forward after the first item is retrieved from the list. So far, we have omitted the stride parameter, and Python defaults to the stride of 1, so that every item between two index numbers is retrieved.

# The syntax for this construction is list[x:y:z], with z referring to stride. Let’s make a larger list, then slice it, and give the stride a value of 2:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(numbers[1:11:2])
# Our construction numbers[1:11:2] prints the values between index numbers inclusive of 1 and exclusive of 11, then the stride value of 2 tells the program to print out only every other item.

# We can omit the first two parameters and use stride alone as a parameter with the syntax list[::z]:

print(numbers[::2])
# Modifying Lists with Operators
# Operators can be used to make modifications to lists. We’ll review using the + and * operators and their compound forms += and *=.

# The + operator can be used to concatenate two or more lists together:
sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']

print(sea_creatures + oceans)
# Because the + operator can concatenate, it can be used to add an item (or several) in list form to the end of another list. Remember to place the item in square brackets:
sea_creatures = sea_creatures + ['yeti crab']
print (sea_creatures)
print(sea_creatures * 2)
print(oceans * 3)