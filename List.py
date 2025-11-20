#List is mutable and represent with []

mixed = [1, "hello", True, 3.14]
print("Mixed list:", mixed)

fruits = ["apple", "banana", "mango", "grape"]
print("Fruits:", fruits)

if "Apple" in fruits:
    print("Apple is in the list!")
else:
    print("Apple is not in the list.")

for fruit in fruits:
    print("I like", fruit)

fruits.append("kiwi")      # Add at the end
fruits.append("orange")      # Add at the end
fruits.insert(1, "pear")   # Add at index 1
print("After adding:", fruits)

fruits.remove("kiwi")
print("After removing Kiwi:", fruits)
fruits.pop() #LIFO
print("After removing Orange:", fruits)