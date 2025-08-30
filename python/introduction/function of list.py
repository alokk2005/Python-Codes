numbers=[10,0,-1,7,8,10,67]

# 1. slicing
print(numbers[1:3])  # start from 1 and print till 2 

# 1.1 extended slicing
print(numbers[0:5:3])  #start from 0 and print till 5 and print index 3


# 2. sorting
numbers.sort()
print(numbers)

# 3. Reverse
numbers.reverse()
print(numbers)

# 4. Minimum & Maximum
print(min(numbers))
print(max(numbers))

# 5. Add elements to list use append() at last position
numbers.append(45)
print(numbers)

# 5.1 Add elements to list at specific position
numbers.insert(2,50)
print(numbers)

# 5.2 Add more than one elements to list at specific position
numbers.extend([44,46,47,78,89])
print(numbers)

# 6. Change the element in list
numbers[1]=38
print(numbers)

# 7. Remove the elements in list
numbers.remove(38)
print(numbers)

# 7. Pop = remove last element by default
numbers.pop(0)
print(numbers.pop())
print(numbers)

# 7. count the elements in list
print(numbers.count(0))
