# 4. Functions
def happy_brithday():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Fred...")
    print("Happy Birthday to you!")
    happy_brithday()
print("**************************************************************")
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount} is due on {due_date}")

display_invoice("nour", 1000, "1/1/2021")  # Call the function with sample arguments
print("**************************************************************")
def Create_name(first_name, last_name):
    first_name=first_name.capitalize()
    last_name=last_name.capitalize()
    return first_name +" "+ last_name
full_name=Create_name("nour", "mohamed")
print(full_name)