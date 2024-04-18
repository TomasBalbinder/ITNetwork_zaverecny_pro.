from pojistenec import Pojistenec, Pojistenci
import msvcrt # Importing the msvcrt module for keyboard input handling

print("---------------------------\nEvidence pijistenych\n---------------------------")
print("\n")
print("Vyberte si akci:")

def menu():

    """
    Method to create a menu of actions.
    """
    return ("1 - Pridat noveho pojisteneho\n2 - Vypsat vsechny pojistene\n3 - Vyhledat pojisteneho\n4 - Konec")

if __name__ == "__main__":
    pojistenci = Pojistenci() # Creating an instance of the Pojistenci class for managing insured persons


end_program = True
while end_program:
    print(menu())  # Printing the menu of actions

    get_num = input("")  # Waiting for user input
    match get_num:

        case "1":
            # Adding a new insured person
            empty = True
            while empty:
                add_name = input("Zadejte jmeno pojisteneho: ")
                add_sur_name = input("Zadejte prijmeni: ")
                if len(add_name) > 3 and len(add_sur_name) > 3 :empty = False

            add_phone = input("Zadejte telefonni cislo: ")
            add_age = input("Zadejte vek: ")
            new_client = Pojistenec(add_name, add_sur_name, add_phone, add_age)
            pojistenci.add_client(new_client)
            print("\nData byla ulozena. Pokracujte libovolnou klavesnici...\n")
            msvcrt.getch()

        case '2':
            # Printing all insured persons
            pojistenci.shows_clients()
            print("\nPokracujte libovolnou klavesnici...\n")
            msvcrt.getch()

        case '3':
            # Searching for a specific insured person
            add_name = input("Zadejte jmeno pojisteneho: ")
            add_sur_name = input("Zadejte prijmeni: ")
            pojistenci.searching_client(add_name, add_sur_name)
            print("\nPokracujte libovolnou klavesnici...\n")
            msvcrt.getch()
           
        case '4':
            # Ending the program
            end_program = False





