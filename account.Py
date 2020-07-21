#python 3.7.1

print ("Hello, Dcoder!")


class BankAccount:
  bank="National Bank"
  branch="Nairobi"
  def __init__(self,name, balance ,accno):
    self.name=name
    self.balance=balance
    self.accno=accno
Terry=BankAccount(name="Terry", balance=10000,accno=87453/60)
Ryan=BankAccount(name="Ryan", balance=50654,accno=67435/60)
Tracy=BankAccount(name="Tracy", balance=87946,accno=87549/60)
print(Terry.bank)
print(Ryan.name)
print(Tracy.balance)



class BankAccount:
  bank="National bank"
  
  def __init__(self,first_name,last_name):
    self.first_name=first_name
    self.last_name=last_name
    self.balance=0
    self.phonenumber=724649620
    
 #method1   
  def account_name(self):
    name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
    return name
 
 #method2   
  def deposit(self, amount):
    self .balance+=amount
    if amount>0:
      print("You have deposited {} to your account". format(amount))
    else:
      print("You cannot  deposit  {} into your account".format(amount))
 
 #method3 
  def get_balance(self):
    return("The balance for {} is {} ".format(self.account_name(),self.balance))
  
  #method4
  def withdraw(self,amount): amount>0
if self.balance>=amount:
      self.balance>=amount
      print("You have withdrawn {} from your account".format(amount))
else:
      print("You cannot withdraw {} from your account".format(amount))  
#method5
def loanamount(self,amount): amount>0
if self.balance>=amount:
      self.balance>=amount
      print("you have borrowed {} from the bank".format(amount))
else:
      print("you cannot borrow {} from the bank".format(amount))
#method6
def storeloan(self,amount):amount>0
if self.balance>amount:
    self.balance>amount
print("you have stored {} from the bank".format(amount))

 else:
      print("you have not stored {} from the bank".format(amount))
#method7
   def repayloan(self,amount)
    if self.amount:>amount:
       self.balance>amount:
       print("you have repaidloan {} from the bank".formart(amount))
       else:
       print("you have not repaid {} from the bank".format(amount))
    def reduceloan(self,amount)
     if self.amount:>amount:
        self.balnce>amount:
       print("reduce loan {} from the bank".format(amount))
       else:
       print("you cannot reduceloan {} from the bank".format(amount))
   



acc1=BankAccount("Wangare","Mungai")
acc2=BankAccount("Njoki","Caren")
print("---------")
print(acc1.account_name())
print(acc2.account_name())
print("--------")
acc1.deposit(1000)
acc2.deposit(2000)
acc1.deposit(90)
acc2.deposit(-80)
print("----------")

print(acc1.get_balance())
print(acc2.get_balance())
print("---------")


#questions  

acc3=BankAccount("Sharon","Njonjo")
acc4=BankAccount("Cherop","Rael")
print("--------")
acc3.deposit(800)
acc4.deposit(700)
acc3.deposit(600)
acc4.deposit(500)
print("----------")
acc3.withdraw(300)
acc3.withdraw(260)
acc4.withdraw(250)
acc4.withdraw(200)

print("----------")
print(acc3.get_balance())
print(acc4.get_balance())
  
    