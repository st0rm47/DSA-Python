animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# append() method
animals.append('Guinea Pig')
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Dog', 'Cat', 'Guinea Pig']

# extend() method
animals.extend(wild_animals)
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Dog', 'Cat', 'Guinea Pig', 'Tiger', 'Coyote']

# insert() method
animals.insert(2, 'Rat')
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Dog', 'Cat', 'Rat', 'Guinea Pig', 'Tiger', 'Coyote']

# remove() method
animals.remove('Cat')
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Dog', 'Rat', 'Guinea Pig', 'Tiger', 'Coyote']

# pop() method
animals.pop()
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Dog', 'Rat', 'Guinea Pig', 'Tiger']

# index() method
print('Index of Rat: ', animals.index('Rat'))
# Output: Index of Rat:  1

# count() method
print('Count of Rat: ', animals.count('Rat'))
# Output: Count of Rat:  1

# sort() method
animals.sort()
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Dog', 'Guinea Pig', 'Rat', 'Tiger']

# reverse() method
animals.reverse()
print('Updated animals list: ', animals)
# Output: Updated animals list:  ['Tiger', 'Rat', 'Guinea Pig', 'Dog']
