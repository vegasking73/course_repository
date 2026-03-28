text = "HeLLo WoRLd"


print("lower: ", text.lower())  # lower:  hello world
print ("Original: ", text)      # Original:  HeLLo WoRLd
print("upper: ", text.upper())  # lower:  HELLO WORLD

text = "   HeLLo WoRLd       "
print("Stripped: ", text.strip())  # Stripped: HeLLo WoRLd
print ("Original again: ", text)      # Original again:     HeLLo WoRLd

text = "hello hello WoRLd"
print("Replaced: ", text.replace("hello", "goodbye"))   # Replaced:  goodbye goodbye WoRLd
print(text)   # hello hello WoRLd

text = "   hello hello WoRLd    "
print("Replaced: ", text.strip().replace("hello", "goodbye").upper())   # Fjerner "White space" og gjør om ordene. + Bare store bokstave" Replaced:  GOODBYE GOODBYE WORLD