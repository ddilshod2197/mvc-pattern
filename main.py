# Strategy patterni namoyish qiluvchi klasslar
from abc import ABC, abstractmethod

# Strategy klassi
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategy klasslari
class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Credit card strategy: {amount} paid")

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"PayPal strategy: {amount} paid")

# Context klassi
class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def pay(self, amount):
        self._strategy.pay(amount)

# Tayyorlash klassi
class PaymentFactory:
    @staticmethod
    def create_strategy(strategy_type):
        if strategy_type == "credit_card":
            return CreditCardStrategy()
        elif strategy_type == "paypal":
            return PayPalStrategy()
        else:
            raise ValueError("Unknown strategy type")

# Tayyorlash
def main():
    payment_factory = PaymentFactory()
    payment_context = PaymentContext(payment_factory.create_strategy("credit_card"))
    payment_context.pay(100)

    payment_context.strategy = payment_factory.create_strategy("paypal")
    payment_context.pay(100)

if __name__ == "__main__":
    main()
```

Kodni o'rganish uchun quyidagilar qilishingiz mumkin:

1. `PaymentStrategy` klassi - Strategy klassi, unda `pay` metodi mavjud.
2. `CreditCardStrategy` va `PayPalStrategy` klasslari - Concrete strategy klasslari, ular `PaymentStrategy` klassidan meros olgan va `pay` metodi mavjud.
3. `PaymentContext` klassi - Context klassi, u `PaymentStrategy` klassidan meros olgan va `pay` metodi mavjud.
4. `PaymentFactory` klassi - Tayyorlash klassi, u `PaymentStrategy` klassidan meros olgan va `create_strategy` metodi mavjud.
5. `main` funktsiyasi - Tayyorlash funktsiyasi, u `PaymentFactory` klassidan meros olgan va `create_strategy` metodi mavjud.
