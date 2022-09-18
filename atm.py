
from random import randrange
import sys


print("     *******WELCOME TO MARIAMMAN INDIAN BANK*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
first_name = input("\n Enter your First name: ").upper()
last_name = input(" Enter your last name :").upper()
name=first_name+" "+last_name 
try:
    phone_number=int(input(" Enter your phone number:" ))
except:
    print("\nInvalid number! Please Enter the valid Phone number ")
    phone_number=int(input("Enter your phone number:" ))    
    print("Congratulations! Account created successfully......\n")
else:
    print("Congratulations! Account created successfully......\n")
account_number=randrange(1757584938,1846463298) 
print("\n Your Account number :",account_number)
        
class atm():
    def __init__(self, name, account_number, phone_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.phone_number = phone_number
        self.balance = balance
         
    def account_detail(self):
        print("\n----------ACCOUNT DETAILS----------")
        print(f" Account Holder: {self.name}")
        print(f" Account Number: {self.account_number}")
        print(f" Phone Number  : {self.phone_number}")
        print(f" Available balance: Rs.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Rs.{amount} withdrawal successfully...")
            print("Current account balance: Rs.", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: Rs.", self.balance)
        print()
 
    def transaction(self):
        print("""
            TRANSACTION
        ---------------------
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        ----------------------
        """)
       
        while True:
            try:
                option = int(input("Enter Your's choice:"))
            except:
                print("ERROR! Invalid number\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("Enter the amount to be credited:"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("Enter the amount to be debited:"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
          ******************************************
              Transaction is now complete.                        
              Transaction number: {randrange(10000, 1000000)} 
              Account holder    : {first_name+""+last_name}                  
              Account number    : {self.account_number}                
              Phone number      : {self.phone_number}
              Available balance : Nu.{self.balance}

 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                sys.exit()
                 
 

 
atm = atm(name, account_number, phone_number)
 
while True:
    trans = input("\nDo you want to do any transaction? (yes/no):").lower().strip()
    if trans == "yes":
        atm.transaction()
    elif trans == "no":
        print("""
     ***********************************   
     Thanks for choosing us as your bank 
             Visit us again!                     
     ***********************************
        """)
        break
    else:
        print("Wrong command!  Enter 'yes' or 'no' only \n")