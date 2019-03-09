
secret = "7363"
balance = 120000
def mainloop():
    inp = input("enter code \n")
    if inp != secret:
        print("The secret code you entered is unrecognised \n")
        return 0
    else:
        inp = input("Welcome costumer! \n"
                    "input 1 to check your balance \n"
                    "input 2 to withdraw \n"
                    "input 3 to change your secret code \n"
                    "input 4 to close \n")
    global funchoice
    if inp != '4':
        funchoice[inp]()
    else:
        return 4


def printbalance():
    print(balance)
    return


def withdraw():
    global balance
    amount = int(input("Enter the amount you wish to withdraw \n"))
    if amount > balance:
        print("you can't withdraw an amount larger than your balance \n")
    else:
        balance = balance - amount
        print("Withdrawal successful \n")

    return


def changesecret():
    global secret
    inp = input("Enter your new secret code \n")
    if len(inp) != 4:
        print("The code you entered is invalid \n")
    else:
        secret = inp
        print("Operation successful \n")
    return


funchoice = {'1': printbalance, '2' : withdraw, '3': changesecret}


if __name__ == '__main__':
    ret = 0
    while ret != 4:
        ret = mainloop()
print("Goodbye costumer! \n")

exit()