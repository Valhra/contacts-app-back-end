class  Money:

    def  = {
        "USD": 1.2,
        "GBP": 0.88,
        "RUB": 89,
        "PLN": 4.5 
    }

    def  blank (self, euro):
        self.euro = euro

    def usd(self):
        return self.euro * self.rates["USD"]

    def gbp(self):
        return self.euro * self.rates["GBP"]