names = ["John", "Jane", "Kelvin", "Joe", "Joe"]

print(names.count("Joe")) # Teller antal ganger Joe er på listen
                            # 2
                            
print(names.index("Joe")) # Viser hvilken posisjon første Joe er i
                            # 3

numbers = [1, 9, 4, 5, 2, 3] 
numbers.sort() # sorterer numbers i rekkefølge
print(numbers) # [1, 2, 3, 4, 5, 9]

numbers.reverse() # sorterer numbers i motsatt rekkefølge
print(numbers) # [9, 5, 4, 3, 2, 1]