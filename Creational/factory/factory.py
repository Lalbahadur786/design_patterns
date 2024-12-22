"""
Train ticket booking system with only one function as book train classes would be sleeper, two-tier and first-tier
using factory design pattern.
"""
# Design pattern: Factory
# Interface implemented by concrete classes with common abstract method
# Factory class has a static method to create objects of concrete classes based on input
# Concrete objects returned and used by client to call concrete methods

from abc import ABC, abstractmethod

# Ticket interface
class Ticket(ABC):
    @abstractmethod
    def book(self):
        pass

# Concrete class 1
class SleeperClass(Ticket):
    def book(self):
        print("Ticket has been booked for Sleeper class.")

# Concrete class 2
class TwoTierClass(Ticket):
    def book(self):
        print("Ticket has been booked for Two-tier class")

# Concerte class 3
class FirstTierClass(Ticket):
    def book(self):
        print("Ticket has been booked for Fisrt-tier class.")

# Factory class
class TrainTicketFactory:
    @staticmethod
    def create_ticket(ticket_class):
        if ticket_class.lower() == "sleeper":
            return SleeperClass()
        elif ticket_class.lower() == "twotier":
            return TwoTierClass()
        elif ticket_class.lower() == "firsttier":
            return FirstTierClass()
        else:
            raise ValueError(f"Invalid ticket class selected: {ticket_class}")

if __name__ == "__main__":
    ticket_factory = TrainTicketFactory()
    sleeper_class = ticket_factory.create_ticket("sleeper")
    sleeper_class.book()
