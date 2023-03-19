#SBI Bank

#Account create (method) --[name,accno] ,minbalnce-5000
# total balance=minbalance

#Deposit (method)--[cash] == minbalance+deposit amnt 'balance amount credited=amnt

#Withdrawn
class Bank:
    bank_name='SBI'
    def details(self,name,accno):
        self.name=name
        self.accno=accno
        self.minbalance=0
        self.balance=self.minbalance
        # print("Details: ",self.name,self.accno)

    def deposit(self,deposit_amnt):
        self.deposit_amnt=deposit_amnt
        self.balance=self.balance+self.deposit_amnt
        print(self.name,"Your",Bank.bank_name,'accnt no ',self.accno,"account has credited with  amount",self.deposit_amnt)

    def withdrawn(self,withdraw):
        self.withdraw=withdraw
        if self.withdraw>self.balance:
            print("Insufficent amount")
        else:
            self.balance=self.balance-self.withdraw
            print("Your",Bank.bank_name,'account debited amount is ',self.withdraw)

    # def printvalue(self):
    #     print(self.name,'Account ',self.accno,'balance is',self.minbalance)

ba1=Bank()
ba1.details("Arun",'12345')
ba1.deposit(5000)
ba1.withdrawn(7000)






