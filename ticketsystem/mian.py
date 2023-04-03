

class Main():
    def __init__(self):
        while True:

            user_input = input("input a number:")

            match user_input:
                case "1":  # make a ticket
                    staff_ID = input("input staff ID")
                    email = input("input email")
                    creator_name = input("input creator_name")
                    description_issue = input(
                        "give a description of the issue: ")
                    Ticket(staff_ID, email, creator_name, description_issue)

                case "2":  # print stats of all tickets
                    print(Ticket.ticket_info_all())

                case "3":  # print stats of a ticket
                    print("Printing ticket info")
                    ticket = self.find()
                    print(ticket.ticket_info())

                case "4":  # add response to ticket
                    print("adding a response to a ticket")
                    ticket = self.find()
                    response = input("input the response: ")
                    ticket.resolve(response)

                case "5":  # close a ticket
                    print("closing a ticket")
                    ticket = self.find()
                    ticket.close()

                case "6":  # exit program
                    exit()

                case _:  # if user doesn't inputs wrong
                    print("that is not one of the options :(")

    # this is to find a ticket because ticket ID starts at 2000 with first ticket being 2001
    def find(self, UID=None):
        if UID is None:
            UID = int(input("input ID"))
        UID -= 2001
        ticket = Ticket.Ticket_list[UID]
        return ticket

        """
        #Linear Search "slow when there is alot of tickets but still good"
        for ticket in Ticket.Ticket_list:
            if ticket.UID == user_input:
                print(ticket.ticket_info())
                break
        """


class Ticket():
    ID = 2000
    Ticket_list = list()
    amount_open = 0  # keeping track of the amout of tickets open

    def __init__(self, staff_ID, email, creator_name, description_issue):

        # giving ticket a UID and adding one to ID
        self.UID = Ticket.ID
        Ticket.ID += 1

        # inputed values
        self.staff_ID = staff_ID
        self.creator_name = creator_name
        self.email = email
        self.description_issue = description_issue
        self.response = self.password_change()

        self.ticket_status = "open"
        Ticket.amount_open += 1
        Ticket.Ticket_list.append(self)

    # The first two characters of the staffID, followed by the first three characters of the ticket creator name.
    def password_change(self):
        if self.description_issue.lower() == "password change":
            pasword = self.staff_ID[:2]  # first two characters of the staffID
            # first three characters of the ticket creator name
            pasword += self.creator_name[:3]
            return pasword
        else:
            return "not yet provided"

    def resolve(self, response):
        self.response = response
        self.close()

    def close(self):
        self.ticket_status = "closed"
        Ticket.amount_open -= 1

    def reopen(self):
        self.ticket_status = "reopened"
        Ticket.amount_open += 1

    # returns string of the info on it self
    def ticket_info(self):
        info = f"Ticket number: {self.UID}\n"
        info += f"Ticket creator: {self.creator_name}\n"
        info += f"Staff ID: {self.staff_ID}\n"
        info += f"Desctiption: {self.description_issue}\n"
        info += f"ticket status: {self.ticket_status}"
        return info

    # returns string of info of all the tickets
    def ticket_info_all(self):
        info = "--- Ticket Statistics ---\n"
        info += self.TicketStats + "\n"
        info += "------ Ticket Print ------"
        for ticket in Ticket.Ticket_list:
            info += ticket.ticket_info() + "\n\n"
        return info

    # retuns string of amout of tickets, amount open, amount closed
    def TicketStats():
        stats = f"Tickets Created: {len(Ticket.Ticket_list)}\n"
        stats += f"Tickets Resolved: {Ticket.amount_open}\n"
        stats += f"Tickets to sovle: {len(Ticket.Ticket_list)- Ticket.amount_open}\n"
        return stats


if __name__ == "__main__":
    Main()
