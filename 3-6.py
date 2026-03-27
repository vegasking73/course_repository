is_logged_in = True
is_admin = False

if is_logged_in:
    print("User is logged in")
    if is_admin:
        print("Show admin panel")
    else: 
        print("Show regular dashboard")
else: 
    print("Redirect login page")
