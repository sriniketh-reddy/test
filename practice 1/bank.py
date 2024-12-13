class Bank:
    def __init__(self):
        self.accBal = 10000
    def viewOptions(self):
        print("\n 1.Deposit\n 2.Withdraw\n 3.Bal Enquiry\n 4.EXIT\n")
    def validate(self):
        count = 0
        while(count<3):
            pin = int(input("Enter PIN No: "))
            if pin==2909:
                obj.viewOptions()
                break
            else:
                count += 1
                print("Wrong PIN! Please try again") if (count!=3) else print("Your Accout is blocked!")
    def deposit(self):
        amount = int(input("\nEnter Depositing Amount: "))
        if amount<100: print("\nMinimum deposit amount should be 100rs/-")
        elif amount%100!=0: print("\nDepositing amount should be multiples of 100")
        elif amount>50000: print("\nMaximum deposit amount is 50K")
        else:
            self.accBal += amount
            print(amount,"debited in your bank acount successfully!!")
    def withdraw(self):
        amount = int(input("\nEnter Withdrawl Amount: "))
        if amount<100: print("Minimum withdrawl amount should be 100rs/-")
        elif amount%100!=0: print("WIthdraw amount should be multiples of 100")
        elif amount>20000: print("Maximum withdraw transaction limit is 20K")
        else:
            if self.accBal-amount<500: print("Bank Account should maintain min Bal of 500rs/- \n Your current Bal is",self.accBal)
            else:
                self.accBal -= amount
                print(amount,"is credited from your account")
    def balEnquiry(self):
        print("\nYour Account Balance is: ",self.accBal)
print("Welcome to SBI Bank")
obj = Bank()
while True:
    obj.viewOptions()
    op = int(input("Please enter an option: "))
    if op==1:
        obj.deposit()
    elif op==2:
        obj.withdraw()
    elif op==3:
        obj.balEnquiry()
    elif op==4:
        print("\nThank You for your support!")
        break
    else:
        print("Enter valid option(1-4)")

