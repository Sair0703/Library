class LibraryItem:  # This is the library item clss

    def __init__(self, library_item, title):
        self._library_item = library_item  # This is the init method for the library item class with the parameters self,_library_item_id, and title
        self._title = title  # we are making self.title and defining it as _title
        self._location = "ON_SHELF"  # We are defining the location of self being on the shelf
        self._checked_out_by = None  # Defining the checkout
        self._requested_by = None  # Defining the requesting of the book
        self._date_checked_out = 0  # Stating the date checked out and making it 0

    def get_library_item(self):  # This is the get_library_item_id function with the parameter of self

        return self._library_item  # Returns library item

    def get_title(self):  # This is the get_title function with the parameter self

        return self._title  # Returns self._title

    def get_location(self):  # This is the function get_location
        return self._location  # This function returns the location

    def get_checked_out_by(self):  # This is the function get_checked_out_by

        return self._checked_out_by  # Returns self._checked_out_by

    def get_requested_by(self):  # This is the function get_requested_by
        return self._requested_by  # This function returns requested by

    def get_date_checked_out(self):  # This is the function  get_date_checked_out
        return self._date_checked_out  # This function returns get_date_checked_out

    def set_date_checked_out(self,
                             current_date):  # The rest of the functions follow the same example as they have their own parameters and returns them
        self._date_checked_out = current_date  # This ome equalizes the date checked out to the current date

    def set_location(self, new_location):
        self._location = new_location

    def set_library_item_id(self, library_item):
        self._library_item = library_item

    def set_checked_out_by(self, patron):
        self._checked_out_by = patron

    def set_requested_by(self, patron):
        self._requested_by = patron


class Book(LibraryItem):
    def __init__(self, library_item, title, author):
        self._author = author
        self._date_checked_out = None
        super().__init__(library_item, title)

    def get_check_out_length(self):
        return 21

    def author(self):
        return self._author


class Album(LibraryItem):
    def __init__(self, library_item, title, musician):
        self._musician = musician
        self._date_checked_out = None
        super().__init__(library_item, title)

    def get_check_out_length(self):
        return 14

    def get_musician(self):
        return self._musician


class Movie(LibraryItem):
    def __init__(self, library_item, title, movie_director):
        self._director = movie_director
        self._date_checked_out = None
        super().__init__(library_item, title)


def get_check_out_length(self):
    return 7 # Returns


def get_director(self):
    return self._director


class Patron:
    def __init__(self, patron, name):
        self.patron = patron
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        return self._fine_amount

    def get_patron(self):
        return self.patron

    def get_name(self):
        return self._name

    def get_checked_out_items(self):
        return self._checked_out_items

    def add_library_item(self, library_item):
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        for item in self._checked_out_items:
            if item == library_item:
                self._checked_out_items.remove(item)

    def amend_fine(self, fine):
        self._fine_amount += fine


class Library: # This is the library class
    def __init__(self):
        self._current_date = 0  # made the holdings and members into lists for easiness
        self._holdings = []
        self._members = []

    def get_current_date(self):
        return self._current_date

    def add_library_item(self, library_item):
        self._holdings.append(library_item)

    def add_patron(self, patron):
        self._members.append(patron)

    def lookup_library_item_from_id(self, item):
        found = False
        for library_items in self._holdings:
            if item == library_items.get_library_item():
                found = True
                return library_items
        if not found:
            return None

    def lookup_patron_from_id(self, member):
        found = False
        for persons in self._members:
            if member == persons.get_patron():
                found = True
                return persons
        if not found:
            return None


def check_out_library_item(self, patron, library_item): # This is the check out library item function 
    patron = self.lookup_patron_from_id(patron)

    if patron is None:
        return "patron not found" # These statements make sure that if the patron and item is none they will print these results and not have errors
    if library_item is None:
        return "library_item not found"

    if patron == patron.get_patron_id():
        if library_item == library_item.get_library_item_id():
            if library_item.get_checked_out_by() is None:
                if patron == library_item.get_requested_by():
                    library_item.set_checked_out_by(patron) # Item was checked out by patron
                    library_item.set_date_checked_out(self._current_date) # The date in which the item was checked out
                    library_item.set_location("CHECKED_OUT") # The code will state that the item was checked out

                    if library_item.get_requested_by() == patron:
                        library_item.set_requested_by(None)
                        patron.add_library_item(library_item)
                        print("check out accomplished")

                else:
                    return "item is on hold"
            else:
                return "item has been checked out"
        else:
            return "item cannot be found"
    else:
        return "patron cannot be found"


def request_library_item(self, patron, library_item): # This is the request library item function with the parameters self, patron, and library item
    patron = self.lookup_patron_from_id(patron)
    library_item = self.lookup_library_item_from_id(library_item) # Looks for item using the library item id

    if patron is not None and patron == patron.get_patron_id():

        if library_item == library_item.get_library_item_id():

            if library_item.get_requested_by() is None:
                library_item.set_requested_by(patron)

                if library_item.get_location() == "ON_SHELF": # Location of the library item to get items
                    library_item.set_location("ON_HOLD_SHELF") #Location of the items when they are on hold

                print("request accomplished") # Prints the request

            else:
                return "item is currently on hold"
        else:
            return "item is not available"
    else:
        return "patron does not exist"


def return_library_item(self, library_item): # This is the function return library item
    library_item = self.lookup_library_item_from_id(library_item) # This equalizes the library item and looking up the specific item
    patron = library_item.get_checked_out_by()

    if library_item == library_item.get_library_item_id(): # This is the if statement for the library item return

        if library_item.get_checked_out_by() is not None:
            patron.remove_library_item(library_item) # If nobody checks out the item, then the item is removed

            if library_item.get_requested_by() is not None:
                library_item.set_location("ON_HOLD_SHELF")
                print("return victory") # If the item is requested by someone, then the item will get checked out

            else:
                library_item.set_location("ON_SHELF")
                print("return victory") #If the item is on the shelf, then the item will also be checked out

        else:
            return "item already in library" # If item is already in the library

    else:
        return "item not found" # If item is not found


def pay_fine(self, patron, payment):  # This is the pay fine function with the parameters self, patron_id and ccost
    patron = self.lookup_patron_from_id(patron)  # If statement for assessing the fine for the patron
    if patron == patron.get_patron_id():
        patron.give_fine(payment)
        print("payment accomplished")
    else:
        print("patron is not found")


def increment_current_date(self):  # Function for incrementing current date with parameter self

    self._current_date += 1  # For loop for  fine for the checked out items of the library

    for patron in self._members:
        for item in patron.get_checked_out_items():
            if (int(self._current_date) - int(item.get_date_checked_out())) > item.get_check_out_length():
                patron.give_fine(0.9)
                              # The amount of the fine that needs to be paid by the patron the for loop represents the fine
