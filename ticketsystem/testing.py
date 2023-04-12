"""class Ticket():
    ID = 2000
    Ticket_list = list()
    amount_open = 0  # keeping track of the amout of tickets open

    def __init__(self, staff_ID, email, creator_name, description_issue):

        # giving ticket a UID and adding one to ID
        Ticket.ID += 1
        self.UID = Ticket.ID

        # inputed values
        self.staff_ID = staff_ID
        self.creator_name = creator_name
        self.email = email
        self.description_issue = description_issue
        self.ticket_status = "open"
        Ticket.amount_open += 1
        self.response = "response"  # self.password_change()
        Ticket.Ticket_list.append(self)


ticket1 = Ticket("jay", "jay@email.com", "jay", "computer not working")


print(ticket1.staff_ID, ticket1.email, ticket1.creator_name,
      ticket1.description_issue, ticket1.ticket_status, ticket1.UID)
print(Ticket.ID, Ticket.amount_open, Ticket.Ticket_list)


ticket2 = Ticket("bob", "bob@email.com", "bob", "computer is working")

print(ticket2.staff_ID, ticket2.email, ticket2.creator_name,
      ticket2.description_issue, ticket2.ticket_status, ticket2.UID)
print(Ticket.ID, Ticket.amount_open, Ticket.Ticket_list)"""


"""class Ticket():
    def __init__(self, staff_ID, creator_name, description_issue):
        self.staff_ID = staff_ID
        self.creator_name = creator_name
        self.description_issue = description_issue
        self.response = self.password_change()

    def password_change(self):
        if self.description_issue.lower() == "password change":
            pasword = self.staff_ID[:2]  # first two characters of the staffID
            # first three characters of the ticket creator name
            pasword += self.creator_name[:3]
            # self.close() not used in testing
            return "password change: " + pasword
        else:
            return "not yet provided"


ticket1 = Ticket("jay123", "123jay", "computer not wokring")
print(ticket1.response, ticket1.description_issue)
ticket2 = Ticket("bob123", "bob123", "password change")
print(ticket2.response, ticket2.description_issue)"""


"""class Ticket():
    amount_open = 0  # keeping track of the amout of tickets open

    def __init__(self):
        self.response = "response"
        self.ticket_status = "open"
        Ticket.amount_open += 1

    def resolve(self, response):
        self.response = response
        self.close()

    def close(self):
        self.ticket_status = "closed"
        Ticket.amount_open -= 1

    def reopen(self):
        self.ticket_status = "reopened"
        Ticket.amount_open += 1


ticket1 = Ticket()
ticket2 = Ticket()
ticket3 = Ticket()


print(ticket1.amount_open, ticket1.response, ticket1.ticket_status)

ticket2.resolve("this ticket has been resolved")
print(ticket2.amount_open, ticket2.response, ticket2.ticket_status)

ticket3.close()
print(ticket3.amount_open, ticket3.response, ticket3.ticket_status)

ticket3.reopen()
print(ticket3.amount_open, ticket3.response, ticket3.ticket_status)
"""


"""class Ticket():

    def __init__(self, staff_ID, email, creator_name, description_issue):
        self.UID = 2000
        self.creator_name = creator_name
        self.email = email
        self.staff_ID = staff_ID
        self.description_issue = description_issue
        self.response = "response"
        self.ticket_status = "open"

    # returns string of the info on it self
    def ticket_info(self):
        info = f"Ticket number: {self.UID}\n"
        info += f"Ticket creator: {self.creator_name}\n"
        info += f"Staff ID: {self.staff_ID}\n"
        info += f"Email address: {self.email}\n"
        info += f"Desctiption: {self.description_issue}\n"
        info += f"response: {self.response}\n"
        info += f"ticket status: {self.ticket_status}"
        return info


ticket1 = Ticket("jay", "jay@email.com", "jay", "computer not working")
print(ticket1.ticket_info())

ticket2 = Ticket("bob", "bob@email.com", "bob", "computer is working")
print(ticket2.ticket_info())"""


"""class Ticket():
    Ticket_list = ["ticket2001", "ticket2002", "ticket2003"]

    def find(UID=None):

        if UID is None:
            UID = int(input("input ID: "))
        UID -= 2001
        if UID >= 0 and UID < len(Ticket.Ticket_list):
            ticket = Ticket.Ticket_list[UID]
            return ticket
        else:
            return None


print(Ticket.find())
print(Ticket.find())
print(Ticket.find())
print(Ticket.find())
print(Ticket.find())"""
