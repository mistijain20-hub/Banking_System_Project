
import os



art_welcome = ''' __      __       .__                                .___            _____          
/  \    /  \ ____ |  |   ____  ____   _____   ____   |   | ____     /     \ ___.__. 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  |   |/    \   /  \ /  <   |  | 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/  |   |   |  \ /    Y    \___  | 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  > |___|___|  / \____|__  / ____| 
       \/       \/          \/            \/     \/           \/          \/\/      
__________                __                                                        
\______   \_____    ____ |  | __                                                    
 |    |  _/\__  \  /    \|  |/ /                                                    
 |    |   \ / __ \|   |  \    <                                                     
 |______  /(____  /___|  /__|_ \                                                    
        \/      \/     \/     \/                                                    '''



ava_bal = 30000
print(art_welcome)

while(True):
    print("Welcome to Our Banking System")
    
    press=int(input("Enter "))
    if press==1:
        print("Available balance:",ava_bal)
    if press==2: 
        print("Available balance:",ava_bal)
        enter_amount = int(input("Enter amount for deposite:"))
        if enter_amount>0:
            ava_bal += enter_amount;
            print("Congrats!✨ ","Your current available balance:",ava_bal)
            
        else:
            print("Enter valid amount")
    if press==3:
        print("Available balance:",ava_bal)
        enter_amount = int(input("Enter amount for withdrawal:"))
        if enter_amount<=0:
            print("Enter valid amount")
        if enter_amount > ava_bal:
            print("You've no sufficient money")
        else:
            ava_bal -= enter_amount
            print("Congrats!✨ ","Your current available balance:",ava_bal)
        
    if press==4:
        print("Exit")
        break;

    os.system('cls')
        