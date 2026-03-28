# list[start:stop]

numbers = [1,2,3,4,5,6]

print(numbers[0:3]) # Deler lista frem til FØR 3.posisjon
                    # [1, 2, 3]
                    
print(numbers[2:-1]) # Deler list fra posisjon 2 til FØR siste posisjon
                        # [3, 4, 5]
                    
print(numbers) # Numnber er fortsatt den samme [1, 2, 3, 4, 5, 6]

print(numbers[2:10]) # Hvis listen har mindre enn 10 posisjoner, viser den hele listen fra posisjon 2 (I dette tilfellet) 
                        # [3, 4, 5, 6]