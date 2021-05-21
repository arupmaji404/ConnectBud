with open("details", 'r') as fptr:
    lst = fptr.readlines()

print(lst)
balance = 0
index = -1
print("1. New user 2. Already user")
choice = int(input(">> "))

userId = input("Enter userId: ")
password = input("Enter password: ")

if choice == 1:
    balance = int(input("Enter account balance: "))
else:
    for i in range(len(lst)):
        name, pwd, amt = lst[i].split(" ")
        if userId == name and password == pwd:
            print("Verification Successful")
            print(f"Welcome {name}, You are authenticated user")
            balance = int(amt)
            index = i
            break
    else:
        print("Verification Unsuccessful")
        input("Press any key to exit.")
        exit(0)

while True:

    print("[1] Check Balance \n[2] Cash Withdraw \n[3] Cash Deposit \n[4] Exit")
    choice = int(input("What do you want to do: "))
    if choice == 1:
        print('$',balance)
    elif choice == 2:
        withdraw_amount = int(input("How much money do you want to withdraw: "))
        if withdraw_amount > balance:
            print("You don't have enough money!")
        else:
            balance = balance - withdraw_amount
            print("Transaction successful.")
    elif choice == 3:
        deposit_amount = int(input("How much money do you want to deposit: "))
        balance = balance + deposit_amount
        print("Transaction successful.")
    elif choice == 4:
        print("You have logged out.")
        break
    else:
        print("That is not a valid choice.")


with open("details", "w") as fptr:

    s = userId + " " + password + " " + str(balance) + "\n"
    if index == -1:
        lst.append(s)
    else:
        lst[index] = s
    print(lst)
    fptr.writelines(lst)

