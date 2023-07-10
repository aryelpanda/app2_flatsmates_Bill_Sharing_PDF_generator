class Bill:
    """
    Object tat contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period


class FlatMate:
    """
    Creates a flatmate  person who loves in the flat and pays a share od the bill
    """

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):

        weight = self.days_in_house / \
            (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
