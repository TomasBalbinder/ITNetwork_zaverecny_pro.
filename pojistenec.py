from dataclasses import dataclass

@dataclass
class Pojistenec:

    """
    Class representing an insured person.

    Attributes:
        name (str): The name of the insured person.
        surname (str): The surname of the insured person.
        phone (str): The phone number of the insured person.
        age (str): The age of the insured person.
    """
    name : str
    surename : str
    phone : str
    age : str


class Pojistenci:

    """
    Class representing a collection of insured persons.

    Attributes:
        clients (list): A list of insured persons.
    """

    def __init__(self):
        self.clients = []

    def print_client(self,client):

        """
        Prints the details of an insured person.

        Args:
            client : The insured person to print.
        """
        print(f"\n{client.name}  {client.surename}  {client.age}     {client.phone}")

    def add_client(self, client):
        """
        Adds an insured person to the list of clients.

        Args:
            client : The insured person to add.
        """
        self.clients.append(client)

    def shows_clients(self):
        """
        Prints details of all insured persons in the list.
        """
        for client in self.clients:
            self.print_client(client)
              
    def searching_client(self, name, surname):
        """
        Searches for an insured person by name and surname.

        Args:
            name (str)
            surname (str)
        """
        for client in self.clients:
            if client.name == name and client.surename == surname:
                self.print_client(client)
            else:
                print("\nKlient nenalezen.")

    
