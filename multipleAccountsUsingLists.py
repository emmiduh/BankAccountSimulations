# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('     Name', accountNamesList[accountNumber])
    print('     Balance', accountBalancesList[accountNumber])
    print('     Password', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if amountToWithdraw > accountBalancesList[accountNumber]:
            print('You cannot withdraw more than you have in your account')
            return None

    accountBalance = accountBalancesList[accountNumber] - amountToWithdraw
    return accountBalance

def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount')
        return None
    
    accountBalance = accountBalancesList[accountNumber] + amountToDeposit
    return accountBalance

print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print("## Welcome to M-Bank ## \n")
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do ? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    if action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter your account anumber: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    if action == 'w':
        print('Withdrawal:')
        userAccountNumber = input('Please enter your account anumber: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        userWithdrawalAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        newWithdrawal = withdraw(userAccountNumber, userWithdrawalAmount, userPassword)
        if newWithdrawal is not None:
            print('Your new balance is:', newWithdrawal)
    
    if action == 'n':
        print('New Account:')
        newAccountName = input('Please enter the account name: ')
        newAccountBalance = input('Please enter the account balance: ')
        newAccountBalance = int(newAccountBalance)
        newAccountPassword = input('Please enter the password: ')
        print("New account successfully created!")
        print(f"{newAccountName}'s account is account number: {len(accountNamesList)}")
        theNewAccount = newAccount(newAccountName, newAccountBalance, newAccountPassword)
    
    elif action == 's':
        print('Show:')
        theAccount = input('Please enter the account number of the account to show: ')
        theAccount = int(theAccount)
        show(theAccount)
        print()

    elif action == 'q':
        break

print('Done')