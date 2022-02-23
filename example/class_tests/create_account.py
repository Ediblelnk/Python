#import the Account class
from account_class import Account

#create account object instances
acct = Account("admin", "1234", "admin information")
acct2 = Account("student", "0987", "student information")

#test the case for correct login and multiple accounts
acct.login("admin", "1234")
print(acct.loggedin)
print(acct.getInfo())

#test case for incorrect login and multple accounts
acct2.login("falselogin", "9203")
print("\n" + str(acct2.loggedin))
print(acct2.getInfo())