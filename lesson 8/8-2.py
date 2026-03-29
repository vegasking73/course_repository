def compute_total(price, tax_rate=.0625):
    
    tax = price * tax_rate
    print(tax)
    total = price + tax
    return(total)

print(compute_total(100)) # 106.25
print(compute_total(100, 1)) # 200
print(compute_total(price=100, tax_rate=.1))

    
