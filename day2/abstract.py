from abc import abstractmethod


class Payment:
    @abstractmethod
    def payment_method(self):
        pass

class upiPayment(Payment):

    def payment_method(self):
        print("upiPayment")

class cashPayment(Payment):

    def payment_method(self):
        print("cashPayment")
payment = upiPayment()
payment.payment_method()