class bank:
    def transaction(self):
        print("Total Transaction Value")
    def account_opening(self):
        print("An account has been opened")
    def deposits(self):
        print("this will display the deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transactions between HDFC and ICICI")

class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.deposits()
i.transaction()
i.account_opening()