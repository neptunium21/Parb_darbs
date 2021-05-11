
# kaut ko lidzīgo...

class Deposit1:

    def __init__(self):
        self.dep_var = {}

    def add_data(self, deposit, term, rate):
        self.dep_var[deposit] = deposit
        self.dep_var[term] = term
        self.dep_var[rate] = rate
        return "Added datas for interest calculating"

    def interest(self):
        interest = (self.abs(self.deposit - (self.deposit * ((self.rate + 1) ** self.term))))
        return interest

deposit1 = Deposit1()

deposit = int(input("Start Deposit: "))
term = int(input("Term: "))
rate = float(input("Rate: "))

print("interest =", deposit1.interest)



