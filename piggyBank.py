class PiggyBank():
    ''' Piggy Bank class '''

    #class variable
    currency = 'USD'

    def __init__(self, name=None, balance=0.0):
        '''Initializes the instance '''
        self.name = name
        self.balance = balance

    def deposit(self, money=0.0):
        '''Add money to your account'''
        self.balance += money
            
    def display(self):
        '''Display the current balance'''
        return self.balance

    def withdraw(self, money=0.0):
        '''withdraw money from your account'''
        self.balance -= money

    def showName(self):
        '''show user name'''
        return self.name


if __name__== "__main__":
    
    #Take input from user
    name = input('Enter the name of the user: ')
    initBal = float(input('Enter starting balance: '))

    account = PiggyBank(name, initBal) #create an instance

    flag = 1
    while(flag):
        print('\n------Press the numbers accordingly to perform the operation-----')
        print('1. Deposit money\n2. Withdraw money\n3. Show current balance')
        print('4. Show account name\n5. Quit')

        cmd = int(input())

        if cmd == 1:
            money = float(input('Enter the amount to deposit: '))
            account.deposit(money)
            print('Current balance is {} {}'.format(account.display(), account.currency))

        elif cmd == 2:
            money = float(input('Enter the amount to withdraw: '))
            account.withdraw(money)
            print('Current balance is {} {}'.format(account.display(), account.currency))

        elif cmd == 3:
            print('Current balance is {} {}'.format(account.display(), account.currency))

        elif cmd == 4:
            print('Account name: {}'.format(account.name))

        elif cmd == 5:
            while(flag):
                check = input('Are you sure you want to exit? [y / n]: ')
                
                if check == 'y' or check == 'Y':
                    print('exiting the program. See you again!')
                    flag = 0
                else:
                    break
            
            
        
