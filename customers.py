"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,first_name,last_name,email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information"""

        return "<Customer: {}, {}, {}". format(self.first_name, 
                                                self.last_name, 
                                                self.email)

    customers = {}

    with open("customers.txt") as file:
        for line in file:
            (first_name, last_name, email,password) = line.strip().split("|")
            customers[email] = Customer(first_name, last_name, email, password)

    def get_by_email(email):
        """Return a customer, given its email"""

        return customers[email]
