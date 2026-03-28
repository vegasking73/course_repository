a = [1,2,3]
b = a # kopierer liste a. Men alt som blir lagt inn i b blir også lagt inn i a

print(b) # [1, 2, 3]

b.append(4) # Legger til 4 i b

print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4]

b = a.copy()  # kopierer liste a som egen liste
b.append(4) # Legger til 4 i b

print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4, 4]