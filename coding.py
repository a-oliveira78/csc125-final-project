import random
accounts = {}
def create_account(name, email, phone):
    user_id = generate_user_id()
    accounts[user_id] = {
        "Name" : name,
        "Phone" : phone,
        "Email" : email,
        "Books borrowed" : [],
        "Books returned" : []
    }

def delete_account(entered_id):
    if entered_id in accounts:
        del accounts[entered_id]
        return f"Account {entered_id} successfully deleted\n"
    return f"Account {entered_id} not found. Please try again"
    
def generate_user_id():
    while True:
        user_id = random.randint(10000,99999)
        if user_id not in accounts:
            return user_id
        
def borrow_book(name, book):
    for user_id, acc in accounts.items():
        if acc["Name"] == name:
            if len(acc["Books borrowed"]) < 5:
                acc["Books borrowed"].append(book)
                return (("- " * 30) + "\nBook successfully checked out\n" + ("- " * 30))
            else:
                return(("- " * 30) + "\nERROR - Books taken out exceeds capacity. Please return a book first\n" + ("- " * 30))
    return "No account found for that name. Please try again."

def return_book(name, book):
    for user_id, acc in accounts.items():
        if acc["Name"] == name:
            if len(acc["Books borrowed"]) > 0:
                if book in acc["Books borrowed"]:
                    if book not in acc["Books returned"]:
                        acc["Books borrowed"].remove(book)
                        acc["Books returned"].append(book)
                        return(("- " * 30) + "\nBook successfully returned\n" + ("- " * 30))
                    else:
                        acc["Books borrowed"].remove(book)                        
                        return(("- " * 30) + "\nBook successfully returned\n" + ("- " * 30))
                else:
                    return(("- " * 30) + "\nERROR - This book is not currently borrowed by you. Please borrow a book first\n" + ("- " * 30) + "\n")
            else:
                return "There are currently no books borrowed.\n"
    return "Account not found. Please try again.\n"

def to_string(entered_input):
    entered_input = entered_input.strip()
    for user_id, acc in accounts.items():
        if (entered_input.isdigit() and user_id == int(entered_input)) or acc["Name"] == entered_input.title() or acc['Email'] == entered_input:
            return (("- " * 30) + f"User ID: {user_id} \nName: {acc['Name']}\nPhone: {acc['Phone']}\nEmail: {acc['Email']}\nBooks out: {acc['Books borrowed']}\nBook History: {acc['Books returned']}\n" + ("- " * 30))
    return "No accounts found for that input. Please try again"

def view_history(entered_input):
    entered_input = entered_input.strip()
    for user_id, acc in accounts.items():
        if (entered_input.isdigit() and user_id == int(entered_input)) or acc["Name"] == entered_input.title() or acc['Email'] == entered_input:
            return (f"Book history for account #{user_id}:\nBooks borrowed: {acc['Books returned']}\nBooks returned: {acc['Books returned']}" + ("- " * 30))
    return "No accounts found. Please try again"


print(("- " * 30) + "\n\nHello, welcome to the BH Bookstore!\n\n" + ("- " * 30))
while True:
    print("How can I help you?\n")
    print("\tA. Create Account")
    print("\tB. Borrow Book")
    print("\tC. Return Book")
    print("\tD. View book history")
    print("\tE. View account history")
    print("\tF. Delete account")
    print("\tG. EXIT")

    user_choice = input().strip().lower()
    
    if user_choice == 'a':
        print("Option A: Create Account\n")
        print("please enter a name: ")
        name = input().strip().title()
        print("please enter an email: ")
        email = input().strip()
        print("please enter a phone number: ")
        phone = input().strip()
        while phone.isdigit() == False or (phone.isdigit() == True and len(phone) != 10):
            print("ERROR = Please enter a valid phone number: ")
            phone = input().strip()
        phone = int(phone)
        create_account(name, email, phone)
        print("Account successfully created")
    elif user_choice == 'b':
        print("Option B: Borrow Book")
        print("Enter account name you would like to access: ")
        acc_name = input().strip().title()
        print("Enter book you would like to borrow: ")
        acc_book = input().strip()
        print(borrow_book(acc_name, acc_book))
    elif user_choice == 'c':
        print("Option C: Return Book")
        print("Enter account name you would like to access: ")
        acc_name = input().strip().title()
        print("Enter book you would like to return: ")
        acc_book = input().strip()
        print(return_book(acc_name, acc_book))
    elif user_choice == 'd':
        print("Option D: View book history")
        print("Enter the name, email, or account # you would like to view: ")
        entered_input = input().strip()
        print(view_history(entered_input))
    elif user_choice == 'e':
        print("Option E: View account history")
        print("Enter the name, email, or account # you would like to print: ")
        entered_input = input().strip()
        print(to_string(entered_input))
    elif user_choice == 'f':
        print("Option F: Delete Account\n")
        print("please enter user ID: ")
        entered_id = int(input().strip())
        print(delete_account())
    elif user_choice == 'g':
        print("Option G: EXIT")
        break
    else:
        print("Invalid choice, please select 'A', 'B', 'C', 'D', 'E', 'F', or 'G': ")

print("THANK YOU FOR VISIING BH BOOKSTORE! COME AGAIN SOON")
print("- " * 8)
print("Exiting program...")