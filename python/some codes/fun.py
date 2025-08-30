# 1. os - interacting with the operating system
import os
print("Current working directory:", os.getcwd())

# 2. map - applying a function to all items in an iterable
numbers = ["1", "2", "3"]
mapped = list(map(int, numbers))  # Convert strings to integers
print("Mapped numbers:", mapped)

# 3. split - splitting a string
text = "Hello world from Python"
words = text.split()
print("Split words:", words)

# 4. strip - removing leading and trailing spaces
messy = "   clean me!   "
clean = messy.strip()
print("Stripped text:", clean)

# 5. append - adding an item to a list
fruits = ["apple", "banana"]
fruits.append("cherry")
print("Appended list:", fruits)

# 6. ord - getting ASCII value of a character
char = 'A'
ascii_value = ord(char)
print(f"ASCII of '{char}':", ascii_value)

# 7. isalpha - check if string contains only alphabets
name = "Alok"
print(f"Is '{name}' alphabetic?", name.isalpha())

# 8. enumerate - getting index with items
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# 9. items - iterating over key-value pairs in a dictionary
person = {"name": "Alok", "age": 21}
for key, value in person.items():
    print(f"{key}: {value}")

# 10. lambda - anonymous function
double = lambda x: x * 2
print("Double 4:", double(4))

# 11. zip - combining two lists
names = ["Alok", "Ravi", "Meena"]
scores = [90, 85, 88]
paired = list(zip(names, scores))
print("Zipped pairs:", paired)

# 12. join - joining list into string
word_list = ["Python", "is", "fun"]
sentence = " ".join(word_list)
print("Joined sentence:", sentence)
