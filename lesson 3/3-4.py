is_member  = True
purchase_total = 120

if is_member and purchase_total >= 100:
    print("Discount applies")
else: 
    print("No discount")
    
has_coupon = False
is_vip = False

if has_coupon or is_vip:
    print("Discount applies")
else:
    print("No discount")
    
is_locked = False

if not is_locked:
    print("You can open the door")
else:
    print("The door is locked")