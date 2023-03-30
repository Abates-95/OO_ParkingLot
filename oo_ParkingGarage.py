#!/usr/bin/env python
# coding: utf-8

# In[145]:


class ParkingGarage():
    
    
    """
    The ParkingGarage class allows a user to simply input a 
    Letter or Number to navigate through a small menu
    and either take a ticket pay for a ticket or leave.
    for every ticket taken, ticket avaialability and spots available reduce by 1
    once ticket has been paid user is prompted to leave within 15 min
    for every person that leaves ticket availability and spots available increase by 1
    
    """
    
    
     # initialize ticket list, spots list and currentTicket value
    def __init__(self):
        self.ticket = [1,2,3,4]
        self.spots = [1,2,3,4]
        self.currentTicket = {'paid':False}

    # Allows user to hypothetically print a ticket.  
    # Also reduces ticket list and spot list amount by 1
    # and stores in respective global variables 
    def takeTicket(self):
        global ticketPop 
        global spotPop
        global stub
        inp = input('\nPress "A" to accept or "M" to go back to main menu: ')
        if inp.lower() == 'a':
            stub = True
            ticketPop = self.ticket.pop()
            spotPop = self.spots.pop()
            print('Thank you! Please take your ticket')
        else:
            pass

    # Function asks user to input the integer 5
    # Will not accept any other input
    def payForParking(self):
        paid = input('\nTicket price is $5. Please enter "5": ')
        paid_already = self.currentTicket.get('paid')
        if stub != True and int(paid) == 5:
            print('\nYou dont have a ticket!')
        elif paid_already == True and int(paid) == 5:
            print('\nYou have already paid!')
        elif int(paid) != 5:
            print('\nERROR: Wrong Amount ')
        elif int(paid) == 5:
            print('\n!Thank you, you have 15 min to leave!')
            self.currentTicket['paid'] = True
            ticketCount + 1
            spotCount + 1
            stub == False
    
    # Function allows user to leave only if they have paid
    # and prompts user to pay if they have not
    # and appends 1 ticket and 1 spot back into lists for availablitiy
    def leaveGarage(self):
        value = self.currentTicket.get('paid')
        if value == True:
            print('\nHave a nice day')
            value == False
            if self.ticket[-1] == 3:
                self.ticket.append(4)
                self.spots.append(4)
            elif self.ticket[-1] == 2:
                self.ticket.append(3)
                self.spots.append(3)
            elif self.ticket[-1] == 1 :
                self.ticket.append(2)
                self.spots.append(2)
        elif value == False:
            fee = input('\nYou have not paid yet! Enter "5": ')
            if int(fee) == 5 or fee == '$5':
                value == True
                print('\nThank you, you have 15min to leave')
                if self.ticket[-1] == 3:
                    self.ticket.append(4)
                    self.spots.append(4)
                elif self.ticket[-1] == 2:
                    self.ticket.append(3)
                    self.spots.append(3)
                elif self.ticket[-1] == 1 :
                    self.ticket.append(2)
                    self.spots.append(2)
            else:
                print('\nERROR: Wrong amount')


toll = ParkingGarage()
 
 
def Run():

    while True:
        response1 = input(f"\nWelcome, there are {toll.ticket[-1]} tickets available and {toll.spots[-1]} spots available. \nPress 'T' for ticket menu, 'P' to pay, 'L' to leave or 'Q to quit': ")

        if response1.upper() == "T" and len(toll.ticket) != 1:
            toll.takeTicket()
        elif response1.upper() == "P":
            toll.payForParking()
        elif response1.upper() == "L":
            toll.leaveGarage()
        elif response1.upper() == "Q":
            break
Run()


# In[ ]:





# In[ ]:





# In[ ]:




