# Parking Garage Project

# imports function from another file to have a cool car image 
import car_image
image = car_image
image.playImage()

class ParkingGarage():

    # defining parameters
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9]
        self.parkingSpace = [1,2,3,4,5,6,7,8,9]
        self.currentTicket = {}

    # April was the driver, Chris and Jamia Navigators
    def takeTicket(self):
        if self.tickets:
            # display ticket number 
            print(f'Your ticket number is {self.tickets[0]}')
            
            # add to dictionary
            self.currentTicket[self.tickets[0]] = 'unpaid'
            print(self.currentTicket)
            
            # tickets reduce by 1
            print(self.tickets.pop(0))

            # parkingSpaces reduce by 1
            print(self.parkingSpace.pop(0))
        else:
            # print message if no tickets available
            print("Garage is full, Thank you!")


    def payForParking(self):
        # prompt for value (ticket number) to store in payment variable
        spot = int(input('What is your ticket number? '))
        print(type(spot))
        
        
        # if payment variable is not empty (ticket has been paid) display message: 15 minutes to leave
        if self.currentTicket.get(spot) == "unpaid": 
            print("You're ticket has been paid, you have 15 minutes to leave.")
            # update currentTicket dict key "paid" to true
            self.currentTicket[spot] = 'paid'

            print(self.currentTicket)
            # update update parkingSpaces list to increase by 1
            self.parkingSpace.append(spot)

    # April was the driver, Chris and Jamia Navigators
    def leaveGarage(self):
        # if ticket paid, dict value == True display: Thank you, have a nice day 
        vacant = int(input('What is your ticket number? '))
        # when paid display: Thank you, have a nice day
        if self.currentTicket[vacant] == "paid":
            image.playImage()
            print("                Thank you have a nice day.")
        # update tickets list to increase by 1
            self.tickets.append(vacant)
            print(self.tickets)
            print(self.parkingSpace)
        # if not paid display: message to pay ticket before leaving
        elif self.currentTicket[vacant] == "unpaid":
            print("You must pay your ticket before leaving.")
        

    # menu for calling all methods defined in our class
    def runParkingGarage(self):
        while True:
            response = input('What do you want to do? (T)Take Ticket/ (P)Pay for Ticket/ (L)Leave Garage/ (Q)Quit > ')
            
            # Quit
            if response.lower().strip() == 'q':       
                image.playImage()
                print('                Thanks for your interest, we look forward to your business.')
                break
            # Take ticket
            elif response.lower().strip() == 't':
                ParkingGarage.takeTicket(self)
            # Pay for ticket
            elif response.lower().strip() == 'p':
                ParkingGarage.payForParking(self) 
            # Leave Garage
            elif response.lower().strip() == 'l':
                ParkingGarage.leaveGarage(self)

        return

# runs the program
run = ParkingGarage()
run.runParkingGarage()
