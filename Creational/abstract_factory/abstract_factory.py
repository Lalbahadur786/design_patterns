from abc import ABC, abstractmethod
from factory import TrainTicketFactory


# Abstarct Factory 
class TrainTypeAndBookingFactory(ABC):

    @abstractmethod
    def get_train(self):
        pass

    def book_ticket(self, train_class_type):
        self.get_train() # Display Train type to user
        train_ticket_class = TrainTicketFactory.create_ticket(train_class_type)
        train_ticket_class.book()

# Concrete factory 1
class RajdhaniTrainTicketFactory(TrainTypeAndBookingFactory):
    def get_train(self):
        print("Your Ticket being booked under Rajdhani.")

# Concrete factory 2
class DuruntoTrainTicketFactory(TrainTypeAndBookingFactory):
    def get_train(self):
        print("Your Ticket being booked under Durunto.")

# Concrete class 3
class VandeBharatTrainTicketFactory(TrainTypeAndBookingFactory):
    def get_train(self):
        print("Your Ticket being booked under VandeBharat.")
    
    
class TrainTicketBookingFactory():
    @staticmethod
    def select_train(train_type):
        if train_type.lower() == "rajdhani":
            return RajdhaniTrainTicketFactory()
        elif train_type.lower() == "duranto":
            return DuruntoTrainTicketFactory()
        elif train_type.lower() == "vandebharat":
            return VandeBharatTrainTicketFactory()
        else:
            raise Exception(f"Invalid train type: {train_type}")



if __name__ == "__main__":
    train_ticket_booking_factory =  TrainTicketBookingFactory()
    train_ticket_booking_factory.select_train("Rajdhani").book_ticket("sleeper")
