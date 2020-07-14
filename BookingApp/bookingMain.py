import datetime
from People import passenger
from People.passenger import Passenger


class Bookingapp(Passenger):
    def __init__(self, fname, lname, passportNumber, DoB):
        super().__init__(fname, lname, passportNumber, DoB)

    @classmethod
    def createUser(cls):
        return cls(
            input('First Name: '),
            input('Last Name: '),
            int(input('PassportNumber: ')),
            input('Date of Birth in DD/MM/YYYY format: ')
        )

    @staticmethod
    def userStore():
        passengerB = {}
        for i in range(1):
            user = Bookingapp.createUser()
            passengerB[user.fname] = user
            print(passengerB.items())


user = Bookingapp
user.createUser()
