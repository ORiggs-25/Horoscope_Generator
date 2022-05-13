class Horoscope:
    # ---- class attributes: -----------
    date = 0
    month = 0

    # ---- Mutator methods: --------------
    def setDate(self, date_input):
        self.date = date_input

    def setMonth(self, month_input):
        self.month = month_input

    # ---- accessor methods: --------------
    def getDate(self):
        return self.date

    def getMonth(self):
        return self.month

    # prompt the user to enter date and month


