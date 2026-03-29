# Funskjon 1:

def say_hello():   # function stasrter med def. say_hello er navnet på funksjonen
    print("Hello!")
    print("Welcome to Python!")
    
say_hello()   # Dette gir output:   Hello!
              #                     Welcome to Python!
              
# Funksjon 2: 

def greet(name):
    print("Hello, " + name)
    
greet("Kenneth")  # Hello, Kenneth

# Funksjon 3:

def add(a,b):
    return a + b

print(add(5,9)) # 14

# Funskjon 4

a = 1 + 2 
b = 2 + 3

def test(a,b):
    return a + b

print(add(a,b))  # 8
    