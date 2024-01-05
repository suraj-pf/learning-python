class Atm():

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = int(input("Enter 1 for pin generation 2 for pin change 3 for balance checking and 4 for withdraw and any other to exit :-"))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.change_pin()
        elif user_input == 3:
            self.balance_check()
        elif user_input == 4:
            self.withdraw_amount()
        else :
            exit() 

    def create_pin(self):
        user_pin = int(input("Enter the new pin:-"))
        self.pin = user_pin

        user_balance = int(input("Enter the balance :-"))
        self.balance = user_balance

        print("Pin created successfully!!!!!")
        self.menu()

    def change_pin(self):
        old_pin = int(input("Enter the old name :- "))
        if old_pin == self.pin:
            user_pin = int(input("Enter the new pin:-"))
            self.pin = user_pin
            print("Pin updated successfully!!!!!")


        else :
            print("Wrong Pin!!!!!! ")
        self.menu()

    def balance_check(self):
        print("The amount in your account is :-",self.balance)
        self.menu()


    def withdraw_amount(self):
        user_input = int(input("Enter the amount you want to withdraw :-"))
        if user_input > self.balance:
            print("Insufficient funds!!!!!")
        else:
            self.balance = self.balance - user_input 
            print("Amount Withdrwan !!!!!")
            print("The amount in your account is :-",self.balance)
        
        self.menu()
        


obj = Atm()