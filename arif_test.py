# Accounting application
from datetime import datetime
import os
acc = ''
amt = 0
accountList = os.listdir()
opStr = """
'd': Deposit Amount
't': Show all transaction
'w': Withdraw Amount
'e': End application
Enter your option, please:
"""
newAccStr = """
Creating new account
Enter account number to create:
"""
now = datetime.now()
date_str = now.strftime("%d/%m/%Y %H:%M:%S")
print(date_str)

def menuDisplay():
    acc = ''
    a = acc + '.dat'
    if a in accountList:
        option = input(opStr)
    else:
        acc = input(newAccStr)
        newAcc_2 = acc + '.dat'
        f = open(newAcc_2, 'a')
        acc_text = 'Account_number' + ': ' + acc
        list_entry1 = ['Transaction_Details', '=======================', acc_text]
        f.write('\n'.join(list_entry1))
        f.write('\n')
        list_entry2 = ['Transaction_type', 'Trans._completed_on', 'Previous_Balance', 'Trans._Amount', 'Balance']
        f.write('  '.join(list_entry2))
        f.write('\n')
        list_entry3 = ['open_account', date_str, '0.00', '0.00', '0.00']
        f.write('  '.join(list_entry3))
        f.write('\n')
        f.close()
        option = input(opStr)
    return option, acc
    
def depositAmount(acc,amt):
    if amt < 0:
        print("Insert a positive amount to deposit")
    else:
        bal = float(getBal(acc))
        newBal = bal + amt
        a = acc + '.dat'
        f = open(a,'a')
        newBal = str(newBal)
        amt = str(amt)
        bal = str(bal)
        list_entry = ['deposit_amount', date_str, bal, amt, newBal]
        f.write('  '.join(list_entry))
        f.write('\n')
        f.close()

def withdrawAmount(acc,amt):
    bal = float(getBal(acc))
    if amt > bal:
        print("You dont have sufficient balance to withdraw this amount")
    elif amt < 0:
        print("Insert a positive amount to withdraw")
    else:
        newBal = bal - amt
        a = acc + '.dat'
        f = open(a,'a')
        newBal = str(newBal)
        amt = str(amt)
        bal = str(bal)
        list_entry = ['withdraw_amount', date_str, bal, amt, newBal]
        f.write('  '.join(list_entry))
        f.write('\n')
        f.close()

def displayTransaction(acc):
    a = acc + '.dat'
    f = open(a)
    f_content = f.read()
    print(f_content)

def getBal(acc):
    a = acc + '.dat'
    a_file = open(a, "r")
    lines = a_file.readlines()
    lastLine = lines[-1]
    fields = [x for x in lastLine.split('  ')]
    balance = float(fields[-1])
    return balance

acc = input('Enter account number: ')
option = ''
while option is not 'e':
    opt = menuDisplay()
    acc = opt[1]
    option = opt[0]
    if option is 'd':
        amt = float(input("Please enter your deposit amount: "))
        depositAmount(acc,amt)
    elif option is 't':
        displayTransaction(acc)
    elif option is 'w':
        amt = float(input("Please enter your withdraw amount: "))
        withdrawAmount(acc,amt)
    elif option is 'e':
        print("Closing account and all transactions")
        exit()
    else:
        print("Please choose valid option among of either 'd' or 't' or 'w' or 'e'")
        print(opStr)
