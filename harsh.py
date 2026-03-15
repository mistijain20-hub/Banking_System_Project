import os;

balance = 500

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

def showMenu():
       print("\n\n");
       print("Press 1 for checking available balance");
       print("Press 2 for deposit money");
       print("Press 3 for withdrawing money");
       print("Press 4 for Exit\n\n");

def getAmount():
       global balance;
       os.system("cls");
       print("Available balance is : ", balance); 

def depositeMoney():
       global balance;
       os.system("cls");
       amount = int(input("Pls Enter the amount to deposit: "));
       balance += amount;
       print(amount, " is successfully credited!");
       getAmount();

def withdrawMoney():
       global balance;
       os.system("cls");

       amount = int(input("Pls Enter the amount to withdraw: "));
       if(amount <= 0 or not isinstance(amount, int)):
              print("Error: Invalid amount");
              return;
       elif(amount > balance):
              print("Insufficent Balance");
              return;

       balance -= amount;
       print(amount, " is successfully debited!");
       getAmount();






os.system("cls");
print(art_welcome);
while(True):
       showMenu();
       n = int(input("Enter a Value "));
       
       if(n == 1):
              getAmount();
       
       elif(n == 2):
              depositeMoney();

       elif(n == 3):
              withdrawMoney();

       elif(n == 4):
              print("---------  Exit :)  --------");
              break;

       else:
              os.system("cls");
              print("Pls Enter the valid input");
