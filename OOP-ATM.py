import random

class ATM:
    def __init__(self, name, typeCard, cardNo, expired, cvv, username, balance):
        self.name = name
        self.typeCard = typeCard
        self.cardNo = cardNo
        self.expired = expired
        self.cvv = cvv
        self.username = username
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"You deposit {amount} baht, your balance is {self.balance}.")
    def withdraw(self,amount):
        self.balance -= amount
        print(f"You withdraw {amount} baht, your balance is {self.balance}.")
    def requestOTP(self, phone):
        number = [0,1,2,3,4,5,6,7,8,9]
        otp_list = []
        for i in range(4):
            digit = str(random.choice(number))
            otp_list.append(digit)
        otp = otp_list[0] + otp_list[1] + otp_list[2] + otp_list[3]
        print(f"Your OTP will send to Phone: {phone}.")
        print(f"The OTP is {otp}")
    def transfer(self, amount, account):
        self.balance -= amount
        print(f"You transfer {amount} baht to account no: {account}, your balance is {self.balance}.")
    def loan(self,amount):
        self.balance += amount
        print(f"You loan {amount} baht, your balance is {self.balance}.")
