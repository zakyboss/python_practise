# for i in range(0,3):
#    print(i)
#    Next, we’ll look at range(start, stop), with values passed for when the iteration should start and for when it should stop:
for i in range(20,25):
   print(i)
#    he step argument of range() is similar to specifying stride while slicing strings in that it can be used to skip values within the sequence.

# With all three arguments, step comes in the final position: range(start, stop, step). First, let’s use a step with a positive value:
for i in range(0,15,3):
   print(i)
#    We can also use a negative value for our step argument to iterate backwards, but we’ll have to adjust our start and stop arguments accordingly:

for i in range(100,0,-10):
   print(i)
#    For Loops using Sequential Data Types
# Lists and other data sequence types can also be leveraged as iteration parameters in for loops. Rather than iterating through a range(), you can define a list and iterate through that list.

# We’ll assign a list to a variable, and then iterate through the list:
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for shark in sharks:
   print(shark)
#    Lists and other sequence-based data types like strings and tuples are common to use with loops because they are iterable. You can combine these data types with range() to add items to a list, for example:
# sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
# goat='mee'
# for item in range(len(sharks)):
#    sharks.append(goat)

# print(sharks)
# Here, we have added a placeholder string of 'shark' for each item of the length of the sharks list.

# You can also use a for loop to construct a list from scratch:
integers = []  # Initialize an empty list

while True:  # Infinite loop to continuously get input
    i = input("Enter a value (or type 'done' to finish): ")  # Ask the user for input
    if i.lower() == 'done':  # Check if the user wants to stop
        break  # Exit the loop if the user types 'done'
    else:
        try:
            integers.append(int(i))  # Convert input to integer and append to list
        except ValueError:
            print("Please enter a valid integer.")

print("You entered:", integers)  # Display the list of entered integers


print(integers)