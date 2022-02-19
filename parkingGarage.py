# Parking Garage Project

# Methods
    # takeTicket
        # show availavle spots
        # select spot
        # decrease amount of tickets by 1
        # decrease parkingSpace by 1
    
    # payForParking
        # display input with amount from user and stores it
        # if payment variable is not empty display that their ticket has been paid and they have 15 mins to leave
        # update currentTicket dictionary key "paid" to True

    # leaveGarage
        # if ticket paid display "Thank you, have a nice day."
        # if not paid input prompt for payment 
            # once paid display "Thank you, have a nice day"
        # update parkingSpaces list to increase by 1, (meaning add to the parkingSpaces list)
        # update ticket list to increase by 1, (meaning add to the tickets list)

# Attributes required
    # tickets - list
    # parkingSpace - list
    # currentTicket - dictionary

class ParkingGarage():

    # defining parameters
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9]
        self.parkingSpace = [1,2,3,4,5,6,7,8,9]
        self.currentTicket = {}

    def takeTicket(self, tickets):
        # tickets reduce by 1
        self.tickets.pop(0)
        print(self.tickets.pop(0))
        # parkingSpaces reduce by 1

        # add to dictionary

        # display ticket number - pop
        print(f'Your ticket number is {tickets.pop()}')
        pass

    def payForParking(self, currentTicket):
        # prompt for value (ticket number) store in payment variable
        spot = input('What is your ticket number? ')
        
        # if payment variable is not empty (ticket has been paid) display message: 15 minutes to leave
        if currentTicket[spot]:
            pass
        
        # update currentTicket dict key "paid" to true
        

    def leaveGarage():
        # if ticket paid, dict value == True display: Thank you, have a nice day
        # if not paid display: input for payment
            # when paid display: Thank you, have a nice day
        # update update parkingSpaces list to increase by 1
        # update tickets list to increase by 1
        pass


    def runParkingGarage():
        while True:
            response = input('What do you want to do? (T)Take Ticket/ (P)Pay for Ticket/ (L)Leave Garage/ (Q)Quit')
            
            if response.lower() == 'q':          
                print('Thanks for shopping')
                break
            elif response.lower() == 't':
                ParkingGarage.takeTicket()
                pass
            elif response.lower() == 'p':
                ParkingGarage.payForParking()
                pass   
            elif response.lower() == 'l':
                ParkingGarage.leaveGarage()
                pass

        return

run = ParkingGarage()
run.runParkingGarage()
