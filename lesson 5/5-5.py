numbers = [1,2,3,4,3]

numbers.remove(3) # Fjerner første tall 3
print(numbers) # [1, 2, 4, 3]

numbers.pop(-2) # Fjerner nest siste posisjon
print(numbers) # [1, 2, 3]

numbers.pop() # Fjerner siste posisjon
print(numbers) # [1, 2]

numbers.clear() # Fjerner alt på listen
print(numbers) # []
