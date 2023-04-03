

def Main():
    def __init__(self):
        while True:
            user_input = input("input a number:")

            match user_input:
                case 1:  # make a ticket
                    staff_ID = input("input staff ID")
                    email = input("input email")
                    creator_name = input("input creator_name")
                    description_issue = input(
                        "give a description of the issue: ")
                    Ticket(staff_ID, email, creator_name, description_issue)

                case 2:  # print stats of all tickets
                    print(Ticket.ticket_info_all())

                case 3:
                    # print stats of a ticket
                    pass
                case 4:
                    # add response to ticket
                    pass
                case 5:
                    # close a ticket
                    pass
                case 6:
                    # exit program
                    pass
                case _:
                    print("something went wrong :( ")


class Ticket():
    ID = 2000
    Ticket_list = list()
    amount_open = 0  # keeping track of the amout of tickets open

    def __init__(self, staff_ID, email, creator_name, description_issue):

        # values that gets inputed into the class
        self.UID = Ticket.ID
        Ticket.ID += 1

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
            pasword = self.staff_ID[:2]
            pasword += self.creator_name[:3]
            return pasword
        else:
            return "not yet provided"

    def Resolve(self, response):
        self.response = response
        self.close()

    def close(self):
        self.ticket_status = "closed"
        Ticket.amount_open -= 1

    def reopen(self):
        self.ticket_status = "reopened"
        Ticket.amount_open += 1

    def ticket_info(self):
        info = f"Ticket number: {self.UID}\n"
        info += f"Ticket creator: {self.creator_name}\n"
        info += f"Staff ID: {self.staff_ID}\n"
        info += f"Desctiption: {self.description_issue}\n"
        info += f"ticket status: {self.ticket_status}"
        return info

    def ticket_info_all(self):
        info = "--- Ticket Statistics ---\n"
        info += self.TicketStats + "\n"
        info += "------ Ticket Print ------"
        for ticket in Ticket.Ticket_list:
            info += ticket.ticket_info() + "\n\n"
        return info

    def TicketStats():
        stats = f"Tickets Created: {len(Ticket.Ticket_list)}\n"
        stats += f"Tickets Resolved: {Ticket.amount_open}\n"
        stats += f"Tickets to sovle: {len(Ticket.Ticket_list)- Ticket.amount_open}\n"
        return stats


if __name__ == "__main__":
    Main()
