# Non-OOP
# Bank 3
# Two accounts

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show(accountNumber):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password    
    
    if accountNumber == 0:
        print(f'The account details are for account number {accountNumber}:')
        print('     Name', account0Name)
        print('     Balance:', account0Balance)
        print('     Password:', account0Password)
        print()

    if accountNumber == 1:
        print(f'The account details are for account number {accountNumber}:')
        print('     Name', account1Name)
        print('     Balance:', account1Balance)
        print('     Password:', account1Password)
        print()



def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance


def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    
    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
    
    if accountNumber == 0:
        accountBalance = account0Balance + amountToDeposit
        return accountBalance
    if accountNumber == 1:
        accountBalance = account1Balance + amountToDeposit
        return accountBalance

def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
    
    if accountNumber == 0:
        if amountToWithdraw > account0Balance:
            print('You cannot withdraw more than you have in your account')
            return None
    if accountNumber == 1:
        if amountToWithdraw > account1Balance:
            print('You cannot withdraw more than you have in your account')
            return None
    
    if accountNumber == 0:
        accountBalance = account0Balance - amountToWithdraw
        return accountBalance
    if accountNumber == 1:
        accountBalance = account1Balance - amountToWithdraw
        return accountBalance

newAccount(0, 'Joe', 100, 'soup')
newAccount(1, 'Kate', 200, 'stew')
    
while True:
    print()
    print('Select 0 or 1')
    accountNumber = input('Which is your account number? ')
    accountNumber = int(accountNumber)
    
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(accountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(accountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 's':
        print('Show:')
        show(accountNumber)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newWithdrawal = withdraw(accountNumber, userWithdrawAmount, userPassword)
        if newWithdrawal is not None:
            print(f'You withdrew {userWithdrawAmount}, Your new balance is: {newWithdrawal}')

print('Done')