#Tuple is immutable and represent with ()

fruits = ("apple", "banana", "mango", "grape")
print("Fruits tuple:", fruits)

print("First fruit:", fruits[0])   # apple
print("Last fruit:", fruits[-1])   # Negative indexing which returns grape

for fruit in fruits:
    print("I like", fruit)


# Packing
person = ("Sameer", 22, "Lahore")

# Unpacking
name, age, city = person
print(name)  # Sameer
print(age)   # 22
print(city)  # Lahore
