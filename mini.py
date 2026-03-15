import os
import art
from datetime import datetime
balance = 500000
#history=[]

print(art.welcome)

def show_menu():
    print("press 1 for checking balance")
    print("press 2 for depositing money")
    print("press 3 for withdrawing money")
    print("press 5 for Exit")
    print("press 4 for Show Passbook")

def get_money():
    global balance
    #os.system("cls")
    print(balance)

def deposite_money():
    global balance
    #os.system("cls")
    print(balance)
    amount=int(input("Enter amount value: "))
    if amount>=0:
        balance+=amount
    else:
        print("Pls enter valid amount")
        return
    now=datetime.now()
    st=f"{now} - Deposited amount: {amount}\n"
    with open("tran.txt",'a') as file:
        file.write(st)
    # transaction_history(st)
    get_money()

def withdraw_money():
    global balance
    #os.system("cls")
    print(balance)
    amount=int(input("Enter amount value: "))
    if amount>=0 and amount<=balance:
        balance-=amount
    else:
        print("Insufficient balance")
        return
    st=f"Withdraw amount: {amount}\n"
    with open("tran.txt",'a') as file:
        file.write(st)
    # transaction_history(st)
    get_money()

# def transaction_history(log):
#     global history
#     history+=log

# def show_tran_history():
#     global history
#     for log in history:
#         print(log)


def show_passbook():
    get_money()
    with open("tran.txt",'r') as file:
        print(file.read())



def exit():
    #os.system("cls")
    print("exit")
    print(art.exit)


while True:
    show_menu()
    press = int(input("Enter your value: "))
    os.system('cls')
    if press==1:
        get_money()

    elif press==2:
        deposite_money()

    elif press==3:
        withdraw_money()

    #elif press==4:
        #transaction_history(log)
    
    #elif press==5:
        #show_tran_history()

    elif press==4:
        show_passbook()

    elif press==5:
        exit()
        break
    
    else:
        print("pls enter the correct input")
        
