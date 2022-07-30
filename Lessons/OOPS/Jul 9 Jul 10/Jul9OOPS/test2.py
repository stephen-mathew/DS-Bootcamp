class bank:
    def transaction(self):
        print("Total Transaction Value")
    def account_opening(self):
        print("An account has been opened")
    def deposits(self):
        print("this will display the deposited amount")
    def test(self):
        print("this is a test method in bank class")

class HDFC_bank():
    def hdfc_to_icici(self):
        print("this will show you all the transactions between HDFC and ICICI")
    def test(self):
        print("this is a test method in HDFC class")

class icici1(bank, HDFC_bank):
    pass

class icici2(HDFC_bank, bank):
    pass

class ineuron_bank:
    def account_status_icici(self):
        print("print account status in icici")

class icici3(HDFC_bank, bank, ineuron_bank):
    pass


i = icici1()
i.transaction()
i.account_opening()
i.deposits()
i.hdfc_to_icici()

i.test()


i2 = icici2()
i2.test()