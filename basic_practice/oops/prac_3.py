# create a class train which has method of book ticket and show fare and number of seats available

class Train:
    def __init__(self,destination,passenger_num):
        self.destination=destination
        self.passenger_num=passenger_num
        self.seats_available=100
        self.fare=1010

    def book_Ticket(self):

        if self.passenger_num<self.seats_available:
            print("Ticket booked successfully ")
            self.seats_available=self.seats_available-self.passenger_num
            print(f"Number of ticket available is {self.seats_available}")

    def getStatus(self):

        print(f"ticket requested for destination : {self.destination}")
        print(f"Number of seats available : {self.seats_available}")
        print(f"fare for {self.destination} is :  {self.fare}")
        print("")

p1=Train("Lucknow",4)
p1.getStatus()
p1.book_Ticket()

