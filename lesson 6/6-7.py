text = "Hello world"

print("Hello" in text)  # True
print("bye" in text)    # False

print(text.startswith("Hel"))   # True
print(text.startswith("bye"))   # False

print(text.endswith("rld")) # True
print(text.endswith("bye")) # False  OBS! CASE SENSITIVE

text = "Hello WORLD"
print(text.endswith("rld")) # FALSE

print(text.lower().endswith("rld")) # True Her har vi gjort om teksten til små bokstaver først.


