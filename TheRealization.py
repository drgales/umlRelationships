from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₱{amount:.2f} in cash.")


def main():
    payment = CashPayment()
    payment.pay(500.00)


if __name__ == "__main__":
    main()