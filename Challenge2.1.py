#creating a class called BankAccount
class BankAccount:

#private attributes for account number, account holder name,accountbalance
  def __init__(self, account_number,account_holder_name,account_balance = 0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = account_balance 

#adding methods to deposit money, withdraw money and display the account balance 
#to deposit 
  def deposit (self,amount):
    if amount > 0:
      self.__account_balance += amount 
      print("The amount you deposited is ₹{}.the current balance is ₹{}.".format(amount,
      self.__account_balance))
    else:
      print("Invalid deposit amount.")
      
#to withdraw 
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount 
      print("The amount you withdrawn is ₹{}." "the current balance is ₹{}.".format(amount,
            self. __account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
      
#to display the account balance 
  def display_balance(self):
    print("Account balance for {} (A/c #{}) is ₹{}.".format(self.__account_holder_name,self.__account_number,
self.__account_balance))
    
#creating an object for class  
obj = BankAccount(account_number = "987654321",
account_holder_name = "Ms.Durga", account_balance = 10000)

obj.display_balance()
obj.deposit (2000)
obj.withdraw (5000)
obj.display_balance ()

      

  